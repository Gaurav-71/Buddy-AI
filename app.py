import re
from flask import Flask, render_template, request, redirect
import time
import uuid

app = Flask(__name__)

def generateEmail(string):
    return string.replace(" ", "").lower()+"@unisys.com"

class Messages():
    def __init__(self, sender, message, mtype):
        self.sender = sender
        self.message = message
        self.mtype = mtype
        

messagesQ = []

messagesQ.insert(0,Messages("user","Hi from user","str"))
messagesQ.insert(0,Messages("bot",["Hi from bot","2nd","4th"], "list"))


class Employee():
    def __init__(self, name, role):
        self.id = uuid.uuid4()
        self.name = name
        self.role = role
        self.email= generateEmail(name)

employees = []

employees.insert(0,Employee("Aishwarya G","Designer"))
employees.insert(0,Employee("Gaurav V","Software Engineer"))

class Track():
    def __init__(self, role, slack, training, orientation, date,time):        
        self.role = role
        self.slack = slack
        self.training = training
        self.orientation = orientation
        self.date = date
        self.time = time
        

tracks = []

tracks.insert(0,Track("Designer","https://slack.com/designer-group","https://coursera.org/design-course","https://zoom.us/123","2021-06-19", "04:00"))
tracks.insert(0,Track("Software Engineer","https://slack.com/se-group","https://coursera.org/se-course","https://zoom.us/132","2021-06-21", "04:00"))



@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html', messages = messagesQ)

@app.route('/chats',methods=['POST','GET'])
def character():
    if request.method == 'POST':
        
        if request.form.get("b0"):
            user_query = request.form['query']

        elif request.form.get("b1"):
            user_query = "Onboard me"

        elif request.form.get("b2"):
            user_query = "View Team & Team Mates"

        elif request.form.get("b3"):
            user_query = "About Unisys"
        
        elif request.form.get("b4"):
            user_query = "Latest News"
        
        elif request.form.get("b5"):
            user_query = "Nearby Restaurants"

        elif request.form.get("b6"):
            user_query = "Generate My Email"

        elif request.form.get("b7"):
            user_query = "Join Team Slack Channel"

        elif request.form.get("b8"):
            user_query = "Visit unisys.com"
        
        else:
            pass
        
        messagesQ.insert(0,Messages("user",user_query,"str"))
        messagesQ.insert(0,Messages("bot","analyzed reply from bot","str"))
        return redirect('/')
    else:
        return render_template('index.html', messages = messagesQ)

@app.route("/admin",methods=['POST','GET'])
def admin():
    return render_template("admin.html")

@app.route("/employee",methods=['POST','GET'])
def employee():
    if request.method == 'POST':
        employees.insert(0,Employee(request.form["name"],request.form["role"]))
        return redirect("/employee")
    else:
        return render_template("employee.html",  employees = employees)

@app.route("/tracks",methods=['POST','GET'])
def track():
    if request.method == 'POST':
        dt = request.form["date"].split('T')
        tracks.insert(0,Track(request.form["role"],request.form["slack"],request.form["training"],request.form["orientation"],dt[0], dt[1]))
        return redirect("/tracks")
    else:
        return render_template("tracks.html", tracks = tracks)



if __name__ == "__main__":
    app.run(debug=True)