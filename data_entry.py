from datetime import datetime

CATEGORIES = {
    'I':'Income',
    'E':'Expense'
}
date_format = "%d-%m-%y"
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Hey idiot, the value you have put is invalid. Please put it in this format dd-mm-yyy or fuck yourself")
        return get_date(prompt, allow_default)

    



def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <=0:
            raise ValueError("Idiot, enter a non-zero, non-negative value, its a fucking amount it is in numbers...natural numbers idiot.")
        return amount
    except ValueError as e:
        print(e)
        get_amount()

                



def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Ah man! whatever you have typed is wrong doesn't match to the format I said. 'I' for Income or 'E' for Expense. ")
    return get_category()


def get_description():
    return input("Enter a Description: ")




