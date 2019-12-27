from flask import Flask, Response
from flask import request, render_template, session
import database as db
import json

app=Flask(__name__)



@app.route('/getrepos/<username>', methods=['GET'])
def getrepos(username):
    rv = {}
    rv["persondata"] = db.get_userdata(username)[0]
    rv["repos"] = db.get_repos_for_user(username)
    resp = Response(json.dumps(rv))
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/getdata/<username>', methods=['GET'])
def getdata(username):
    resp = Response(json.dumps(db.get_userdata(username)))
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return json.dumps(db.get_userdata(username))

@app.route('/makerepos', methods=['POST'])
def makerepos():
    return json.dumps(db.insert_repos(request.json))



if __name__=="__main__":
    app.run(debug=True)
