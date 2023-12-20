from os.path import exists
from flask import Flask, render_template, make_response, request
from flask.helpers import send_file
from werkzeug.utils import redirect
from subprocess import check_output

app = Flask(__name__)

@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/review", methods=["GET", "POST"]) # store indiv. reviews in separate cookies
def Review():
    if(request.method == "POST"):
        review_num = 0
        try:
            for cookie in request.cookies:
                if(cookie.startswith("feedback_")):
                    review_num = max(review_num, int(cookie.split("_")[1]))
        except:
            pass

        text = request.form["review"]
        resp = make_response(redirect("/review"))
        resp.set_cookie(f"feedback_{review_num + 1}", text)
        return resp

    else:
        reviews = []
        for cookie in request.cookies:
                if(cookie.startswith("feedback_")):
                    reviews.append((cookie, request.cookies[cookie]))
        return render_template("reviews.html", reviews=reviews)

@app.route("/debug")
def Debug():
    return render_template("debug.html")

@app.route("/download/templates", methods=["POST"])
def Download(): # vuln is here
    filename = request.form["template"]
    if(exists("templates/" + filename)):
        return send_file("templates/" + filename, as_attachment=True)
    else:
        return render_template("announce.html", title="Oh no!", message="Bargain Duck is dumbfounded. (File not found)")

@app.route("/ping", methods=["POST"])
def Ping(): # should be safe
    addr = request.form["addr"]
    if(not addr):
        return render_template("announce.html", title="Oh no!", message="No address given!")

    if any(illegal in addr for illegal in " !\"#$%&'()*+,/:;<=>?@[\\]^_`{|}~"):
        return render_template("announce.html", title="Oh no!", message="Invalid character(s) in given address!")
    else:
        try:
            res = check_output(["ping", "-c", "3", "-W", "5", addr]).replace(b"\n", b"<br>")
            return res
        except Exception:
            return render_template("announce.html", title="Oh no!", message="Error while pinging address!")

@app.route("/devmessage", methods=["POST"])
def DevMessage():
    return render_template("announce.html", title="Success", message="Message sent succesfully!")

if(__name__ == "__main__"):
    app.run()
