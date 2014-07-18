from app import app, db, lm
from flask import render_template, g, redirect, session
from flask.ext.login import (
    login_user, logout_user, current_user, login_required, url_for
)
from random import randint
from forms import LoginForm
from models import User

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

@app.route('/downloads')
def downloads():
    queue=['Movie1',
           'Movie2']
    navbar=["index"]
    return render_template('categories.html',
                            title="Downloads Page",
                            queue=queue,
                            navbar=navbar,
                            category="Downloads"
                            )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.username.data is not None:
        login_user(load_user(form.username.data))
        return redirect(url_for('index'))
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           navbar=sorted(cats.keys()),
                           form=form)

@lm.user_loader
def load_user(name):
    for user in User.query.all():
        if user.username == name:
            return user
