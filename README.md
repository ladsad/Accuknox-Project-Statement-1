# AccuKnox Project Assessment - Statement 1

This repository contains the solution for **Project Statement 1** of the AccuKnox assessment. It includes Python scripts for API data retrieval, data visualization, and database operations.

## Project Structure

*   **`task1_books.py`**: Fetches book data from the OpenLibrary API and stores it in a SQLite database (`books.db`).
*   **`task2_students.py`**: Retrieves mock student test scores, calculates statistics, and generates a visualization (`student_scores_chart.png`).
*   **`task3_csv_import.py`**: Imports user data from a CSV file (`users.csv`) into a SQLite database (`users.db`).
*   **`requirements.txt`**: List of dependencies required to run the project.

## Prerequisites

*   Python 3.x
*   pip (Python package installer)

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/ladsad/Accuknox-Project-Statement-1.git
    cd Accuknox-Project-Statement-1
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Task 1: API Data Retrieval (Books)
Fetch book data and store it in the database:
```bash
python task1_books.py
```
*Output*: Creates/Updates `books.db` and displays retrieved records in the console.

### Task 2: Data Visualization (Student Scores)
Fetch student scores and generate a bar chart:
```bash
python task2_students.py
```
*Output*: Displays average score and counts in the console. Saves a bar chart as `student_scores_chart.png`.

### Task 3: CSV to Database Import
Import user records from CSV to SQLite:
```bash
python task3_csv_import.py
```
*Output*: Reads `users.csv`, populates `users.db`, and verifies the data entry.

## Output Files
The scripts will generate the following artifacts in your directory:
*   `books.db` (SQLite Database)
*   `users.db` (SQLite Database)
*   `student_scores_chart.png` (Image)
