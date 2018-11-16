from flask import render_template, request, redirect, url_for
from . import main

#views
@main.route('/')
def index():
    '''
    Returns index page and it's data
    '''
    return render_template('index.html', title = title)