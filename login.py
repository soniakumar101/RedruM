from flask import Flask, render_template, redirect, flash, request, session
import model

app = Flask(__name__)
app.secret_key = "bgntjklhun6jr5hdbc bygtfdrc g6h65vt happy bday sonia"
modelsession = model.session

@app.route("/login", methods=["GET"])
def show_login():
    if "user_id" in session:
        del session["user_id"]
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    print email
    # password = request.form.get("password")

    user = modelsession.query(model.User).filter_by(email = email).first()
    print user

    if user:
         session["user_id"] = user.id
         flash("Successfully logged in")
         return redirect ("/")
    else:
         flash("Username not found")
         return redirect("/login") 
if __name__ == "__main__":
    app.run(debug = True)
