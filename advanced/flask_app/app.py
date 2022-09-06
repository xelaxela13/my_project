import string
from random import choices

from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def generate_password():
    if request.method == "POST":
        password = ''.join(choices(string.ascii_letters + string.digits,
                                   k=int(request.form['password_length'])))
        return render_template('success.html', password=password)
    return render_template('generate_password.html')