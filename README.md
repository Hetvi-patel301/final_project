# COVID-19 Data Analysis & Visualization Program

### Introduction

The **COVID-19 Data Analysis & Visualization Program** is a menu-driven Python application developed using Pandas, NumPy, Matplotlib, and Seaborn. It helps users load, explore, clean, manipulate, analyze, and visualize COVID-19 data from CSV files.

This project uses Object-Oriented Programming (OOP) to organize different functionalities into a single `COVID19Data` class. It also uses exception handling to manage common file and input errors.

### Features

#### 1. Load Dataset
- Load COVID-19 datasets from CSV files.
- Handle missing files and empty CSV files.
- Display dataset loading status.

#### 2. Explore Data
- Display the first and last five rows.
- Display column names and data types.
- Display basic dataset information.
- Show the number of rows and columns.

#### 3. Handle Missing Data
- Display rows containing missing values.
- Fill missing numeric values using the column mean.
- Remove rows containing missing values.
- Replace missing values with a specific value.

#### 4. Mathematical Operations
Perform mathematical operations on numeric columns:
- Addition
- Subtraction
- Multiplication
- Division

Includes numeric column validation and division-by-zero handling.

#### 5. Combine DataFrames
- Concatenate two datasets.
- Merge datasets using a common column.
- Optionally update the current dataset.

#### 6. Split Data
- Split rows based on a selected column and value.
- Display matching and remaining rows.
- Save both groups as separate CSV files.

#### 7. Search, Sort and Filter
- Search for specific values.
- Sort data in ascending or descending order.
- Filter numeric data using a minimum value.
- Filter data by country.

#### 8. Advanced Operations
- Create pivot tables using sum, mean, and count.
- Reset the DataFrame index.
- Calculate group-wise averages.

#### 9. Statistical Analysis
- Calculate sum, mean, and median.
- Calculate standard deviation and variance.
- Find minimum and maximum values.
- Calculate percentiles.
- Generate correlation matrices and descriptive statistics.
- Perform country-wise statistical analysis.

#### 10. Data Visualization
Create visualizations using Matplotlib and Seaborn:
1. Line Plot
2. Bar Plot
3. Scatter Plot
4. Histogram
5. Correlation Heatmap
6. Box Plot

#### 11. Save Visualization
- Save generated graphs as PNG, JPG, or PDF files.
- Export visualizations for future reference.

### Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Creating graphs and plots |
| Seaborn | Statistical data visualization |
| CSV | Dataset input and output |
| OOP | Organizing code using classes and methods |

### Requirements

- Python 3.10 or above
- Pandas
- NumPy
- Matplotlib
- Seaborn

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

### How to Run

**Step 1: Open the project directory**

Open your project folder in VS Code.

**Step 2: Run the Python file**

```bash
python COVID19_Data_Analysis.py
```

Replace `COVID19_Data_Analysis.py` with your actual Python filename.

**Step 3: Load the dataset**

Select option `1` from the main menu and enter the path of your COVID-19 CSV file.

**Step 4: Analyze your data**

Choose the required menu options to explore, clean, manipulate, analyze, and visualize the dataset.

### Main Menu

```text
========== COVID-19 DATA ANALYSIS AND VISUALIZATION ==========

1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Statistical Analysis
6. General Data Visualization
7. Save Visualization
8. Exit
```

### Project Structure

```text
Project_10/
│
├── COVID19_Data_Analysis.py
├── covid_data.csv
└── README.md
```

### Created by:

**Hetvi Patel**
