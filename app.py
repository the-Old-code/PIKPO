from flask import Flask, render_template, url_for
import controller
app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/reg')
def reg():
    return render_template("reg.html")


@app.route('/info')
def info():
    proc_file = controller.get_source()
    return render_template("info.html",proc_file=proc_file)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=False)