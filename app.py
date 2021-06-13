import re
from flask import Flask, render_template, request, redirect
import time
import uuid
import webbrowser

app = Flask(__name__)

def generateEmail(string):
    return string.replace(" ", "").lower()+"@unisys.com"

class Messages():
    def __init__(self, message,mtype="str", sender="bot", ):
        self.sender = sender
        self.message = message
        self.mtype = mtype
        

messagesQ = []

messagesQ.insert(0,Messages("Hello, i am your onboarding buddy, i am here to make your transition into the company super smooth and easy."))

class Employee():
    def __init__(self, name, role, uid=uuid.uuid4()):
        self.id = uid
        self.name = name
        self.role = role
        self.email= generateEmail(name)

employees = []

employees.insert(0,Employee("Aishwarya G","Designer","0022bb2f-3909-4008-9gfa-3c472cge479u"))
employees.insert(0,Employee("Dheeraj Bhat","Software Engineer","3909-4738-4609-4738-9ef1-6c8603280c"))
employees.insert(0,Employee("Aravind Shreyas","Software Engineer","4609-4738-6032aa2e-9ef1-6c875cde480c"))
employees.insert(0,Employee("Gaurav V","Software Engineer","6032aa2e-4609-4738-9ef1-6c875cde480c"))

def searchEmployee(key):
    for index,emp in enumerate(employees):
        if emp.id == key:
            return index
        else:
            return -1

loggedUserUid = ""
currentEmployee = None

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


def analyzeMessage(message):
    currentEmployee = employees[0] 
    if "clear" in message:
        messagesQ.clear()
        messagesQ.insert(0,Messages("Cleared all messages succesfully !"))
    elif "role" in message or "position" in message :
        messagesQ.insert(0,Messages("You currently hold the job role of a "+currentEmployee.role))
    elif "hi" in message or "hello" in message or "yo" in message:
        messagesQ.insert(0,Messages("Hi, "+currentEmployee.name+". How are you doing today ?"))
    elif "good" in message or "great" in message:
        messagesQ.insert(0,Messages("That's wonderful, how may i help you ?"))
    elif "mail" in message:
        messagesQ.insert(0,Messages("Your company email id is : "+currentEmployee.email))
        messagesQ.insert(0,Messages("Please note this email id is provided only for office use."))
    elif "unisys.com" in message:
        messagesQ.insert(0,Messages("I have opened unisys.com in a new tab, hope you can find the relevant information you are looking for"))
        webbrowser.open("https://unisys.com",new=2)
    elif "slack" in message:
        if currentEmployee.role == "Software Engineer":
            for track in tracks:
                if track.role == "Software Engineer":
                    messagesQ.insert(0,Messages("The slack link for your team is : "+track.slack))
                    messagesQ.insert(0,Messages("Please click on the above link to join the group and stay updated with your team."))
        else:
            messagesQ.insert(0,Messages("There is no slack channel provided currently for your team."))
    elif "team" in message:
        mates = ""
        for emp in employees:
            if emp.role == "Software Engineer" and emp.name != "Gaurav V":
                mates =  emp.name + ", " + mates
        messagesQ.insert(0,Messages("You belong to the Software Engineering team."))
        messagesQ.insert(0,Messages("Your teammates are "+mates+" you can connect with them on your teams' slack channel."))
        
    else:
        messagesQ.insert(0,Messages("Sorry, I won't be able to answer that right now"))
        
    



@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html', messages = messagesQ, employee = currentEmployee)

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        loggedUserUid = request.form["user"]
        currentEmployee = employees[0]   
        if len(employees) == 0:
            messagesQ.insert(0,Messages("Hello, i am your onboarding buddy, i am here to make your transition into the company super smooth and easy."))
        return render_template("index.html", messages = messagesQ, employee = currentEmployee)
    else:
        return render_template("login.html")

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
            user_query = "Show My Email"

        elif request.form.get("b7"):
            user_query = "Join Team Slack Channel"

        elif request.form.get("b8"):
            user_query = "Visit unisys.com"
        
        else:
            pass
        
        messagesQ.insert(0,Messages(user_query,"str","user"))
        analyzeMessage(user_query.lower())
        return redirect('/')
    else:
        return render_template('index.html', messages = messagesQ, employee = currentEmployee)

@app.route("/admin",methods=['POST','GET'])
def admin():
    return render_template("admin.html")

@app.route("/employee",methods=['POST','GET'])
def employee():
    if request.method == 'POST':
        employees.append(Employee(request.form["name"],request.form["role"]))
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