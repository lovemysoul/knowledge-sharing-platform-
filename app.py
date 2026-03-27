from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB="knowledge.db"


def connect_db():
    return sqlite3.connect(DB)


def create_tables():

    conn=connect_db()
    cur=conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        category TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS answers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id INTEGER,
        answer TEXT
    )
    """)

    conn.commit()
    conn.close()


create_tables()


@app.route("/ask", methods=["POST"])
def ask():

    data=request.json

    conn=connect_db()
    cur=conn.cursor()

    cur.execute(
        "INSERT INTO questions(title,description,category) VALUES(?,?,?)",
        (data["title"],data["description"],data["category"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message":"question added"})


@app.route("/questions", methods=["GET"])
def questions():

    conn=connect_db()
    cur=conn.cursor()

    cur.execute("SELECT * FROM questions")
    rows=cur.fetchall()

    result=[]

    for r in rows:
        result.append({
            "id":r[0],
            "title":r[1],
            "description":r[2],
            "category":r[3]
        })

    conn.close()

    return jsonify(result)


@app.route("/answer", methods=["POST"])
def answer():

    data=request.json

    conn=connect_db()
    cur=conn.cursor()

    cur.execute(
        "INSERT INTO answers(question_id,answer) VALUES(?,?)",
        (data["question_id"],data["answer"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message":"answer added"})


@app.route("/answers/<int:qid>", methods=["GET"])
def get_answers(qid):

    conn=connect_db()
    cur=conn.cursor()

    cur.execute("SELECT answer FROM answers WHERE question_id=?", (qid,))
    rows=cur.fetchall()

    result=[]

    for r in rows:
        result.append({"answer":r[0]})

    conn.close()

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)