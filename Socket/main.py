from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
from string import ascii_uppercase
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "jfjajpifauhgpofgajh"
socketio = SocketIO(app)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)