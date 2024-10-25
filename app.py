import datetime
from flask import Flask, render_template, Response
import subprocess
import os
import platform
import shutil

app = Flask(__name__)

@app.route("/")
def index():
    hostname = platform.node()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total, used, free = shutil.disk_usage("/")
    total_space = f"{total // (2**30)} GB"
    free_space = f"{free // (2**30)} GB"

    try:
        top_output = subprocess.check_output(['top', '-bn1']).decode()
    except subprocess.CalledProcessError as e:
        top_output = f"Error running top: {e}"

    return render_template('index.html', hostname=hostname, current_date=current_date, total_space=total_space, free_space=free_space, top_output=top_output)

@app.route('/top')
def top_command():
    try:
        top_output = subprocess.check_output(['top', '-bn1']).decode()
        return Response(top_output, mimetype='text/plain')
    except subprocess.CalledProcessError as e:
        return Response(f"Error running top: {e}", mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
