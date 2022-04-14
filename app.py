import subprocess
import os
from pathlib import Path
from uuid import uuid4

from flask import Flask, request, send_from_directory, g


UPLOAD_DIRECTORY = str(Path.home())
MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 30)) #In Megabyte

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIRECTORY
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE * 1000 * 1000


@app.route("/health", methods=['GET'])
def health():
    return {"message": "up like a murtherrrr "}, 200

@app.route("/", methods=['GET'])
def index():
    return {"message": "hello"}, 200

@app.route("/forms/libreoffice/convert", methods=['POST'])
def conversion_view():
    file = request.files.get('files')
    if not file:
        return {"error": "ensure file is passing in the request"}, 422
    
    ext = file.filename.split('.')[-1]
    filename = uuid4().hex+'.'+ext
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    source_file = f'{UPLOAD_DIRECTORY}/{filename}'
    
    subprocess.call(['libreoffice', '--headless', '--convert-to', 'pdf', source_file, "--outdir", UPLOAD_DIRECTORY])
    
    Path(source_file).unlink(missing_ok=True)
    
    new_name = f"{filename.split('.')[0]}.pdf"
    
    #Get reference for the uploaded file for deletion after response(True Stateless)
    g.dest_file = f'{UPLOAD_DIRECTORY}/{new_name}'
    
    return send_from_directory(app.config["UPLOAD_FOLDER"], new_name, as_attachment=True)

@app.after_request
def after_request_func(response):
    if hasattr(g, 'dest_file'):
        Path(g.dest_file).unlink(missing_ok=True)
    return response

if __name__ == '__main__':
    # app.run(port=3000, debug=True, host='0.0.0.0')
    app.run()
