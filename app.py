from flask import Flask, render_template, make_response
from weasyprint import HTML

app = Flask(__name__, static_folder='data', static_url_path='/data')

@app.route('/')
def index():
    """Renders the CV page from the HTML template."""
    return render_template('cv.html')

@app.route('/download')
def download_pdf():
    """Renders the CV as HTML, converts it to PDF, and serves it for download."""
    # Render the HTML template to a string
    html_string = render_template('cv.html', for_pdf=True)
    
    # Create a PDF file in memory from the HTML string
    pdf_bytes = HTML(string=html_string, base_url='.').write_pdf()
    
    # Create a response to send the PDF file to the user
    response = make_response(pdf_bytes)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=cv.pdf'
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)