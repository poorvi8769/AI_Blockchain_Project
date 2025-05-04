from flask import Flask, render_template, request, jsonify, send_from_directory
from prediction import predict_threat
from blockchain import save_report_to_blockchain, verify_report_hash
import os
from web3 import Web3
import pandas as pd
from fpdf import FPDF

app = Flask(__name__)

if not os.path.exists('data'):
    os.makedirs('data')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    filepath = os.path.join('data', file.filename)
    file.save(filepath)

    try:
        # Analyze the file
        results = predict_threat(filepath)
        threats_present = any(r['predictions'] == 1 for r in results)

        # Generate a detailed PDF report
        report_path = os.path.join('data', 'detailed_report.pdf')
        generate_pdf_report(results, threats_present, report_path)

        # Log the report path to verify it is created
        print(f"Report saved at: {report_path}")

        # Save the report hash to the blockchain
        report_hash = save_report_to_blockchain(str(results))

        return render_template(
            'report.html',
            results=results,
            report_hash=report_hash,
            report_file='detailed_report.pdf'
        )
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500


@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'GET':
        return render_template('verify.html')

    # Handle POST request for verification
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    filepath = os.path.join('data', file.filename)
    file.save(filepath)

    try:
        # Read the uploaded PDF file in binary mode
        with open(filepath, 'rb') as f:
            report_content = f.read()

        # Compute the hash of the uploaded report
        computed_hash = Web3.keccak(report_content).hex()

        # Get the transaction hash from the form
        tx_hash = request.form.get('tx_hash')
        stored_hash = verify_report_hash(tx_hash)

        # Compare hashes to check integrity
        is_tampered = computed_hash != stored_hash

        return jsonify({'is_tampered': is_tampered})
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500


@app.route('/download/<filename>')
def download_file(filename):
    """
    Serve the specified file from the data directory for download.
    """
    try:
        # Absolute path to the data directory
        data_dir = os.path.join(os.getcwd(), 'data')

        # Check if the file exists
        if not os.path.exists(os.path.join(data_dir, filename)):
            return jsonify({'error': 'File not found'}), 404

        # Serve the file for download
        return send_from_directory(data_dir, filename, as_attachment=True)
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500


def generate_pdf_report(results, threats_present, filepath):
    """
    Generate a detailed PDF report using the FPDF library.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Threat Detection Report", ln=True, align="C")
    pdf.ln(10)

    # Add threat summary
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Threats Present: {'Yes' if threats_present else 'No'}", ln=True, align="L")
    pdf.ln(10)

    # Add detailed results
    pdf.cell(200, 10, txt="Detailed Analysis:", ln=True, align="L")
    pdf.ln(5)

    for result in results:
        pdf.multi_cell(0, 10, txt=str(result))

    # Save the PDF
    pdf.output(filepath)


if __name__ == '__main__':
    app.run(debug=True)
