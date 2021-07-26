import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check for username
        known_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if known_user:
            flash("Username Already Exists .... Sorry !")
            return redirect(url_for("signup"))

        signup = {
            "fullname": request.form.get("fullname").lower(),
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        # Utilise Session Cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful !")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in the database
        known_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if known_user:
            # check password matches user
            if check_password_hash(
                    known_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # pull the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/get_vinyls")
def get_vinyls():
    vinyls = list(mongo.db.vinyl.find())
    return render_template("vinyl.html", vinyl=vinyls)


@app.route("/logout")
def logout():
    # remove user session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_vinyl", methods=["GET", "POST"])
def add_vinyl():
    if request.method == "POST":

        vinyl = {
            "genre_name": request.form.get("genre_name"),
            "vinyl_name": request.form.get("vinyl_name"),
            "vinyl_artist": request.form.get("vinyl_artist"),
            "vinyl_label": request.form.get("vinyl_label"),
            "vinyl_description": request.form.get("vinyl_description"),
            "release_year": request.form.get("release_year"),
            "owner": session["user"]
        }

        mongo.db.vinyl.insert_one(vinyl)
        flash("Your Vinyl Has Been Successfully Added")
        return redirect(url_for("get_vinyls"))

    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("add_vinyl.html", genre=genre)


@app.route("/edit_vinyl/<vinyl_id>", methods=["GET", "POST"])
def edit_vinyl(vinyl_id):
    if request.method == "POST":
        vinyl_edit = {
            "genre_name": request.form.get("genre_name"),
            "vinyl_name": request.form.get("vinyl_name"),
            "vinyl_artist": request.form.get("vinyl_artist"),
            "vinyl_label": request.form.get("vinyl_label"),
            "vinyl_description": request.form.get("vinyl_description"),
            "release_year": request.form.get("release_year")
        }
        mongo.db.vinyl.update({"_id": ObjectId(vinyl_id)}, vinyl_edit)
        flash("Your Vinyl Has Been Successfully Updated")

    vinyl = mongo.db.vinyl.find_one({"_id": ObjectId(vinyl_id)})
    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("edit_vinyl.html", vinyl=vinyl, genre=genre)


@app.route("/delete_vinyl/<vinyl_id>")
def delete_vinyl(vinyl_id):
    mongo.db.vinyl.remove({"_id": ObjectId(vinyl_id)})
    flash("Your Vinyl Has Been Deleted")
    return redirect(url_for("get_vinyls"))


@app.route("/confirm_modal/<vinyl_id>")
def confirm_modal(vinyl_id):
    vinyl = mongo.db.vinyl.find_one({"_id": ObjectId(vinyl_id)})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("confirm_modal.html", vinyl=vinyl, username=username)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
