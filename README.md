# 🍕 CS50P – Pizza.py

This project is my solution to the **“Pizza Py”** problem from Harvard’s **CS50P (Introduction to Programming with Python)** course.  
It demonstrates reading CSV files, validating command-line arguments, and formatting data beautifully using the **Tabulate** library.

---

## 🧠 Overview

The program takes a CSV file containing a pizza menu and prints it in a clean, formatted table using ASCII grid borders.  
It also validates the command-line arguments to ensure the user provides a valid `.csv` file.

---

## ⚙️ How It Works

1. **Checks the number of command-line arguments**  
   - If no argument or more than one is provided, the program exits with an error message.

2. **Validates the file extension**  
   - Ensures the provided file ends with `.csv`.

3. **Opens and reads the CSV file**  
   - Uses Python’s built-in `csv.DictReader` to read data into dictionaries.

4. **Displays the data as a formatted table**  
   - Uses the `tabulate` library to print the table in a user-friendly grid layout.

5. **Handles file errors gracefully**  
   - If the file doesn’t exist, the program exits with a clear error message.

---

## 🧩 Example

**Input (command line):**
```bash
python pizza.py menu.csv
Contents of menu.csv:
Pizza,Small,Large
Cheese,13.50,18.95
Pepperoni,14.50,19.95
Hawaiian,15.25,21.50

**🟦 Output (in terminal):**

+------------+--------+--------+
| Pizza      | Small  | Large  |
+============+========+========+
| Cheese     | 13.50  | 18.95  |
+------------+--------+--------+
| Pepperoni  | 14.50  | 19.95  |
+------------+--------+--------+
| Hawaiian   | 15.25  | 21.50  |
+------------+--------+--------+

---

## 🧰 Technologies Used

Python 3

csv (built-in module)

tabulate (external library for table formatting)

sys (for command-line arguments)

---

💡 Key Concepts

File I/O (reading .csv files)

Command-line argument validation

Exception handling (FileNotFoundError)

Data presentation and formatting

---
⚠️ Error Handling Examples

| Situation                    | Output Message                    |
| ---------------------------- | --------------------------------- |
| No argument provided         | `Too few command-line arguments`  |
| More than one argument       | `Too many command-line arguments` |
| File doesn’t end with `.csv` | `Not a CSV file`                  |
| File not found               | `File does not exist`             |


🧑‍💻 Author

Mohammad Reza Abdollah
📧 mohammadenor@gmail.com
