from app import app
from flask import render_template

cats = {'popular':["Hackathon 3D",
                   "Mark Dankberg's Big Day",
                   "Exede vs. Predator",
                   "Sleeping on a Plane"],
        'sports':["Local Sports Stars",
                  "Local Sports Stars II: Beating the Better Team",
                  "The Giant Football",
                  "The Pitcher and the Pilot",
                  "Intern Volleyball"],
        'action':["Shooting People with Guns",
                  "A Conspicuous Conspirator",
                  "Things Exploding Just Far Enough Away"],
        'nature':["When Ladybugs Attack",
                  "Roses: Artificial In-stamen-ation",
                  "Watermelons, Bananas, and Other Suggestive Plants",
                  "The Cabbage Revolution"],
        'indie':["Hipsters Pretending to Understand Fake Concepts",
                 "Neutral Milk Hotel Slaying Dragons",
                 "Undead Elmo II"]}

@app.route('/')
@app.route('/index')
def index():
    title = "Downloads Home"
    return render_template("base.html",
                           title=title,
                           navbar=sorted(cats.keys()))

@app.route('/<category>')
def category(category):
    return render_template("base.html",
                           title="Category Page",
                           navbar=sorted(cats.keys()),
                           category=category,
                           queue=cats[category])

@app.route('/downloads')
def downloads():
    queue=['Movie1',
                'Movie2']
    navbar=["index"]
    return render_template('base.html',
                            title="Downloads Page",
                            queue=queue,
                            navbar=navbar,
                            category="Downloads"
                            )
