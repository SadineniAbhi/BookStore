from project import app, db
from flask import flash,redirect,render_template,url_for
from project.forms.signin import Signin
from project.forms.registeration import Registration
from project.models.user_model import User
from flask_login import login_user,login_required,logout_user

@app.route("/register",methods = ["GET","POST"])
def register():
    form = Registration()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                              email_address = form.email_address.data,
                              address = form.address.data,
                              password= form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("login"))
    
    #check errors
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"there was an error with creating a user:{err_msg}",category="danger")
    return render_template("register.html",form = form)

@app.route("/login",methods = ["GET","POST"])
def login():
    form = Signin()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')


            return redirect(url_for("show_books"))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("you have been logged out!!",category='info')
    return redirect(url_for('show_books'))