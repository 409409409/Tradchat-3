from flask import Flask, render_template, render_template_string, redirect, request, flash
from flask_socketio import SocketIO
from werkzeug.utils import secure_filename
import sqlite3
import os
import secrets


# Create application and Server

app = Flask(__name__)
app.secret_key = secrets.token_hex(64)
Server = SocketIO(app)



accounts_db_exists = os.path.exists("accounts.db")
rooms_db_exists = os.path.exists("rooms_names.db")

# make basic databases
accounts_db = sqlite3.connect("accounts.db")
accounts = accounts_db.cursor()

room_names_db = sqlite3.connect("rooms_names.db")
room_names = room_names_db.cursor()

# Create tables if databases didn't exist
if not accounts_db_exists:
    accounts.execute('''
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            DOB TEXT NOT NULL,
            theme TEXT NOT NULL
        )
    ''')
    accounts_db.commit()

if not rooms_db_exists:
    room_names.execute('''
        CREATE TABLE rooms (
            roomid INTEGER PRIMARY KEY AUTOINCREMENT,
            roomname TEXT NOT NULL,
            roomtype TEXT NOT NULL,
            invites TEXT
        )
    ''')
    room_names_db.commit()



@app.route('/')
def index():
    return render_template('welcome.html')


# Configure upload settings
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'css', 'html', 'js', 'png', 'jpg', 'jpeg', 'gif', 'svg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_ext = filename.rsplit('.', 1)[1].lower()
            
            # Determine upload directory based on file type
            if file_ext == 'css':
                upload_dir = 'static/css'
            elif file_ext in ['png', 'jpg', 'jpeg', 'gif', 'svg']:
                upload_dir = 'static/graphics'
            elif file_ext == 'js':
                upload_dir = 'static/javascript'
            elif file_ext == 'html':
                upload_dir = 'templates'
            else:
                flash('File type not allowed')
                return redirect(request.url)
            
            # Ensure directory exists
            os.makedirs(upload_dir, exist_ok=True)
            
            # Save file
            file_path = os.path.join(upload_dir, filename)
            file.save(file_path)
            flash(f'File {filename} uploaded successfully to {upload_dir}')
            return redirect(request.url)
        else:
            flash('File type not allowed')
    
    return render_template('upload.html')


if __name__ == "__main__":
    Server.run(app, host='localhost', port=80, debug=True)