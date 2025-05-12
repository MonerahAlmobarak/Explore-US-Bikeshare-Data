# Bikeshare Data Exploration

This project analyzes bikeshare trip data for three major U.S. cities—Chicago, New York City, and Washington—using Python. You will compute descriptive statistics and build an interactive terminal script to let users explore the data by city, month, and day.

---

## 📋 Project Overview

- **Objective**: Load and explore bikeshare CSV data to answer questions about trip duration, popular times, popular stations, user demographics, and more.
- **Cities Covered**:  
  - Chicago (`chicago.csv`)  
  - New York City (`new_york_city.csv`)  
  - Washington (`washington.csv`)  
- **Time Frame**: Data spans various months; users can filter by month (January to June) and day of week.

---

## 🗂 Project Files

- `bikeshare.py`  
  The main script. Prompts the user for filters (city, month, day) and displays statistics.
- `README.md`  
  Project documentation (this file).
- `*.csv`  
  Raw data files for each city, provided in the workspace or Downloads folder.
- `requirements.txt`  
  Lists Python dependencies.

---

## ⚙️ Dependencies

- Python 3.7+  
- pandas  
- NumPy  

---

## 🚀 How to Run

### Option 1: Udacity Workspace (Recommended)

1. Open the project workspace in your browser.
2. Locate `code.py` and open a terminal.
3. Run:

4. Follow the prompts to choose a city, month, and day filter, then view your statistics.

### Option 2: Local Machine

1. Clone or download this repository.
2. Ensure you have Python 3, pandas, and NumPy installed (see Dependencies).
3. Place the CSV files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) in the project root.
4. From your terminal, run:

   ```bash
   python code.py
   ```
5. Answer the interactive prompts to explore the data.

---

## 🔍 Features

When you run the script, it will calculate and display:

* **Time Statistics**: Most common month, day, and start hour.
* **Station Statistics**: Most popular start station, end station, and trip combination.
* **Trip Duration**: Total and average trip durations.
* **User Info**: Counts of user types, gender distribution, and birth year stats (where available).

---

## 📥 Download Data

If you’re working locally, download the CSV files from the Udacity Resources tab (folder icon) or from the course repository:

* `chicago.csv`
* `new_york_city.csv`
* `washington.csv`

---

## 👤 Author

**Monerah Almobarak**
