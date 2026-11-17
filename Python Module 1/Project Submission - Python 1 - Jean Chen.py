# Final Project Submission
# Python 1
# Jean Chen


allExpenses = []
info = {}
expenseSum = 0
budgetInput = 0.01


def userInput():
    print("Expense Information")
    expenseAmount = input("Amount: ")
    print("Enter date in format YYYY-MM-DD")
    expenseDate = input("Date: ") 
    expenseType = input("Type: ")
    expenseDesc = input("Short Description: ")
    return expenseAmount,expenseDate,expenseType,expenseDesc


def singleExpenseInput():
    amount,date,type,desc = userInput()
    return {
        "Amount": amount,
        "Date": date,
        "Type": type,
        "Description": desc
    }


def saveExpenses():
    with open("expenses.csv", "w") as fout:    
        fout.write("Amount,Date,Type,Description\n")
        for rExpenses in allExpenses:
             fout.write(f"{rExpenses['Amount']},{rExpenses['Date']},{rExpenses['Type']},{rExpenses['Description']}\n") 
            
    fout.close()


def viewExpenses():
    import csv
    
    fin = open("expenses.csv","r") 
    
    reader = csv.DictReader(fin)
    
    for row in reader:
        if row["Amount"] == '':
            print("Amount: entry missing")
        else:
            print(f"Amount: {row['Amount']}")
        if row["Date"] == '':
            print("Date: entry missing")
        else:
            print(f"Date: {row['Date']}")
        if row["Type"] == '':
            print("Type: entry missing")
        else:
            print(f"Type: {row['Type']}")
        if row["Description"] == '':
            print("Description: entry missing")
        else:
            print(f"Description: {row['Description']}")


def sumOfExpenses():
    expenseSum = 0 
    
    import csv
    
    fin = open("expenses.csv","r") 
    
    reader = csv.DictReader(fin)
    
    for row in reader:
        if row["Amount"] == '':
            print("Amount: entry missing")
        else:
            print(row["Amount"])
            expenseSum += float(row["Amount"])
            print(f"expenseSum = {expenseSum:.2f}")
    
    print(f"Total expenses so far: {expenseSum:.2f}")

    return expenseSum


def getBudget():
    budgetInput = input("Enter this month's budget: ")
    return budgetInput


def trackBudget():
    fBudgetInput = float(budgetInput)
    
    if expenseSum > fBudgetInput:
        print(f"You are over budget by {expenseSum-fBudgetInput}")
    elif expenseSum == fBudgetInput:
        print("You have met your budget.")
    else:
        print(f"You are under budget. You have {fBudgetInput-expenseSum} left to spend.")


ans=True

while ans == True:
    print("\n")
    print("1. Add expense")
    print("2. View expenses")     
    print("3. Track budget")      
    print("4. Save expenses") 
    print("5. Quit")
    print("\n")
    
    answer = input("Please select an option: ")

    print("\n")
    
    if int(answer) == 5:
        saveExpenses()
        print("Your expenses have been saved") 
        print("You will now quit the program.")
        ans=False 
        
    if int(answer) == 1: 
        expense = singleExpenseInput()
        allExpenses.append(expense)
    elif int(answer) == 2:
        viewExpenses()
    elif int(answer) == 3:
        budgetInput = float(getBudget())
        expenseSum = sumOfExpenses()
        trackBudget(budgetInput, expenseSum)
    elif int(answer) == 4:
        saveExpenses()
    else:
        saveExpenses()