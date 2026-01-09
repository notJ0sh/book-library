import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g
from datetime import datetime

app = Flask(__name__)
DATABASE = 'books.db'

# Database helper functions
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Routes
@app.route('/')
def index():
    db = get_db()
    filter_status = request.args.get('status')
    search_query = request.args.get('search')

    if filter_status:
        db.execute(
            'SELECT * FROM books WHERE status = ? ORDER BY date_added DESC',
            (filter_status,)
        ).fetchall()
    elif search_query:
        books = db.execute(
            'SELECT * FROM books WHERE title LIKE ? OR author LIKE ? ORDER BY date_added DESC',
            (f'%{search_query}%', f'%{search_query}%')
        ).fetchall()
    else:
        books = db.execute('SELECT * FROM books ORDER BY date_added DESC').fetchall()
    
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        status = request.form['status']
        rating = request.form['rating']
        notes = request.form['notes']

        db = get_db()
        db.execute(
            'INSERT INTO books (title, author, status, rating, notes) VALUES (?, ?, ?, ?, ?)',
            (title, author, status, rating, notes)
        )
        db.commit()
        return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    db = get_db()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        status = request.form['status']
        rating = request.form['rating']
        notes = request.form['notes']

        db.execute(
            'UPDATE books SET title = ?, author = ?, status = ?, rating = ?, notes = ? WHERE id = ?',
            (title, author, status, rating, notes, id)
        )
        db.commit()
        return redirect(url_for('index'))
    
    book = db.execute('SELECT * FROM books WHERE id = ?', (id,)).fetchone()
    return render_template('edit.html', book=book)

@app.route('/delete/<int:id>')
def delete(id):
    db = get_db()
    db.execute('DELETE FROM books WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    import os
    print(f"Current working directory: {os.getcwd()}")
    print(f"DATABASE path: {DATABASE}")
    print(f"Database exists: {os.path.exists(DATABASE)}")
    
    if not os.path.exists(DATABASE):
        print("Creating database...")
        init_db()
        print(f"Database created: {os.path.exists(DATABASE)}")
    else:
        print("Database already exists")
    
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))