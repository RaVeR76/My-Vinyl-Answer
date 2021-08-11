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


# Home
@app.route("/")
@app.route("/home")
def home():
    return render_template("pages/home.html")


# About 
@app.route("/about")
def about():
    return render_template("pages/about.html")


# Signup Function
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
            "password": generate_password_hash(request.form.get("password")),
            "profile_pic": request.form.get("profile_pic").lower()
        }
        mongo.db.users.insert_one(signup)

        # Utilise Session Cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful !")
        return redirect(url_for("profile"))

    return render_template("pages/signup.html")


# Login Function
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
                    flash("Welcome {}".format(
                        request.form.get("username")))
                    return redirect(url_for("profile"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("pages/login.html")


# Profile
@app.route("/user/profile", methods=["GET", "POST"])
def profile():
    # pull the session user's profile from the database
    users = mongo.db.users.find_one({"username": session["user"]})

    if session["user"]:
        return render_template("pages/profile.html", users=users)

    return redirect(url_for("login"))


# Get Vinyl Collection From The Database
@app.route("/vinyl/collection")
def my_vinyls():
    vinyls = list(mongo.db.vinyl.find())

    if session["user"] == 'admin':
        return render_template("pages/manage_vinyl.html", vinyl=vinyls)
    else:
        return render_template("pages/vinyl.html", vinyl=vinyls)


# Vinyl Query Function
@app.route("/vinyl/search", methods=["GET", "POST"])
def vinyl_search():
    query = request.form.get("vinyl_query")
    vinyls = list(mongo.db.vinyl.find({"$text": {"$search": query}}))

    if session["user"] == 'admin':
        return render_template("pages/manage_vinyl.html", vinyl=vinyls)
    else:
        return render_template("pages/vinyl.html", vinyl=vinyls)


# Logout Function
@app.route("/logout")
def logout():
    # remove user session cookies
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


# Add Vinyl Function
@app.route("/vinyl/add", methods=["GET", "POST"])
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
        return redirect(url_for("my_vinyls"))

    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("pages/add_vinyl.html", genre=genre)


# Edit Vinyl Function
@app.route("/vinyl/edit/<vinyl_id>", methods=["GET", "POST"])
def edit_vinyl(vinyl_id):

    genre = mongo.db.genre.find().sort("genre_name", 1)
    vinyl = mongo.db.vinyl.find_one({"_id": ObjectId(vinyl_id)})
    users = mongo.db.users.find_one({"username": session["user"]})
    owner = vinyl.get('owner')

    if request.method == "POST":
        vinyl_edit = {
            "genre_name": request.form.get("genre_name"),
            "vinyl_name": request.form.get("vinyl_name"),
            "vinyl_artist": request.form.get("vinyl_artist"),
            "vinyl_label": request.form.get("vinyl_label"),
            "vinyl_description": request.form.get("vinyl_description"),
            "release_year": request.form.get("release_year"),
            "owner": owner
        }

        mongo.db.vinyl.update({"_id": ObjectId(vinyl_id)}, vinyl_edit)
        flash("{} Has Been Successfully Updated".format(
            request.form.get("vinyl_name")))

        if session["user"] == 'admin':
            vinyl = mongo.db.vinyl.find_one({"_id": ObjectId(vinyl_id)})
            return render_template(
                "components/forms/vinyl_card.html", vinyl=vinyl, genre=genre, users=users)
        else:
            vinyl = mongo.db.vinyl.find_one({"_id": ObjectId(vinyl_id)})
            return render_template(
                "pages/edit_vinyl.html", vinyl=vinyl, genre=genre, users=users)

    return render_template(
        "pages/edit_vinyl.html", vinyl=vinyl, genre=genre, users=users)


# Delete Vinyl Function
@app.route("/vinyl/delete/<vinyl_id>")
def delete_vinyl(vinyl_id):
    mongo.db.vinyl.remove({"_id": ObjectId(vinyl_id)})
    flash("Your Vinyl Has Been Deleted")

    if session["user"] == 'admin':
        return redirect(url_for("vinyl_list"))
    else:
        return redirect(url_for("my_vinyls"))


# Vinyl Deletion Modal For Confirmation Purposes
@app.route("/delete/vinyl/confirm/<vinyl_id>")
def confirm_modal(vinyl_id):
    vinyl = mongo.db.vinyl.find_one({"_id": ObjectId(vinyl_id)})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template(
        "components/modals/confirm_modal.html", vinyl=vinyl, username=username)


# User Deletion Modal For Confirmation Purposes
@app.route("/delete/user/confirm/<user_id>")
def del_user_confirm(user_id):
    users = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template(
        "components/modals/del_user_confirm.html", users=users, username=username)


# Genre Deletion Modal For Confirmation Purposes
@app.route("/delete/genre/confirm/<genre_id>")
def del_genre_confirm(genre_id):
    genre = mongo.db.genre.find_one({"_id": ObjectId(genre_id)})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template(
        "components/modals/del_genre_confirm.html", genre=genre, username=username)


# Find Database collection names for displaying to Admin
@app.route("/admin/manage_site")
def manage_site():
    collection = mongo.db.collection_names(include_system_collections=False)
    collection.sort()

    return render_template("pages/manage_site.html", collection=collection)


# Redirect Admin To Chosen Database Collection Name
@app.route("/admin/manage_collection/<collection>")
def manage_collection(collection):

    if collection == "genre":
        return redirect(url_for("genre_list"))
    elif collection == "users":
        return redirect(url_for("users_list"))
    elif collection == "vinyl":
        return redirect(url_for("vinyl_list"))
    else:
        return redirect(url_for("manage_site"))


# Get Genre List Function (Alphabetically)
@app.route("/admin/genre")
def genre_list():

    genre = list(mongo.db.genre.find().sort("genre_name", 1))
    return render_template("pages/manage_genre.html", genre=genre)


# Get User List Function (Alphabetically)
@app.route("/admin/users")
def users_list():

    users = list(mongo.db.users.find().sort("username", 1))
    return render_template("pages/manage_users.html", users=users)


# Get vinyl List Function (Alphabetically)
@app.route("/admin/vinyl")
def vinyl_list():

    vinyl = list(mongo.db.vinyl.find().sort("vinyl_name", 1))
    return render_template("pages/manage_vinyl.html", vinyl=vinyl)


# Admin Add Genre Function
@app.route("/admin/genre/add", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genre.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("genre_list"))

    return render_template("components/forms/add_genre_form.html")


# Admin Edit Genre Function
@app.route("/admin/genre/edit/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genre.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Uddated")
        return redirect(url_for("genre_list"))

    genre = mongo.db.genre.find_one({"_id": ObjectId(genre_id)})
    return render_template(
        "components/forms/edit_genre_form.html", genre=genre)


# Admin Delete Genre Function
@app.route("/admin/genre/delete/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genre.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("genre_list"))


# Admin Edit User Function
@app.route("/admin/user/edit/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):

    users = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    password = users.get('password')

    if request.method == "POST":
        user_edit = {
            "fullname": request.form.get("fullname").lower(),
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": password,
            "profile_pic": request.form.get("profile_pic").lower()
        }

        mongo.db.users.update({"_id": ObjectId(user_id)}, user_edit)
        flash("{} Has Been Successfully Updated".format(
            request.form.get("username")))

        users = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return render_template(
            "components/forms/edit_user_form.html", users=users)

    return render_template(
        "components/forms/edit_user_form.html", users=users)


# Admin Delete User Function
@app.route("/admin/users/delete/<users_id>")
def delete_users(users_id):
    mongo.db.users.remove({"_id": ObjectId(users_id)})
    flash("User Successfully Deleted")
    return redirect(url_for("users_list"))


# Display vinyls to admin display card
@app.route("/admin/vinyl/vinyl_card/<vinyl_id>")
def vinyl_card(vinyl_id):
    vinyl = mongo.db.vinyl.find_one({"_id": ObjectId(vinyl_id)})
    return render_template(
        "components/forms/vinyl_card.html", vinyl=vinyl)


#@app.errorhandler(404)
#def page_not_found(error):
#    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
