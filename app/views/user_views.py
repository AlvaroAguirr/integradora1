from flask import Blueprint, render_template, redirect, url_for, flash, abort


user_views = Blueprint ('user',__name__)

@user_views.route("/login")
def login():
    return render_template('users/login.html')

@user_views.route("/home")
def adm_home():
    return render_template('home/menu_adm.html')