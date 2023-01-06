from flask import Blueprint, render_template, request, flash, jsonify,redirect
from flask_login import login_required, current_user
from .models import Note
from .models import Activities
from .models import current_stats
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/activities', methods=['GET', 'POST'])
@login_required
def activities():
    if request.method == 'POST':
        activity = request.form.get('new_activity')

        Charm = request.form.get('Charm')
        Proficency = request.form.get('Proficency')
        Kindness = request.form.get('Kindness')
        Knowledge = request.form.get('Knowledge')
        Guts = request.form.get('Guts')
        flash(request.form)

        if len(activity) < 1:
            flash('Put something', category='error')
        else:
            new_activity = Activities(activity_name=activity, user_id=current_user.id,proficency_effect=Proficency,charisma_effect=Charm,knowledge_effect=Knowledge,kindness_effect=Kindness,guts_effect=Guts)
            db.session.add(new_activity)
            db.session.commit()
            flash('Activity added!', category='success')
            #TODO for production
        return redirect('http://127.0.0.1:5000/activities')



    return render_template("activities.html",user=current_user)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    """
    

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/deleteActivity', methods=['POST'])
def deleteActivity():
    activity = json.loads(request.data)
    activityId = activity['activityId']
    activity =  Activities.query.get(activityId)
    if activity:
        if activity.user_id == current_user.id:
            db.session.delete(activity)
            db.session.commit()
            flash('Activity Deleted')
    return jsonify({})

@views.route('/CompletedActivity', methods=['POST'])
def CompletedActivity():
    activity = json.loads(request.data)
    activityId = activity['activityId']
    activity =  Activities.query.get(activityId)
    if activity:
        if activity.user_id == current_user.id:
            user_stats = current_stats.query.get(activity.user_id) 
            num1 = user_stats.proficency_level
            if activity.guts_effect != '':
                user_stats.guts_level += int(activity.guts_effect)
            if activity.kindness_effect != '':
                user_stats.kindness_level += int(activity.kindness_effect)
            if activity.knowledge_effect != '':
                user_stats.knowledge_level += int(activity.knowledge_effect)
            if activity.charisma_effect != '':
                user_stats.charisma_level += int(activity.charisma_effect)
            if activity.proficency_effect != '':
                user_stats.proficency_level += int(activity.proficency_effect)
            flash(num1)
            flash(user_stats.proficency_level)
            db.session.commit()
    return jsonify({})

