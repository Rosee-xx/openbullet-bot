import sqlite3
import flask
from flask import Flask
from flask.app import Flask, request, jsonify
from flask.helpers import send_file
import sqlite3
import random
import string
con = sqlite3.connect("Users.db", check_same_thread = False)
cur = con.cursor()
app = Flask(__name__)


def keygen(size=20, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

@app.route("/api", methods = ["GET"])
def login():
  headers = request.headers
  key = headers.get("Authorization")
  ip =  request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
  newkey = keygen()
  with open("blacklist.txt", "r") as f:
    if ip in f:
      return jsonify({"message": "ERROR: banned"}), 401
    else:
      cde = f"SELECT key from Users WHERE key='{newkey}' AND Ip = '{key}';"
      cur.execute(cde)
      if not cur.fetchone():  # An empty result evaluates to False.
        ipcheck = f"SELECT Ip from Users WHERE key='{key}' AND Ip = 'NULL';"
        cur.execute(ipcheck)
        if not cur.fetchone():
            print("wrong key or ip")
            return jsonify({"message": "The Key Or Ip Is Incorrect"}), 400
        else:
            set_ip = f"SELECT ip from Users WHERE Key='{key}' AND set Ip='{ip}';"
            con.commit(set_ip)
            return jsonify({"message": "We're Locking Your Ip To This Key"}), 200
      else:
        return jsonify({"message": "You logged In Succesfully"}), 200

app.run(host='0.0.0.0', port = 8000, threaded = True, debug = True)