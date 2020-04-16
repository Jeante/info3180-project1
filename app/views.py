"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import ProfileForm
from app.models import UserProfile
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
import os, random
from datetime import datetime



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

now = datetime.now() 


@app.route("/profile", methods=["GET", "POST"])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        fn = request.form['firstname']
        ln = request.form['lastname']
        em = request.form['email']
        im = request.files['photo']
        lo = request.form['location']
        ge = request.form['gender']
        bi = request.form['biography']
        filename = secure_filename(im.filename)
        im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        date = now.strftime("%m/%d/%Y")
        new = UserProfile(fn, ln, em, ge, lo, bi, filename, date)
        db.session.add(new)
        db.session.commit()
        flash('File Saved', 'success')
        return redirect(url_for('profiles'))
    return render_template("profile.html", form=form)


@app.route('/profiles')
def profiles():

    users=UserProfile.query.all()

    if request.method == "GET":

        return render_template("profiles.html", users=users)


@app.route('/profile/<userid>', methods=['POST', 'GET'])
def user_spec(userid):
    user = UserProfile.query.filter_by(id=userid).first()
    return render_template("profilespec.html", user=user)
    
# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session

@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
