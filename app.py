from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS skills
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, skill TEXT)''')
    conn.commit()
    conn.close()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Resume route
@app.route('/resume')
def resume():
    return render_template('resume.html')

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Save to database or send email (not implemented here)
        return redirect(url_for('home'))
    return render_template('contact.html')

# Add skill route
@app.route('/add_skill', methods=['POST'])
def add_skill():
    if request.method == 'POST':
        skill = request.form['skill']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO skills (skill) VALUES (?)", (skill,))
        conn.commit()
        conn.close()
    return redirect(url_for('resume'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)