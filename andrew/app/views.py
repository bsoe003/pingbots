from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    title = "Test Title"
    category = "Most Popular Among Interns"
    queue = ["Hackathon 3D", "Mark Dankberg's big day", "Exede vs. Predator",
             "Sleeping on a Plane", "Test Video 1.5"]
    navbar = ["Action", "Nature", "Sports", "Space"]
    return render_template("base.html",
                           title=title,
                           category=category,
                           queue=queue,
                           navbar=navbar)
