from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Handle file upload
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

    # List files
    files = os.listdir(UPLOAD_FOLDER)
    file_links = [f"<a href='/download/{f}'>{f}</a><br>" for f in files]

    html = """
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                font-size: 20px;
                background-color: #232323;
                color: #EAEAEA;
                padding: 20px;
            }}
            h2 {{
                color: #FFD700;
            }}
            a {{
                color: #1E90FF;
            }}
        </style>
    </head>
    <body>
    <h2>w3bs1t3 4 tr4n5f3r1ng  f1l3$ 0v3r L4N</h2>
    <form action="/" method="post" enctype="multipart/form-data">
        <input type="file" name="file" style="height: 35px; font-size: 23px;">
        <input type="submit" value="Upload" style=" height: 35px; font-size: 23px;">
    </form>
    <br>
    <h3>Uploaded Files:</h3>
    {}
    </body>
    </html>
    """.format(''.join(file_links))

    return html

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
