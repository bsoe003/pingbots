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

@app.route('/<category>')
def category(category):
    cats = {'Popular':["Hackathon 3D",
                       "Mark Dankberg's Big Day",
                       "Exede vs. Predator",
                       "Sleeping on a Plane"],
            'Sports':["Local Sports Stars",
                      "Local Sports Stars II: Beating the Better Team"
                      "The Giant Football",
                      "The Pitcher and the Pilot",
                      "Intern Volleyball"],
            'Action':["Shooting People with Guns",
                      "A Conspicuous Conspirator",
                      "Things Exploding Just Far Enough Away"],
            'Nature':["When Ladybugs Attack",
                      "Roses: Artificial In-stamen-ation",
                      "Watermelons, Bananas, and Other Suggestive Plants",
                      "The Cabbage Revolution"],
            'Indie':["Hipsters Pretending to Understand Fake Concepts",
                     "Neutral Milk Hotel Slaying Dragons",
                     "Undead Elmo II"]}
    return render_template("base.html",
                           title="Category Page",
                           navbar=sorted(cats.keys()),
                           category=category,
                           queue=cats[category])

