# tip_calculator.py
# A simple tip calculator to compute tip amount and total bill
# REMEMBER TO REMOVE COMMENTS TO SELF B4 SUBMISSION

#Asks for the bill amount
def bill_amount():
     while True: #Need to put bill > 0 somewhere, dunno where tho, same 4 tip
        try:
            bill = float(input("Enter the bill amount: $"))
            return bill
        except: # i know the except correct
            print("Error")
            bill_amount()
    
#Asks what percentage you want the tip to be of the bill
def tip_percentage():
    while True:
        try:
            tip = float(input("Enter the tip percentage:"))# confident in correct code
            return tip / 100 #Should be correct, print works, check once calculations can work
        except:
            print("Error")
            tip_percentage()

#these two functions cause of issues? ^ Can't call in parameters

# #Calculates the tip amount
def calculate_tip(bill_amount, tip_percentage): #Used right parameters just isn't working??
    calculate_tip = bill * tip #this prolly wrong
    return calculate_tip


#Should all be correct or easily typed correctly
def display_summary(bill_amount, tip_percentage, calculate_tip): # This I'm 99% sure is correct parameters, or need new set of vars(?)
    print("Bill Summary")
#  print(bill_amount) #basic stuff don't wory till later for print but format is print(f"Total is {total:.2f} sjndfksjdf")
#    print(tip_percentage)


def main():
    print("Welcome to the Tip Calculator!")
    bill_amount()
    tip_percentage(tip)
    calculate_tip(bill_amount, tip_percentage)
    # display_summary(bill_amount, tip_percentage, calculate_tip)

#Calls main function
main()