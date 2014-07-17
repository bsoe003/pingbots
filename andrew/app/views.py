from app import app
from flask import render_template, redirect

navbar = ["Action", "Nature", "Sports", "Space"]

@app.route('/')
@app.route('/index')
def index():
    title = "Test Title"
    category = "Most Popular Among Interns"
    queue = ["Hackathon 3D", "Mark Dankberg's big day", "Exede vs. Predator",
             "Sleeping on a Plane", "Test Video 1.5"]

    return render_template("base.html",
                           title=title,
                           category=category,
                           queue=queue,
                           navbar=navbar)

@app.route('/categories/<category>')
def category(category):
    cats = {'Popular':["Hackathon 3D",
                       "Mark Dankberg's Big Day",
                       "Exede vs. Predator",
                       "Sleeping on a Plane"],
            'Sports':["Local Sports Stars Beat Better Team",
                      "Man Punts Giant Football",
                      "The Pitcher and the Pilot"]}
    return render_template("base.html",
                           title="Category Page",
                           category=category,
                           queue=cats[category],
                           navbar=navbar)
