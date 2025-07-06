# 📝 Python CLI Todo App

A simple command-line todo application built with Python. Tasks are stored locally in a JSON file.

## 🚀 Features

- Add tasks
- List tasks
- Mark tasks as done
- Delete tasks
- Data stored in `todo.json`

## 📂 Project Structure

python-todo/
├── todo.py # Main CLI script
├── storage.py # JSON file read/write
├── todo.json # Task storage (ignored in Git)
├── venv/ # Virtual environment (ignored)
├── LICENSE # MIT License
└── README.md # Project description

rust
Copy
Edit

## 💻 Usage

Activate your virtual environment if you're using one:

```bash
source venv/bin/activate
Then run the script:

bash
Copy
Edit
# Add a task
./todo.py --add "Study Python"

# List tasks
./todo.py --list

# Mark a task as done
./todo.py --done 1

# Delete a task
./todo.py --delete 1
⚙️ Requirements
This app uses only Python's standard libraries.
No external packages are required.

To set up a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
📄 License
This project is licensed under the MIT License.
See the LICENSE file for more information.

yaml
Copy
Edit

---

