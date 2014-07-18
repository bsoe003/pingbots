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

hardcoded = Video("Exede vs. Predator")
hardcoded.votes = 49

cats ={'comedy': sorted([Video(x) for x in ["Three Days and a Night in Atlanta",
                                            "Mark Dankberg's Big Day",
                                            "Sleeping on a Plane"]], key=lambda vid: vid.votes, reverse=True),
       'sports':sorted([Video(x) for x in ["Local Sports Stars",
                                            "Local Sports Stars II: Beating the Better Team",
                                            "The Giant Football",
                                            "Hackathon 3D",
                                            "Intern Volleyball"]], key=lambda vid: vid.votes, reverse=True),
       'action':sorted([Video("Shooting People with Guns"),
                        Video("A Conspicuous Conspirator"),
                        hardcoded,
                        Video("Things Exploding Just Far Enough Away")], key=lambda vid: vid.votes, reverse=True),
       'nature':sorted([Video(x) for x in ["When Ladybugs Attack",
                                            "Roses: Artificial In-stamen-ation",
                                            "Watermelons, Bananas, and Other Suggestive Plants",
                                            "The Cabbage Revolution"]], key=lambda vid: vid.votes, reverse=True),
       'indie':sorted([Video(x) for x in ["Hipsters Pretending to Understand Fake Concepts",
                                          "Neutral Milk Hotel Slaying Dragons",
                                          "Undead Elmo II"]], key=lambda vid: vid.votes, reverse=True)}

@app.route('/')
@app.route('/index')
def index():
    title = "Downloads Home"
    return render_template("category.html",
                           title=title,
                           navbar=sorted(cats.keys()),
                           fadeIn=True)


@app.route('/<category>', defaults={'inc': None})
@app.route('/<category>/<inc>')
def category(category, inc):
    return render_template("category.html",
                           title="Category Page",
                           navbar=sorted(cats.keys()),
                           category=category,
                           queue=cats[category],
                           inc=inc,
                           fadeIn=False)
