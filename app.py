from flask import Flask, render_template

app = Flask(__name__)
# creating an app instance


# use a decorator @ to define the route for our web page
@app.route("/")
# setting up a default page
def index():
    return " Welcome DevOps team"

@app.route("/welcome/")
def welcome():
    return "Welcome on board"

@app.route("/home/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


# create two more pages/ routes and add the functionality for email and password
# implement oop inheritance


@app.route("/email/")
def get_email():
    return render_template("email.html")

@app.route("/password/")
def page_2():
    return render_template("password.html")