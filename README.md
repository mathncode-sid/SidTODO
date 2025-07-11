# ✅ SidTODO — Minimalist Task Tracker CLI

SidTODO is a simple, terminal-based To-Do application written in Python. It allows you to manage your daily tasks directly from the command line with minimal setup and a clean interface. Whether you're organizing assignments, projects, or errands, SidTODO helps you stay on top of your to-do list in an efficient way.

## ✨ Features

- 📋 Add new tasks with ease  
- ✅ Mark tasks as completed  
- 🗑️ Delete tasks  
- 📂 Organize and view all your tasks in a simple list  
- 💾 Local file-based storage (no internet required)  
- ⚡ Quick and lightweight — runs instantly in your terminal  

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/mathncode-sid/SidTODO.git
cd SidTODO
```

2. **(Optional) Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

> 📌 Note: If `requirements.txt` is missing, ensure Python is installed. This project uses only standard libraries.

## 🚀 Usage

Run the CLI using:

```bash
python main.py
```

Once launched, you’ll be prompted with a simple menu to:
- Add a task
- View current tasks
- Mark tasks as completed
- Delete tasks
- Exit the app

Follow the on-screen instructions to interact with your tasks.

## 📁 File Structure

```
SidTODO/
├── main.py             # Main CLI application
├── tasks.py            # Task management logic (add, remove, complete, list)
├── utils.py            # Helper functions for file I/O
├── tasks.txt           # Local task storage file
└── README.md           # Project documentation
 
```

## 🛠️ Tech Stack

- Python 3.x  
- Standard libraries: `os`, `datetime`, etc.

## 🧠 Concepts Practiced

- File handling (read/write)  
- Modular Python programming  
- Command-line user interfaces  
- Persistent task storage  

## 📌 Use Cases

- Personal productivity tool for students and developers  
- Lightweight alternative to GUI-based to-do apps  
- Practice project for beginners in Python  

## 🧪 Example

```bash
$ python main.py

Welcome to SidTODO 🎯

1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit

Enter your choice: 1
Task name: Finish Python assignment
Task added!
```

## 🧾 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

## 🙌 Acknowledgements

Created with ❤️ by [Sidney Baraka](https://github.com/mathncode-sid)  
Inspired by minimalism and productivity.
