from flask import Flask, render_template, jsonify
from utils import *

app = Flask(__name__, template_folder="templates")
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def main_page():
    return render_template("index.html", m=load_all())

app.run()