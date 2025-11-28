#!/usr/bin/python3
from flask import Flask, request, render_template_string, g, session, jsonify
import sqlite3
import os, hashlib, binascii

app = Flask(__name__)
raw_bytes = os.urandom(24)
app.secret_key = binascii.hexlify(raw_bytes).decode('utf-8')

def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(os.environ['DATABASE'])
  db.row_factory = sqlite3.Row
  return db

def query_db(query, args=(), one=False):
  cur = get_db().execute(query, args)
  rv = cur.fetchall()
  cur.close()
  return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()

@app.route('/')
def index():
  return "api-server"

@app.route('/api/me')
def me():
  if session.get('uid'):
    return jsonify(userid=session['uid'])
  return jsonify(userid=None)

@app.route('/api/login', methods=['POST'])
def login():
  userid = request.form.get('userid', '')
  password = request.form.get('password', '')
  if userid and password:
    ret = query_db(f"SELECT * FROM users where userid=? and password=?" , one=True, args=(userid, hashlib.sha256(password.encode()).hexdigest()))
    if ret:
      session['uid'] = ret[0]
      return jsonify(result="success", userid=ret[0])
  return jsonify(result="fail")

@app.route('/api/logout')
def logout():
  session.pop('uid', None)
  return jsonify(result="success")

@app.route('/api/join', methods=['POST'])
def join():
  userid = request.form.get('userid', '')
  password = request.form.get('password', '')
  if userid and password:
    conn = get_db()
    cur = conn.cursor()
    cur.execute("Insert into users values(?, ?);", (userid, hashlib.sha256(password.encode()).hexdigest()))
    conn.commit()
    return jsonify(result="success")
  return jsonify(result="error")

@app.route('/api/memo/add', methods=['PUT'])
def memoAdd():
  if not session.get('uid'):
    return jsonify(result="no login")

  userid = session.get('uid')
  title = request.form.get('title')
  contents = request.form.get('contents')

  if title and contents:
    conn = get_db()
    cur = conn.cursor()
    ret = cur.execute("Insert into memo(userid, title, contents) values(?, ?, ?);", (userid, title, contents))
    conn.commit()
    return jsonify(result="success", memoidx=ret.lastrowid)
  return jsonify(result="error")

@app.route('/api/memo/<idx>', methods=['GET'])
def memoView(idx):
  mode = request.args.get('mode', 'json')
  ret = query_db("SELECT * FROM memo where idx=?", args=(idx))[0]
  if ret:
    userid = ret['userid']
    title = ret['title']
    contents = ret['contents']
    if mode == 'html':
      template = ''' Written by {{userid}}<h3>{{title}}</h3>
      <pre>{{contents}}</pre>
      '''
      return render_template_string(template, title=title, userid=userid, contents=contents)
    else:
      return jsonify(result="success",
        userid=userid,
        title=title,
        contents=contents)
  return jsonify(result="error")

@app.route('/api/memo/<int:idx>', methods=['PUT'])
def memoUpdate(idx):
  if not session.get('uid'):
    return jsonify(result="no login")

  
  rows = query_db('SELECT * FROM memo where idx=?', [idx,])
  if not rows:
      return jsonify(result="error") # Memo not found

  userid = session.get('uid')
  title = request.form.get('title')
  contents = request.form.get('contents')

  if title and contents:
    conn = get_db()
    cur = conn.cursor()
    
    cur.execute("UPDATE memo SET title=?, contents=? WHERE idx=? AND userid=?", 
                (title, contents, idx, userid))
    conn.commit()
    
    if cur.rowcount > 0:
      return jsonify(result="success")
      
  return jsonify(result="error")