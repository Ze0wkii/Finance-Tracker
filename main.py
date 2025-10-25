import pandas as pd
from datetime import datetime
import csv
from data_entry import get_date, get_amount, get_category, get_description

class CSV:
    CSV_file = "finance_data.csv"
    COLUMNS=["date", "amount", "category", "description"]
    FORMAT='%d-%m-%y'
    @classmethod
    def initialise(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_file, index=False)
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(cls.CSV_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Data Aded successfully.")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_file)
        df['date'] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, format=CSV.FORMAT)
        end_date = datetime.strptime(end_date, format=CSV.FORMAT)
        mask = (df["date"]>=start_date & df['date']<=end_date)
        filtered_df = df.loc[mask]
        if filtered_df.empty:
            print("No transacations found in the given data range.")
        else:
            print(f"Transacations from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")

            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

            total_income = filtered_df[filtered_df['category']== 'Income']['amount'].sum()
            total_expense = filtered_df[filtered_df['category']== 'Expense']['amount'].sum()
            print("\nSummary: ")
            print(f"Total Income:{total_income:.2f}")
            print(f"Total Expense:{total_expense:2f}")
            print(f"Total Savings:{total_income - total_expense}):.2f")

        




def add():
    CSV.initialise()
    date = get_date("Enter the date (dd-mm-yy) or press enter for today's date: ", True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date,amount,category,description)

add()