# attendancetracker
##### Name: Viraj Rajendra Sanap (N043)
##### Class: MBA Tech Comp Science
##### Assignment for Vashishth Technologies

### Technologies Used:
- Python Flask - Framework
- HTML and CSS (Bootstrap) - For structure and styling
- JavaScript - For alerts and client-side validation
- AngularJS - For better processing and angular directives
- SQLite - For complete backend
- Flask Session - For user login
- mkdTemp - For linking templates

### Prerequisites to run:
- Python (IDLE) or any editor
- Flask libraries and extensions
- Virtual Environment
- Any database structure

### Steps to run:
- Open Python terminal.
- Type "set flask_env=development" to change from production to dev.
- Then, "set flask_app=application.py" to set the Flask Application.
- Open with localhost link.

### Pages
- Login Page
  - Enter your login details here.
  - Custom account can be created from server end.
  - Default id and password is "admin" and "admin" 
- Home Page
  - Enter the month and division you want to check attendance for.
  - View on Results page.
- Students Page
  - View all students here.
  - Add details of new student.
  - Remove/Delete details of existing student.
- Mark Attendance Page
  - Choose the Division first.
  - You can mark both divisions at the same time as well.
  - Enter date of attendance.
  - Mark respective student from dropdown.
- Settings Page
  - Change password here.

*Logout option is present on all pages.

### Backend
- All the Create Table queries are in the funtions.py.
- Backend database is in SQLite3.
- DB Browser was used to check data.
- All other Insert, Update and Delete queries are integrated in application.py.
