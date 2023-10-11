import os
from flask import Blueprint, render_template, request

views = Blueprint('views',__name__,)

# home route
@views.route('/')
def home():
    return render_template('home.html', user={'name':'Evise', 'city':'Hometown'}, number_of_views=123)

# route for user data as a path
@views.route('/user/<path:user_data>')
def user(user_data):
    args=os.path.split(user_data)
    name=args[0]
    city=args[1]
    if not(name):
        name=city
        city=None
    return render_template('user_home.html', username=name, usercity=city)

@views.route('/user')
def user1():
    args=request.args
    name=args.get('name')
    city=args.get('city')
    return render_template('user_home.html', username=name, usercity=city)