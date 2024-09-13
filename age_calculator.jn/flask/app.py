from flask import Flask, render_template, request, redirect, url_for, session, flash

import sqlite3

# Flask - the web application framework used to build the web application
# render_template - restores the HTML template
# request - handles any http requests (or input) from the browser (client) to send back to the app.py (server)
# redirect and url_for - used fore URL direct the user to a web page
# session - manages the user information
# flash - used to display messages to the user
# datetime - handles date and time operations
# sqlite3 - used for interacting with the SQLite applications

# Create a Flask app
app = Flask(__name__) # this creates and instances of the Flask class
app.config ['SECRET_KEY'] = '<>Key<>' # this sets a secret key for session management

# create a connections to the SQLite3 database
def init_db(): # A functions to initialize the database and create the users table if it doesn't exist.
    conn = sqlite3.connect('basic_flask.db') # connects to the database named basic_flask.db
    cursor = conn.cursor() # creates a cursor object to interact with the database using SQL comments
    # cursor.execute() is used to execute SQL commands
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL, age INTEGER NOT NULL) ''')
    conn.commit() # commits the changes to the database
    conn.close() # closes the connection to the database to free up resources/memory

#creates routes for the web applications
@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username'] # gets the username from the form
    password = request.form['password'] # gets the password from the form
    age = request.form['age'] # gets the age from the form
    conn = sqlite3.connect('basic_flask.db') # connects to the database
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, age) VALUES (?, ?, ?)', (username, password, age))
    # inserts the user details into the table
    conn.commit() # commits the change to the database
    conn.close() # closes the connections to the database
    flash('User registered successfully!','success') # displays the success message to the user
    return redirect(url_for('login')) # redirects user to the login page

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username'] # gets username from the form
    password = request.form['password'] # gets password from the form
    conn = sqlite3.connect('basic_flask.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    #? is a placeholder for the values that will be passed in the execute() Function
    # (Username, password) are the values that will be passed in the execute function
    # this is a parameterized query to prevent SQL Injection attacks.
    user = cursor.fetchone() # fetches the first row of results.
    conn.close()
    if user:
        session['user'] = user[1]
        print(user)
        session['age'] = user[3]
        return redirect(url_for('welcome'))
    return 'Login Failed'

@app.route('/hello_world')
def hello_world():
    return 'Hello, World'

@app.route('/welcome')
def welcome():
    if 'user' in session:
        user = session['user']
        age = session['age']
        return render_template('welcome.html', user=user, age=age)
    return redirect(url_for('login'))

     #Calculator page route
    # Calculator page route
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero is undefined"
        else:
            result = "Invalid operator"
        if result.is_integer():
            result = int(result)
    return render_template('calculator.html', result=result)
     #check is the result is a whole number


#Route for logging out
@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    session.pop('age', None)
    return redirect(url_for('login'))

# Main code to run the Flask app and initialise the database
if __name__ == '__main__':
    init_db()  # Calls the init_db() function to initialise
    app.run(port=5000, debug=True)