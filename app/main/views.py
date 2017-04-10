from flask import Flask, jsonify, render_template, request, redirect, flash, json
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from . import main

import numpy as np
import math

import pandas as pd




@main.route('/')
def index():
	return render_template('index.html')

@main.route('/_grid', methods=["GET", "POST"])
def grid():
	x = request.form['x']
	y = request.form['y']
	return render_template('grid.html', x=x, y=y)

@main.route('/_matching_ceremony')
def matching_ceremony():
	return render_template(matching_ceremony.html)
