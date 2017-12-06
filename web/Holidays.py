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
    app.logger.error('Page not ound: %s',(request.path))
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

        empid = InputForm.EmployeeID.data

        print(empid)

        employee = Employee.get(empid)

        if employee:
            employeeHol = EmployeeHoliday.getAllbyUser(employee)

            takenHours = 0
            for hol in employeeHol:
                takenHours = takenHours + hol.Hours

            AvailableHolidays = Holiday.GetHolidaysByServiceDate(employee.ServiceDate)
            availableHours = 0
            for hol in AvailableHolidays:
                availableHours = availableHours + 8

            remainingHours = availableHours-takenHours
            HHours = []
            HHours.append(availableHours)
            HHours.append(takenHours)
            HHours.append(remainingHours)

            employee.UpdateLastViewed()

            print(HHours)

            return render_template("EmployeeSearch.html", Found=True, Hours=HHours, Holidays=employeeHol, form=InputForm)
        else:
            return "Unable to find Employee"
        
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
