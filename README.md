# 🚀 DevLog — Developer Daily Standup CLI + API

DevLog is a simple yet powerful tool that helps developers track their daily work.
It provides a **CLI interface** to log daily standups and a **FastAPI backend** to store and retrieve them.

---

## 📌 Features

* 📝 Add daily standup logs (Yesterday, Today, Blockers)
* 📋 View all logs in a clean table format
* 📅 View last 7 days logs
* 🎨 Beautiful CLI output using Rich
* ⚡ FastAPI backend with REST APIs
* 🗄️ SQLite database (no setup required)

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **CLI:** Click
* **UI:** Rich

---

## 📂 Project Structure

```
devlog/
├── app/
│   ├── main.py        # FastAPI entry point
│   ├── routes.py      # API routes
│   ├── models.py      # Database models
│   ├── database.py    # DB connection
├── cli.py             # CLI interface
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-url>
cd devlog
```

---

### 2️⃣ Create virtual environment

```
python -m venv myenv
myenv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Start FastAPI server

```
uvicorn app.main:app --reload
```

👉 Server runs at:

```
http://127.0.0.1:8000
```

👉 API Docs:

```
http://127.0.0.1:8000/docs
```

---

## 💻 CLI Usage

Open a new terminal (keep server running):

### ➤ Add log

```
python cli.py log
```

---

### ➤ View all logs

```
python cli.py list
```

---

### ➤ View weekly logs

```
python cli.py week
```

---

## 📊 Example Output

```
📘 Dev Logs
┏━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ ID┃ Yesterday    ┃ Today        ┃ Blockers     ┃
┣━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━┫
┃ 1 ┃ Fixed bug    ┃ Build API    ┃ None         ┃
┗━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┛
```

---

## 🌐 Deployment

This project can be deployed using platforms like:

* Render
* Railway

Update `API_URL` in `cli.py` after deployment.

---

## 🔮 Future Improvements

* ✏️ Update & Delete logs (CRUD)
* 🔐 Authentication system
* 📈 Weekly summary analytics
* 🌍 Web frontend (React / Streamlit)
* 🐘 PostgreSQL database

---

## 👨‍💻 Author

Developed as a learning project to understand:

* APIs
* Databases
* CLI tools
* Full-stack flow

---

## ⭐ Acknowledgements

This project is built for practice and learning real-world backend development.

---

## 📌 License

This project is open-source and free to use.
