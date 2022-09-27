from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from projs import project_list

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route("/")
def home():
    time = datetime.now().hour
    return render_template("index.html", time=time, project_list=project_list)


@app.route("/projects/<int:proj_num>")
def projects(proj_num):
    total_proj = len(project_list)
    return render_template(f"{proj_num}.html", project_list=project_list, project_id=proj_num, total_proj=total_proj)


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
