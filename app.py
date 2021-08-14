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
def home():
    """
    Homepage Function
    """
    return render_template("pages/home.html")


# About
@app.route("/about")
def about():
    """
    Genral Overview About The Website
    """
    return render_template("pages/about.html")


# Signup Function
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Allows a user to sign-up to the website
    Checks if username already exists
    Redirects user to their profile
    """
    if request.method == "POST":
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
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful !")
        return redirect(url_for("profile"))

    return render_template("pages/signup.html")


# Login Function
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows user/admin to sign in with their username & password
    Redirects to profile or manage site (depending on user)
    Redirects back to login either don't match the criteria
    """
    if request.method == "POST":
        known_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if known_user:
            if check_password_hash(known_user["password"],
                request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(
                    request.form.get("username")))
                if session["user"] == 'admin':
                    return redirect(url_for("manage_site"))
                else:
                    return redirect(url_for("profile"))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("pages/login.html")


# Logout Function
@app.route("/logout")
def logout():
    """
    Allow the user to log out
    Redirect user back to login
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Profile
@app.route("/user/profile", methods=["GET", "POST"])
def profile():
    """
    User's Profile
    """
    users = mongo.db.users.find_one({"username": session["user"]})
    if session["user"]:
        return render_template("pages/profile.html", users=users)

    return redirect(url_for("login"))


# Vinyl Collection
@app.route("/vinyl/collection")
def my_vinyls():
    """
    Get users vinyl collection from database
    Render vinyl templates depending if user / admin
    """
    vinyls = list(mongo.db.vinyl.find())

    if session["user"] == 'admin':
        return render_template("pages/manage_vinyl.html", vinyl=vinyls)
    else:
        return render_template("pages/vinyl.html", vinyl=vinyls)


# Vinyl Query Function
@app.route("/vinyl/search", methods=["GET", "POST"])
def vinyl_search():
    """
    Search vinyl collection & display results
    """
    query = request.form.get("vinyl_query")
    vinyls = list(mongo.db.vinyl.find({"$text": {"$search": query}}))

    if session["user"] == 'admin':
        return render_template("pages/manage_vinyl.html", vinyl=vinyls)
    else:
        return render_template("pages/vinyl.html", vinyl=vinyls)


# Hardcore Query Function
@app.route("/vinyl/hardcore/search")
def hardcore_search():
    """
    Search hardcore vinyl collection & display results
    """
    vinyls = list(mongo.db.vinyl.find({"genre_name": "Hardcore"}))

    return render_template("pages/manage_vinyl.html", vinyl=vinyls)


# House Query Function
@app.route("/vinyl/house/search")
def house_search():
    """
    Search house vinyl collection & display results
    """
    vinyls = list(mongo.db.vinyl.find({"genre_name": "House"}))

    return render_template("pages/manage_vinyl.html", vinyl=vinyls)


# Techno Query Function
@app.route("/vinyl/techno/search")
def techno_search():
    """
    Search techno vinyl collection & display results
    """
    vinyls = list(mongo.db.vinyl.find({"genre_name": "Techno"}))

    return render_template("pages/manage_vinyl.html", vinyl=vinyls)


# Trance Query Function
@app.route("/vinyl/trance/search")
def trance_search():
    """
    Search trance vinyl collection & display results
    """
    vinyls = list(mongo.db.vinyl.find({"genre_name": "Trance"}))

    return render_template("pages/manage_vinyl.html", vinyl=vinyls)


# Owner Query Function
@app.route("/vinyl/owner/search")
def owner_search():
    """
    Search trance vinyl collection & display results
    """
   # owner = mongo.db.vinyl.find().sort("owner", 1)
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    vinyls = list(mongo.db.vinyl.find({"owner": username}))
   # vinyls = list(mongo.db.vinyl.find({"$text": {"$search": owner}}))

    return render_template("pages/manage_vinyl.html", vinyl=vinyls)


# Add Vinyl Function
@app.route("/vinyl/add", methods=["GET", "POST"])
def add_vinyl():
    """
    Allow user to add new vinyl to the database
    Redirect for displaying vinyls with flash message
    Or return to 'add vinyl' page
    """
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
    """
    Allow user to edit their vinyl
    Add edited vinyl to database
    Render templates depending if user / admin
    """
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
                "components/forms/vinyl_card.html",
                vinyl=vinyl, genre=genre, users=users)
        else:
            vinyl = mongo.db.vinyl.find_one({"_id": ObjectId(vinyl_id)})
            return render_template(
                "pages/edit_vinyl.html", vinyl=vinyl, genre=genre, users=users)

    return render_template(
        "pages/edit_vinyl.html", vinyl=vinyl, genre=genre, users=users)


# Delete Vinyl Function
@app.route("/vinyl/delete/<vinyl_id>")
def delete_vinyl(vinyl_id):
    """
    Allow user / admin to delete vinyl
    Delete chosen vinyl
    Redirect depending if user / admin
    """
    mongo.db.vinyl.remove({"_id": ObjectId(vinyl_id)})
    flash("Your Vinyl Has Been Deleted")

    if session["user"] == 'admin':
        return redirect(url_for("vinyl_list"))
    else:
        return redirect(url_for("my_vinyls"))


# Vinyl Deletion Modal For Confirmation Purposes
@app.route("/delete/vinyl/confirm/<vinyl_id>")
def confirm_modal(vinyl_id):
    """
    Call vinyl delete modal for confirmation
    Pass vinyl & username for personal modal
    """
    vinyl = mongo.db.vinyl.find_one({"_id": ObjectId(vinyl_id)})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template(
        "components/modals/confirm_modal.html", vinyl=vinyl, username=username)


# User Deletion Modal For Confirmation Purposes
@app.route("/delete/user/confirm/<user_id>")
def del_user_confirm(user_id):
    """
    Call user delete modal for confirmation
    Pass users & username for personal modal
    """
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template(
        "components/modals/del_user_confirm.html",
        user=user, username=username)


# Genre Deletion Modal For Confirmation Purposes
@app.route("/delete/genre/confirm/<genre_id>")
def del_genre_confirm(genre_id):
    """
    Call genre delete modal for confirmation
    Pass genre & username for personal modal
    """
    genre = mongo.db.genre.find_one({"_id": ObjectId(genre_id)})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template(
        "components/modals/del_genre_confirm.html", genre=genre, username=username)


# Find Database collection names for displaying to Admin
@app.route("/admin/manage_site")
def manage_site():
    """
    Allow admin to access collections
    Find database collection names
    Pass to manage_site for utilisation
    """
    collection = mongo.db.collection_names(include_system_collections=False)
    collection.sort()

    return render_template("pages/manage_site.html", collection=collection)


# Redirect Admin To Chosen Database Collection Name
@app.route("/admin/manage_collection/<collection>")
def manage_collection(collection):
    """
    Redirect admin to chosen collection list
    Or back to manage site
    """
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
    """
    Get genre list & pass it to manage genre
    """
    genre = list(mongo.db.genre.find().sort("genre_name", 1))
    return render_template("pages/manage_genre.html", genre=genre)


# Get User List Function (Alphabetically)
@app.route("/admin/users")
def users_list():
    """
    Get users list & pass it to manage users
    """
    users = list(mongo.db.users.find().sort("username", 1))
    return render_template("pages/manage_users.html", users=users)


# Get vinyl List Function (Alphabetically)
@app.route("/admin/vinyl")
def vinyl_list():
    """
    Get vinyl list & pass it to manage vinyl
    """
    vinyl = list(mongo.db.vinyl.find().sort("vinyl_name", 1))
    return render_template("pages/manage_vinyl.html", vinyl=vinyl)


# Admin Add Genre Function
@app.route("/admin/genre/add", methods=["GET", "POST"])
def add_genre():
    """
    Allow admin to add a new genre
    Update the database
    """
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
    """
    Allow admin to edit a genre
    Update the database
    """
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
    """
    Allow admin to delete a genre
    Remove from the database
    """
    mongo.db.genre.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("genre_list"))


# Admin Edit User Function
@app.route("/admin/user/edit/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    """
    Allow admin to edit a user
    Update the database
    """
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
@app.route("/admin/users/delete/<user_id>")
def delete_users(user_id):
    """
    Allow admin to delete a user
    Remove from the database
    """
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("User Successfully Deleted")
    return redirect(url_for("users_list"))


# Display vinyls to admin display card
@app.route("/admin/vinyl/vinyl_card/<vinyl_id>")
def vinyl_card(vinyl_id):
    """
    Display admins chosen vinyl in a card
    """
    vinyl = mongo.db.vinyl.find_one({"_id": ObjectId(vinyl_id)})
    return render_template(
        "components/forms/vinyl_card.html", vinyl=vinyl)


# Display selected users vinyl collection to admin display card
@app.route("/admin/users/user_card/<user_id>")
def user_card(user_id):
    """
    Display admins chosen user in a card
    """
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    username = user.get('username')
    vinyls = list(mongo.db.vinyl.find({"owner": username}))
    return render_template(
        "components/forms/user_card.html", user=user, vinyls=vinyls)


@app.errorhandler(404)
def page_not_found(error):
    """
    Renders custom error.html with 404 message.
    """
    error_message = str(error)
    return render_template('pages/error.html',
                           error_message=error_message), 404


@app.errorhandler(500)
def server_error(error):
    """
    Renders custom error.html with 500 message.
    """
    error_message = str(error)
    return render_template('pages/error.html',
                           error_message=error_message), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
