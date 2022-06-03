# render_template is how the flask will be able to render the html file
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Test.html")



if __name__ == "__main__":
    app.run()