from flask import session, redirect, url_for, render_template, request
#from model import User, session as dbsession
from . import main
from .forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
    """"Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        session['room2'] = form.room2.data
        session['mafia'] = form.mafia.data
        session['narrator'] = form.narrator.data
        session['users'] = {'user_1': ["Simon Says", "pass1", "public", "alive"],

    'user_2' : ["Black Mamba", "pass2", "killer", "alive"],
  
    'user_3' : ["Matilda Berkhart", "pass3", "narrator", "alive"],
    
    'user_4' : ["Sesame Street", "pass4", "public", "alive"],

    'user_5' : ["Busta Move", "pass5", "public", "alive"],

    'user_6' : ["Monkey Butt", "pass6", "public", "alive"],

    'user_7' : ["Hakuna Matata", "pass7", "public", "alive"],

    'user_8' : ["Ape Attack", "pass8", "killer", "alive"],

    'user_9' : ["Robot Ninja", "pass9", "public", "alive"],

    'user_10' : ["Turtle Dove", "pass10", "public", "alive"]}

        print session['mafia']
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
        form.room2.data = session.get('room2', '')
        form.mafia.data = session.get('mafia', '')
        form.narrator.data = session.get('narrator', '')
        print ('session')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    room2 = session.get('room2', '')
    mafia = session.get('mafia', '')
    narrator = session.get('narrator', '')
    users = session.get('users', '')
    #dbsession.add(name)
    #dbsession.commit()
    print ('sessionmafia')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room, room2=room2)

