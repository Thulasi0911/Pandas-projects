import pandas as pd


# Create employee DataFrame
def create_dataframe():
    data = {
        "Employee_ID": [101, 102, 103, 104, 105, 105],
        "Name": ["Arun", "Bala", "Cathy", "David", "Esha", "Esha"],
        "Department": ["IT", "HR", "IT", "Sales", "HR", "HR"],
        "Salary": [45000, 35000, None, 55000, 30000, 30000],
        "Experience": [2, 4, 3, 6, 1, 1],
        "Joining_Date": [
            "2024-01-10",
            "2022-06-15",
            "2023-03-20",
            "2020-08-12",
            "2025-01-05",
            "2025-01-05"
        ],
        "Performance": [85, 78, 92, 88, 95, 95]
    }

    return pd.DataFrame(data)


# Clean data
def clean_data(df):

    # Convert joining date into datetime
    df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

    # Fill missing salary with average salary
    df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

    # Remove duplicate employees
    df = df.drop_duplicates(subset="Employee_ID")

    return df


# Department-wise analysis
def department_analysis(df):

    result = df.groupby("Department").agg(
        Average_Salary=("Salary", "mean"),
        Average_Performance=("Performance", "mean"),
        Employee_Count=("Employee_ID", "count")
    )

    return result


# Find high-performance and low-salary employees
def find_high_performance_low_salary(df):

    result = df[
        (df["Performance"] >= 90) &
        (df["Salary"] < 40000)
    ]

    return result


# Create salary category
def create_salary_category(df):

    def category(salary):
        if salary < 30000:
            return "Low"
        elif salary <= 50000:
            return "Medium"
        else:
            return "High"

    df["Salary_Category"] = df["Salary"].apply(category)

    return df


# Sort final data
def sort_data(df):

    return df.sort_values(
        by=["Performance", "Salary"],
        ascending=[False, False]
    )


# Main program
def main():

    df = create_dataframe()

    print("===== ORIGINAL DATA =====")
    print(df)

    df = clean_data(df)

    print("\n===== CLEANED DATA =====")
    print(df)

    print("\n===== DEPARTMENT ANALYSIS =====")
    print(department_analysis(df))

    print("\n===== HIGH PERFORMANCE + LOW SALARY =====")
    print(find_high_performance_low_salary(df))

    df = create_salary_category(df)

    print("\n===== SALARY CATEGORY =====")
    print(df[["Employee_ID", "Name", "Salary", "Salary_Category"]])

    df = sort_data(df)

    print("\n===== FINAL SORTED DATA =====")
    print(df)


if _name_ == "_main_":
    main()