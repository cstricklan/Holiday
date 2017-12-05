from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from flask import abort
from flask import Response
from flask import Session
from flask import flash

app = Flask(__name__)
app.config.from_pyfile('config.py')

from DBModel import *
from logic import *
from forms import EmployeeSearchForm


@app.errorhandler(404)
def Page_Not_Found(error):
    app.logger.error('Page not ound: %s',(requestion.path))
    return error
    
@app.before_request
def _db_connect():
    db.connect()
    
@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()
        
@app.route('/', methods=['GET','POST'])
def default():
    InputForm = EmployeeSearchForm()
    
    if InputForm.validate_on_submit():
        return render_template("EmployeeSearch.html", results=['ad'], form=InputForm)
        
    return  render_template("EmployeeSearch.html", form=InputForm)
    
@app.route('/admin')
def admin():
    return render_template('admin.html')
    
@app.route('/admin/LoadEmployees')
def LoadEmployees():
    return "Load Employees"
    
@app.route('/admin/LoadHolidays')
def LoadHolidays():
    return "Load Holidays"
