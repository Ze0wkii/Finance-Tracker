import pandas as pd
from datetime import datetime
import csv
from data_entry import get_date, get_amount, get_category, get_description
from time import sleep


dashboard = {
    1:"Add a new Transaction",
    2:"View Transaction in a specific date range",
    3:"Exit"
}
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
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)

        filtered_df = df.loc[mask]
        if filtered_df.empty:
            print("No transacations found in the given data range.")
        else:
            print(f"Transacations from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            sleep(1)

            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))
            sleep(1)

            total_income = filtered_df[filtered_df['category']== 'Income']['amount'].sum()
            total_expense = filtered_df[filtered_df['category']== 'Expense']['amount'].sum()
            print("\nSummary: ")
            sleep(2)
            print(f"Total Income:{total_income:.2f}")
            sleep(1)
            print(f"Total Expense:{total_expense:2f}")
            sleep(1)
            print(f"Total Savings:{total_income - total_expense:.2f}")

        
    # @classmethod
    # def transactions_get(cls):
    #     start_date = "Please enter the start-date (dd-mm-yyy): "
    #     end_date = "Please enter the end-date (dd-mm-yyy): "
    #     CSV.get_transactions(start_date, end_date)




def add():
    CSV.initialise()
    date = get_date("Enter the date (dd-mm-yy) or press enter for today's date: ", True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date,amount,category,description)


def main():
    exit_program=0
    while exit_program==False:
        print("--Welcome to your Personal Finance Tracker--")

        for keys, values in dashboard.items():
            print(f"{keys}:{values}")
        choice = int(input("Enter your Choice: "))

        try:
            if choice in dashboard and choice==1:
                add()

            elif choice in dashboard and choice==2:
                start_date = input("Please enter the start-date (dd-mm-yyy): ")
                end_date = input("Please enter the end-date (dd-mm-yyy): ")
                CSV.get_transactions(start_date, end_date)

            elif choice in dashboard and choice==3:
                exit_program=True
                print("Exiting the program")
                exit()
            else:
                raise ValueError("The Value you have entered is incorrect (type either of them 1, 2 or 3 fordesired function)")
        
        except ValueError as e:
            print(e)
        
main()
        


        
    

