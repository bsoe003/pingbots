from app import app
from flask import render_template, redirect
from random import randint

class Video:
    def __init__(self, name, 
                 maxSpeed=50):
        self.name = name
        self.size = round(randint(10, 100000000000) / 10**9, 2) # megabytes?
        self.votes = randint(1, 20)
        self.time = self._time(maxSpeed)
        self.contribution = self._contribution()

    def _time(self, maxSpeed):
        speed = self.votes*12 if maxSpeed > self.votes*12 else maxSpeed
        return round(self.size*1000 / float(speed) / 60, 1)

    def _contribution(self):
        result = round(self.size / float(self.votes), 2)
        return "%.2f" % result


cats = {'popular':[Video(x) for x in ["Hackathon 3D",
                                      "Mark Dankberg's Big Day",
                                      "Exede vs. Predator",
                                      "Sleeping on a Plane"]],
        'sports':[Video(x) for x in ["Local Sports Stars",
                                     "Local Sports Stars II: Beating the Better Team",
                                     "The Giant Football",
                                     "The Pitcher and the Pilot",
                                     "Intern Volleyball"]],
        'action':[Video(x) for x in ["Shooting People with Guns",
                                     "A Conspicuous Conspirator",
                                     "Things Exploding Just Far Enough Away"]],
        'nature':[Video(x) for x in ["When Ladybugs Attack",
                                     "Roses: Artificial In-stamen-ation",
                                     "Watermelons, Bananas, and Other Suggestive Plants",
                                     "The Cabbage Revolution"]],
        'indie':[Video(x) for x in ["Hipsters Pretending to Understand Fake Concepts",
                                    "Neutral Milk Hotel Slaying Dragons",
                                    "Undead Elmo II"]]}

@app.route('/')
@app.route('/index')
def index():
    title = "Downloads Home"
    return render_template("category.html",
                           title=title,
                           navbar=sorted(cats.keys()),
                           fadeIn=True)

@app.route('/<category>')
def category(category):
    return render_template("category.html",
                           title="Category Page",
                           navbar=sorted(cats.keys()),
                           category=category,
                           queue=cats[category],
                           fadeIn=False)
