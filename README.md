A web-based Q&A system built with **Python Flask** and **SQLite**, where users can ask questions, submit answers, vote on content, and share knowledge.

---

## 📁 Folder Structure

```
knowledge_platform/
├── app.py                  ← Flask routes & application logic
├── models.py               ← SQLAlchemy database models
├── requirements.txt        ← Python dependencies
│
├── static/
│   ├── css/
│   │   └── style.css       ← All styles (dark academic theme)
│   └── js/
│       └── main.js         ← Client-side interactivity
│
├── templates/
│   ├── base.html           ← Base layout (navbar, footer, flash messages)
│   ├── index.html          ← Homepage (list all questions)
│   ├── ask.html            ← Ask a new question form
│   ├── question.html       ← Question detail + answer form
│   └── search.html         ← Search results page
│
└── instance/
    └── knowledge.db        ← SQLite database (auto-created on first run)
```

---

## 🚀 Setup & Run in VS Code

### Step 1 — Open the project folder
```
File → Open Folder → knowledge_platform/
```

### Step 2 — Create a virtual environment
```bash
# In the VS Code terminal (Ctrl + `)
python -m venv venv
```

### Step 3 — Activate the virtual environment
```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### Step 4 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 5 — Run the application
```bash
python app.py
```

### Step 6 — Open in browser
```
http://127.0.0.1:5000
```

---

## ✨ Features

| Feature               | Description                                          |
|-----------------------|------------------------------------------------------|
| Ask Questions         | Post questions with title, body, and tags            |
| Answer Questions      | Submit answers with author name                      |
| Voting                | Upvote / downvote questions and answers              |
| Accept Answer         | Mark the best answer as accepted (green checkmark)   |
| Tag System            | Add comma-separated tags; filter by tag              |
| Search                | Full-text search across question titles and bodies   |
| Sort Questions        | Sort by newest, most voted, or unanswered            |
| View Counter          | Track how many times each question has been viewed   |
| Delete               | Remove questions or answers                          |
| Flash Messages        | Success / error feedback with auto-dismiss           |

---

## 🗄️ Database Schema

### Question
| Column       | Type     | Description                  |
|--------------|----------|------------------------------|
| id           | Integer  | Primary key                  |
| title        | String   | Question title (max 200)     |
| body         | Text     | Full question text           |
| author_name  | String   | Author (default: Anonymous)  |
| votes        | Integer  | Net vote count               |
| views        | Integer  | View counter                 |
| created_at   | DateTime | Timestamp                    |

### Answer
| Column       | Type     | Description                  |
|--------------|----------|------------------------------|
| id           | Integer  | Primary key                  |
| body         | Text     | Answer text                  |
| author_name  | String   | Author (default: Anonymous)  |
| votes        | Integer  | Net vote count               |
| is_accepted  | Boolean  | Accepted answer flag         |
| created_at   | DateTime | Timestamp                    |
| question_id  | FK       | Links to Question            |

### Tag
| Column | Type   | Description           |
|--------|--------|-----------------------|
| id     | Integer | Primary key          |
| name   | String  | Unique tag name      |

---

## 🛠️ Tech Stack

- **Backend**: Python 3.x + Flask 3.0
- **Database**: SQLite via Flask-SQLAlchemy
- **Frontend**: Jinja2 templates, vanilla HTML/CSS/JS
- **Icons**: Feather Icons (CDN)
- **Fonts**: Lora + DM Sans (Google Fonts)

---

## 📝 Notes

- The database file (`instance/knowledge.db`) is created automatically on first run.
- No authentication is required — the platform is open for anyone to use.
- All data is stored locally in the SQLite database file.
- To reset the database, simply delete `instance/knowledge.db` and restart the app.
