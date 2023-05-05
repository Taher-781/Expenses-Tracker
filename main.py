import sqlite3
import datetime

conn = sqlite3.connect("expenses.db");
curr = conn.cursor()


while True:
    print("Enter an Option:")
    print("1. Enter the Expense")
    print("2. View Summary")
    choice = int(input())

    if choice==1 :
        Date=input("Enter Date of expense (YYYY-MM-DD):-")
        Description=input("Enter item description:-")
        curr.execute("Select DISTINCT Category from expenses")
        categories=curr.fetchall()
        print("Select Cateogories by number:")
        for idx, Category in enumerate(categories):
            print(f"{idx+1}.{Category[0]}")
        print(f"{len(categories)+1}.Create a New Category:-")
        category_choice=int(input())
        
        if category_choice == len(categories)+1 :
            Category=input("Enter new Category:-")
        else:
            Category=categories[category_choice-1][0]
        
        price = input("Enter the price of expense:-")

        curr.execute("INSERT into expenses(Date,Description,Category,Price) VALUES(?,?,?,?)",(Date,Description,Category,price))

        conn.commit()
        


    
    elif choice==2 :
        print("Select an option:")
        print("1. View all expenses")
        print("2. View monthly expenses by Category")

        view_choice=int(input())
        if view_choice==1:
            curr.execute("Select * from expenses")
            expenses= curr.fetchall()
            for expense in expenses:
                print(expense)
        elif view_choice==2:
            month=input("Enter the month(MM):-")
            year=input("Enter the year(YYYY):-")
            curr.execute("""Select Category,Sum(Price) from expenses WHERE strftime('%m',Date) =? AND strftime('%Y',Date) =? GROUP BY Category""",(month,year))

            expenses= curr.fetchall()
            for expense in expenses:
                print(f"Category:{expense[0]},Total: {expense[1]}")
    
    else :
        exit()

    repeat=input("Would you like to repeat (y/n):-\n")
    if repeat.lower()!="y":
        break

    conn.close()    