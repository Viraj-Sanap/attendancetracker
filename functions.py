import sqlite3
from flask import redirect, render_template, request, session, flash
from functools import wraps


def create_table():
    connection = sqlite3.connect('attendance.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'prof'('id' INTEGER NOT NULL, 'username'	TEXT NOT NULL UNIQUE, 'hash'"
                   " TEXT NOT NULL,	PRIMARY KEY('id' AUTOINCREMENT))")

    cursor.execute("CREATE TABLE IF NOT EXISTS 'students'('s_id' TEXT NOT NULL, 'student_name' TEXT NOT NULL,"
                   "'prof' INTEGER NOT NULL, 'div' TEXT NOT NULL, PRIMARY KEY('div', 's_id') FOREIGN KEY(prof) "
                   "references prof(id) on delete cascade on update cascade)")

    cursor.execute("CREATE TABLE IF NOT EXISTS 'attendance'('a_id' INTEGER NOT NULL UNIQUE, 'date' TEXT NOT NULL, "
                   "'stu_div' TEXT NOT NULL, 'stud_id' TEXT NOT NULL, 'status' TEXT NOT NULL, "
                   "PRIMARY KEY('a_id' AUTOINCREMENT), "
                   "FOREIGN KEY('stu_div') REFERENCES 'students'('div') on delete cascade on update cascade, "
                   "FOREIGN KEY('stud_id') REFERENCES 'students'('s_id') on delete cascade on update cascade)")


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def apology(message):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    print(message)
    print(escape(message))
    flash(message)
    return render_template("login.html", top=message)


def stud_apology(message):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    print(message)
    print(escape(message))
    flash(message)

    connection = sqlite3.connect("attendance.db")
    connection.row_factory = sqlite3.Row
    db = connection.cursor()

    read = "SELECT * FROM students WHERE prof = ? ORDER BY div, s_id"
    db.execute(read, [session["user_id"]])
    student = db.fetchall()
    print(student)
    print(session["user_id"])

    return render_template("students.html", students=student)
