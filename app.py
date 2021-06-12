from flask import Flask, render_template, request, redirect
import time

app = Flask(__name__)

class Messages():
    def __init__(self, sender, message, mtype):
        self.sender = sender
        self.message = message
        self.mtype = mtype
        

messagesQ = []

messagesQ.insert(0,Messages("user","Hi from user","str"))
messagesQ.insert(0,Messages("bot",["Hi from bot","2nd","3rd"], "list"))


@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html', messages = messagesQ)

@app.route('/chats',methods=['POST','GET'])
def character():
    if request.method == 'POST':
        user_query = request.form['query']
        messagesQ.insert(0,Messages("user",user_query,"str"))
        time.sleep(0)
        messagesQ.insert(0,Messages("bot","analyzed reply from bot","str"))
        return redirect('/')
    else:
        return render_template('index.html', messages = messagesQ)

if __name__ == "__main__":
    app.run(debug=True)