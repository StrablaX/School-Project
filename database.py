from flask import Flask, Response
from flask import request
import mysql.connector
import json

def connection():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '*',
        database = 'repos',
        charset = 'utf8',
    )

def get_repos_for_user(nickname):
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    sql = "select repoName,programmingLanguage,description,stars,forks from repos join users on users.id=repos.user_id where username=%s"
    result = cursor.execute(sql,(nickname,))
   
    return list(cursor)

def get_userdata(nickname):
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    sql = "select username,name,avatar from users where username=%s"
    result = cursor.execute(sql, (nickname,))
   
    return list(cursor)
