import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class COVID19Data:
    def __init__(self):
        self.data = None
        self.fig = None

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            if self.data.empty:
                print("The CSV file is empty.")
                self.data = None
                return
            if "date" in self.data.columns:
                self.data["date"] = pd.to_datetime(self.data["date"])
            print("COVID-19 dataset loaded successfully!")
        except FileNotFoundError:
            print("CSV file not found. Please check the file path.")
        except pd.errors.EmptyDataError:
            print("The CSV file is empty.")
        except Exception as e:
            print("Error loading dataset:", e)

    def check_data(self):
        if self.data is None:
            print("\nPlease load a dataset first.")
            return False
        return True

    def explore_data(self):
        if not self.check_data():
            return

        print("\n--- Explore COVID-19 Data ---")
        print("1. Display first 5 rows")
        print("2. Display last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic information")
        print("6. Display number of rows and columns")

        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    print(self.data.head())
                case 2:
                    print(self.data.tail())
                case 3:
                    print(self.data.columns.to_list())
                case 4:
                    print(self.data.dtypes)
                case 5:
                    self.data.info()
                case 6:
                    print("Rows:", self.data.shape[0])
                    print("Columns:", self.data.shape[1])
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number.")
    def clean_data(self):
        if not self.check_data():
            return
        print("\n--- Handle Missing Data ---")
        print("1. Display rows with missing values")
        print("2. Fill numeric missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")

        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    missing = self.data[self.data.isna().any(axis=1)]
                    if missing.empty:
                        print("No rows with missing values were found.")
                    else:
                        print(missing.head(50))
                        if len(missing) > 50:
                            print("Showing first 50 matching rows.")
                case 2:
                    numeric_cols = self.data.select_dtypes(include=np.number).columns
                    self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].mean())
                    print("Numeric missing values filled with column means.")
                case 3:
                    before = len(self.data)
                    self.data.dropna(inplace=True)
                    print("Rows removed:", before - len(self.data))
                case 4:
                    value = input("Enter replacement value: ")
                    self.data.fillna(value, inplace=True)
                    print("Missing values replaced.")
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number.")
    def mathematical_operations(self):
        if not self.check_data():
            return
        numeric_cols = self.data.select_dtypes(include=np.number).columns.to_list()
        if not numeric_cols:
            print("No numeric columns available.")
            return
        print("Numeric columns:", numeric_cols)
        column = input("Enter column name: ").strip()
        if column not in numeric_cols:
            print("Invalid numeric column!")
            return
        try:
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            number = float(input("Enter a number: "))
            choice = int(input("Enter your choice: "))
            values = self.data[column]
            match choice:
                case 1:
                    answer = values + number
                case 2:
                    answer = values - number
                case 3:
                    answer = values * number
                case 4:
                    if number == 0:
                        print("Cannot divide by zero.")
                        return
                    answer = values / number
                case _:
                    print("Invalid choice!")
                    return
            print(pd.DataFrame({"Original": values, "Answer": answer}))
        except ValueError:
            print("Please enter a valid number.")
    def combine_data(self):
        if not self.check_data():
            return
        print("\n--- Combine DataFrames ---")
        print("1. Concatenate datasets")
        print("2. Merge datasets using a common column")
        try:
            choice = int(input("Enter your choice: "))
            file_path = input("Enter the second CSV file path: ").strip()
            second_data = pd.read_csv(file_path)
            match choice:
                case 1:
                    result = pd.concat([self.data, second_data], ignore_index=True)
                case 2:
                    common_cols = list(set(self.data.columns) & set(second_data.columns))
                    print("Common columns:", common_cols)
                    key = input("Enter common column name: ").strip()
                    if key not in self.data.columns or key not in second_data.columns:
                        print("Column not found in both datasets.")
                        return
                    result = pd.merge(self.data, second_data, on=key, how="inner")
                case _:
                    print("Invalid choice!")
                    return
            print(result.head(20))
            print("Combined dataset shape:", result.shape)
            save = input("Replace current dataset? (y/n): ").lower()
            if save == "y":
                self.data = result
                print("Current dataset updated.")
        except FileNotFoundError:
            print("Second CSV file not found.")
        except Exception as e:
            print("Error combining datasets:", e)
    def split_data(self):
        if not self.check_data():
            return
        print("\n--- Split Data ---")
        print("Available columns:", list(self.data.columns))
        column = input("Enter column name to split by: ").strip()
        if column not in self.data.columns:
            print("Invalid column name!")
            return
        value = input("Enter value to separate: ").strip()
        first = self.data[self.data[column].astype(str) == value]
        second = self.data[self.data[column].astype(str) != value]
        print("\nRows matching the value:")
        print(first.head(20))
        print("Number of matching rows:", len(first))
        print("\nRemaining rows:")
        print(second.head(20))
        print("Number of remaining rows:", len(second))
        save = input("Save both groups as CSV files? (y/n): ").lower()
        if save == "y":
            first.to_csv("covid_group_1.csv", index=False)
            second.to_csv("covid_group_2.csv", index=False)
            print("Both groups saved successfully.")
    def search_sort_filter(self):
        if not self.check_data():
            return
        print("\n--- Search, Sort and Filter ---")
        print("1. Search for a value")
        print("2. Sort data")
        print("3. Filter numeric data")
        print("4. Filter by country")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    column = input("Enter column name: ").strip()
                    if column not in self.data.columns:
                        print("Invalid column!")
                        return
                    value = input("Enter value to search: ").strip()
                    result = self.data[self.data[column].astype(str).str.contains(value, case=False, na=False)]
                    print(result.head(50))
                    print("Matching rows:", len(result))
                case 2:
                    column = input("Enter column name to sort: ").strip()
                    if column not in self.data.columns:
                        print("Invalid column!")
                        return
                    ascending = input("Ascending order? (y/n): ").lower() == "y"
                    print(self.data.sort_values(by=column, ascending=ascending).head(50))
                case 3:
                    numeric_cols = self.data.select_dtypes(include=np.number).columns.to_list()
                    print("Numeric columns:", numeric_cols)
                    column = input("Enter numeric column: ").strip()
                    if column not in numeric_cols:
                        print("Invalid numeric column!")
                        return
                    value = float(input("Enter minimum value: "))
                    print(self.data[self.data[column] >= value].head(50))
                case 4:
                    if "location" not in self.data.columns:
                        print("The location column was not found.")
                        return
                    country = input("Enter country name: ").strip()
                    result = self.data[
                        self.data["location"].astype(str).str.lower()
                        == country.lower()
                    ]
                    print(result.head(50))
                    print("Matching rows:", len(result))
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number.")
    def advanced_operations(self):
        if not self.check_data():
            return
        print("\n--- Advanced Operations ---")
        print("1. Create a pivot table")
        print("2. Reset DataFrame index")
        print("3. Add group averages")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    print("Available columns:", list(self.data.columns))
                    index_col = input("Enter country/group column: ").strip()
                    value_col = input("Enter numeric values column: ").strip()
                    if index_col not in self.data.columns:
                        print("Invalid group column!")
                        return
                    if value_col not in self.data.select_dtypes(include=np.number).columns:
                        print("Invalid numeric column!")
                        return
                    print(
                        pd.pivot_table(self.data,index=index_col, values=value_col, aggfunc=["sum", "mean", "count"]))
                case 2:
                    print(self.data.reset_index().head(50))
                case 3:
                    group_col = input("Enter group column (e.g. location): ").strip()
                    value_col = input("Enter numeric column (e.g. new_cases): ").strip()
                    if group_col not in self.data.columns:
                        print("Invalid group column!")
                        return
                    if value_col not in self.data.select_dtypes(
                        include=np.number
                    ).columns:
                        print("Invalid numeric column!")
                        return
                    result = self.data.copy()
                    result["Group_Average"] = result.groupby(group_col)[value_col].transform("mean")
                    print(result[[group_col, value_col, "Group_Average"]].head(50))
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number.")
    def statistical(self):
        if not self.check_data():
            return
        numeric = self.data.select_dtypes(include=np.number)
        if numeric.empty:
            print("No numeric data available.")
            return
        print("\n--- Statistical Analysis ---")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard deviation")
        print("5. Variance")
        print("6. Minimum and maximum")
        print("7. Percentiles")
        print("8. Correlation")
        print("9. Descriptive statistics")
        print("10. Country-wise analysis")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    print(numeric.sum())
                case 2:
                    print(numeric.mean())
                case 3:
                    print(numeric.median())
                case 4:
                    print(numeric.std())
                case 5:
                    print(numeric.var())
                case 6:
                    print("Minimum:\n", numeric.min())
                    print("Maximum:\n", numeric.max())
                case 7:
                    print(numeric.quantile([0.25, 0.50, 0.75]))
                case 8:
                    print(numeric.corr())
                case 9:
                    print(numeric.describe())
                case 10:
                    if "location" not in self.data.columns:
                        print("The location column was not found.")
                        return
                    metric = input("Enter numeric column (e.g. total_cases): ").strip()
                    if metric not in numeric.columns:
                        print("Invalid numeric column!")
                        return
                    print(self.data.groupby("location")[metric].agg(["sum", "mean", "min", "max", "count"]).sort_values("sum", ascending=False).head(20))
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number.")
    def visualize_data(self):
        if not self.check_data():
            return

        numeric_cols = self.data.select_dtypes(include=np.number).columns.to_list()

        print("\n--- Data Visualization ---")
        print("1. Line Plot")
        print("2. Bar Plot")
        print("3. Scatter Plot")
        print("4. Histogram")
        print("5. Heatmap")
        print("6. Box Plot")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                country = input("Enter country name: ")
                column = input("Enter metric (e.g. new_cases): ")

                if column not in numeric_cols:
                    print("Invalid column!")
                    return

                data = self.data[self.data["location"] == country]
                data = data.sort_values("date")

                self.fig, ax = plt.subplots()
                ax.plot(data["date"], data[column])
                ax.set_title("COVID-19 Cases Over Time")
                ax.set_xlabel("Date")
                ax.set_ylabel(column)

            elif choice == 2:
                column = input("Enter metric (e.g. total_cases): ")

                if column not in numeric_cols:
                    print("Invalid column!")
                    return

                data = self.data.groupby("location")[column].max()
                data = data.sort_values(ascending=False).head(10)

                self.fig, ax = plt.subplots()
                data.plot(kind="bar", ax=ax)
                ax.set_title("Top 10 Countries")
                ax.set_ylabel(column)

            elif choice == 3:
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                if x not in numeric_cols or y not in numeric_cols:
                    print("Invalid numeric column!")
                    return

                self.fig, ax = plt.subplots()
                ax.scatter(self.data[x], self.data[y])
                ax.set_xlabel(x)
                ax.set_ylabel(y)
                ax.set_title("Scatter Plot")

            elif choice == 4:
                column = input("Enter column for histogram: ")

                if column not in numeric_cols:
                    print("Invalid column!")
                    return

                self.fig, ax = plt.subplots()
                ax.hist(self.data[column].dropna(), bins=10)
                ax.set_title("Histogram")
                ax.set_xlabel(column)
                ax.set_ylabel("Frequency")

            elif choice == 5:
                self.fig, ax = plt.subplots()
                sns.heatmap(self.data[numeric_cols].corr(), ax=ax,annot=True)
                ax.set_title("COVID-19 Correlation Heatmap")

            elif choice == 6:
                column = input("Enter numeric column: ")

                if column not in numeric_cols:
                    print("Invalid column!")
                    return

                self.fig, ax = plt.subplots()
                sns.boxplot(x=self.data[column], ax=ax)
                ax.set_title("Box Plot")

            else:
                print("Invalid choice!")
                return

            plt.tight_layout()
            plt.show()

        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print("Error:", e)


    def save_visualization(self):
        if self.fig is None:
            print("Please generate a visualization first.")
            return

        file_name = input("Enter file name: ")

        if not file_name:
            print("File name cannot be empty.")
            return

        if not file_name.endswith((".png", ".jpg")):
            file_name = file_name + ".png"

        try:
            self.fig.savefig(file_name)
            print("Visualization saved successfully!")

        except Exception as e:
            print("Error saving visualization:", e)
    def main(self):
        while True:
            print("\n========== COVID-19 DATA ANALYSIS AND VISUALIZATION ==========")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Generate Statistical Analysis")
            print("6. General Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")
            print("=====================================================================")

            try:
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:
                        file_path = input("Enter CSV path or URL of COVID-19 dataset: ").strip()
                        self.load_data(file_path)
                    case 2:
                        self.explore_data()
                    case 3:
                        print("\n1. Mathematical Operations")
                        print("2. Combine DataFrames")
                        print("3. Split Data")
                        print("4. Search, Sort and Filter")
                        print("5. Advanced Operations")
                        choice1 = int(input("Enter your choice: "))
                        match choice1:
                            case 1:
                                self.mathematical_operations()
                            case 2:
                                self.combine_data()
                            case 3:
                                self.split_data()
                            case 4:
                                self.search_sort_filter()
                            case 5:
                                self.advanced_operations()
                            case _:
                                print("Invalid choice!")
                    case 4:
                        self.clean_data()
                    case 5:
                        self.statistical()
                    case 6:
                        self.visualize_data()
                    case 7:
                        self.save_visualization()
                    case 8:
                        print("Exiting the program. Goodbye!")
                        break
                    case _:
                        print("Invalid choice!")
            except ValueError:
                print("Please enter a valid number.")


if __name__ == "__main__":
    analyzer = COVID19Data()
    analyzer.main()
