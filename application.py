import os
import time
import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from functools import wraps
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from functions import login_required, create_table, apology, stud_apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

current = os.path.dirname(os.path.abspath(__file__))


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    if request.method == 'POST':
        month = request.form.get("month")
        year = request.form.get("year")
        division = request.form.get("division")

        print(session["user_id"])
        return result(month, year, division)

    else:
        month = request.form.get("month")
        year = request.form.get("year")
        division = request.form.get("division")

        print(session["user_id"])
        return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
@login_required
def result(month, year, division):

    if month == "January":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-01-01' AND '2022-01-31') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "February":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "March":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "April":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "May":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "June":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "July":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "August":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "September":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "October":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "November":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)

    elif month == "December":

        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT s.div, s.s_id, s.student_name, (SELECT COUNT(*) FROM attendance WHERE status = 'Present' and " \
               "date BETWEEN '2022-02-01' AND '2022-02-28') as present, (SELECT COUNT(*) FROM attendance WHERE " \
               "status = 'Absent' and date BETWEEN '2022/02/01' AND '2022/02/31') as absent from students s inner " \
               "join attendance a on (s.s_id = a.stud_id) where s.prof = ? AND s.div = ?"

        db.execute(read, [session["user_id"], division])
        students = db.fetchall()
        print(students)
        print(session["user_id"])

        return render_template("result.html", students=students, month=month, year=year, division=division)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    create_table()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Query database for username

        connection = sqlite3.connect(r"C:\Users\Viraj\PycharmProjects\attendance\attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()
        read = "SELECT * FROM prof WHERE username = ?"
        db.execute(read, [username])
        user_one = db.fetchone()
        print(user_one)
        print(password)
        # Ensure username exists and password is correct
        if user_one is None:
            message = "Username does not exist!"
            return apology(message)

        if not (user_one[2] == password):
            message = "Invalid password!"
            return apology(message)

        # Remember which user has logged in
        session["user_id"] = user_one[0]

        # Redirect user to home page
        return redirect("/")

        # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/students", methods=["GET", "POST"])
@login_required
def students():
    if request.method == 'POST':

        s_id = request.form.get("s_id")
        student_name = request.form.get("student_name")
        division = request.form.get("division")
        del_stud = request.form.get("symbol")

        if del_stud is None:
            connection = sqlite3.connect("attendance.db")
            connection.row_factory = sqlite3.Row
            db = connection.cursor()

            read = "SELECT * FROM students WHERE s_id = ? AND div = ? ORDER BY s_id"
            db.execute(read, [s_id, division])
            students = db.fetchone()
            print(students)
            print(session["user_id"])

            if students is not None:
                return stud_apology("Student Already Exists")

            insert = "INSERT INTO students (s_id, student_name, div, prof) VALUES(?, ?, ?, ?)"
            db.execute(insert, (s_id, student_name, division, session["user_id"],))
            connection.commit()
            print(insert)

            read = "SELECT * FROM students WHERE prof = ? ORDER BY div, s_id"
            db.execute(read, [session["user_id"]])
            students = db.fetchall()
            print(students)
            print(session["user_id"])

            flash("Student Added Successfully")

            return render_template("students.html", students=students)

        else:
            pass
            connection = sqlite3.connect("attendance.db")
            connection.row_factory = sqlite3.Row
            db = connection.cursor()
            deldiv, delsid = del_stud.split(' ', 1)

            delete = "DELETE FROM students WHERE div = ? AND s_id = ?"
            print(deldiv)
            print(delsid)
            print(del_stud)

            db.execute(delete, [deldiv, delsid])
            connection.commit()

            read = "SELECT * FROM students WHERE prof = ? ORDER BY s_id"
            db.execute(read, [session["user_id"]])
            students = db.fetchall()
            print(students)
            print(session["user_id"])

            flash("Student Deleted Successfully")

            return render_template("students.html", students=students)

    else:
        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()

        read = "SELECT * FROM students WHERE prof = ? ORDER BY div, s_id"
        db.execute(read, [session["user_id"]])
        student = db.fetchall()
        print(student)
        print(session["user_id"])

        return render_template("students.html", students=student)


@app.route("/mark", methods=["GET", "POST"])
@login_required
def mark():

    if request.method == 'POST':

        status = request.form.get("status")
        date = request.form.get("date")

        print(status)
        print(date)

        if status is not None:
            pass
            connection = sqlite3.connect("attendance.db")
            connection.row_factory = sqlite3.Row
            db = connection.cursor()

            stu_div, stud_id, stat = status.split(" ", 2)
            print(stud_id)
            print(stu_div)
            print(stat)
            print(status)
            print(date)

            insert = "INSERT INTO attendance (stud_id, stu_div, status, date) VALUES (?, ?, ?, ?)"
            db.execute(insert, (stud_id, stu_div, stat, date,))
            connection.commit()

            flash("Attendance marked successfully.")
        return render_template("mark.html")

    else:
        connection = sqlite3.connect("attendance.db")
        connection.row_factory = sqlite3.Row
        db = connection.cursor()
        read = "SELECT * FROM students WHERE prof = ? ORDER BY div, s_id"
        db.execute(read, [session["user_id"]])
        student = db.fetchall()

        read = "SELECT * FROM students WHERE prof = ? AND div = 'A'"
        db.execute(read, [session["user_id"]])
        studentA = db.fetchall()

        read = "SELECT * FROM students WHERE prof = ? AND div = 'B'"
        db.execute(read, [session["user_id"]])
        studentB = db.fetchall()

        print(student)
        print(session["user_id"])
        return render_template("mark.html", students=student, studentsA=studentA, studentsB=studentB)


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")