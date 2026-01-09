# 📚 Personal Book Library

A web application to track your reading list - books you've read, are currently reading, and want to read.

## Features

- ✅ Add new books with title, author, status, rating, and notes
- 📖 View all books in a clean card layout
- 🔍 Search books by title or author
- 🏷️ Filter books by reading status (Reading, Read, Want to Read)
- ✏️ Edit book details
- 🗑️ Delete books
- 💾 SQLite database for data persistence

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Jinja2 templates
- **Database**: SQLite
- **Deployment**: Render

## Screenshots

![Book Library Home Page](screenshot.png)
*Add a screenshot here after deployment*

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/notJ0sh/book-library.git
cd book-library
```

2. Create and activate virtual environment:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python
>>> from app import init_db
>>> init_db()
>>> exit()
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

1. **Add a Book**: Click "Add Book" in the navigation and fill in the form
2. **Search**: Use the search bar to find books by title or author
3. **Filter**: Click status buttons to filter by reading status
4. **Edit**: Click the "Edit" button on any book card to modify details
5. **Delete**: Click the "Delete" button to remove a book (with confirmation)

## Project Structure
```
book-library/
├── app.py              # Main Flask application
├── schema.sql          # Database schema
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # CSS styling
└── templates/
    ├── base.html      # Base template
    ├── index.html     # Home page
    ├── add.html       # Add book form
    └── edit.html      # Edit book form
```

## Database Schema
```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    status TEXT NOT NULL,
    rating INTEGER,
    notes TEXT,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Future Enhancements

- [ ] User authentication
- [ ] Book cover images
- [ ] Export to CSV
- [ ] Reading statistics dashboard
- [ ] Book recommendations
- [ ] Multi-user support

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Joshua** - [GitHub](https://github.com/notJ0sh)

## Acknowledgments

- Built as a learning project to practice Flask, SQLite, and web development
- Inspired by the need for a simple personal reading tracker
