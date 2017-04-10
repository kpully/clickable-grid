from flask import Flask, jsonify, render_template, request, redirect, flash, json
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from app import app

import numpy as np
import math

import pandas as pd




@app.route('/')
def index():
	return render_template('index.html')

@app.route('/_grid', methods=["GET", "POST"])
def grid():
	x = request.form['x']
	y = request.form['y']
	return render_template('grid.html', x=x, y=y)
