# Excel-Integrated Todo List Application

A command-line To-Do list application in Python that persists your tasks into an Excel (`.xlsx`) file. This project builds upon basic programming concepts by introducing file handling, persistent data storage, and using third-party libraries.

## Features

- **Add a Task:** Add new tasks, which are automatically time-stamped and set to a "Pending" status.
- **Change Task Status:** Mark tasks as "Done" to keep track of your progress.
- **Delete a Task:** Remove tasks from the Excel sheet permanently.
- **Show All Tasks:** Display all tasks with their current status (e.g., `[Pending]` or `[Done]`) and names.
- **Persistent Data Storage:** Saves all tasks into a file named `todolist.xlsx` so you never lose your data between sessions.

## Dependencies

This project relies on the `openpyxl` library to read and write Excel files.

Install the required library using:
```bash
pip install openpyxl
```

## How to Run

1. Open your terminal or command prompt.
2. Navigate to this project's directory.
3. Run the script:
   ```bash
   python todoxlsx.py
   ```
   
*(Note: If `todolist.xlsx` does not exist, the program will automatically create it for you upon the first run.)*
