#Assignment for list
def main():
    expenses=[2200,2350,2600,2130,2190]
    heros=['spider man','thor','hulk','iron man','captain america']
   
    #expenseInFeb(expenses)
    #expenseOfQuater(expenses)
    #exact2000Spent(expenses)
    #expenseOfJune(expenses)
    #refundOfApril(expenses)
    
    #blackPanter(heros)
    #shiftBlackPanther(heros)
#In Feb, how many dollars you spent extra compare to January?   
def expenseInFeb(expenses):
    print("the extra expense in feb is ",expenses[1]-expenses[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
def expenseOfQuater(expenses):
    quaterlyExpenses=0;
    for i in range(3):
        quaterlyExpenses=quaterlyExpenses+expenses[i]
    print("quaterly expenses are ", quaterlyExpenses)

# 3. Find out if you spent exactly 2000 dollars in any month
def exact2000Spent(expenses):
    for i in range(len(expenses)):
        if(expenses[i]==2000):
            print(f"The expense in {i+1}th month is 2000")
            return;
    print("Expense of no month is equal to 2000")

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
def expenseOfJune(expenses):
    expenses.append(1980)
    print(expenses)

#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
def refundOfApril(expenses):
    expenses[3]=expenses[3]+200;
    print(expenses)

def blackPanter(heros):
    heros.append("Black Panther")
    print(heros)

def shiftBlackPanther(heros):
    heros.pop()
    heros.insert(3,"Black Panther")
    print(heros)
main()