from flask import Flask, render_template

app = Flask(__name__) # This helps Flask find all our files and directory here. 

#  CREATING A ROUTE DECORATOR 
      # Our website needs a url. Eg. www.yourwebsite.com/index.html ___ This index.html is a route that we've to create.  

@app.route("/")
def index():
    first_name = "Shairfa Gul"
    stuff = "This is a bold text."
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
  app.run(debug=True)