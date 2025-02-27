# tip_calculator.py
# A simple tip calculator to compute tip amount and total bill

#Asks for and validates total bill
def bill_amount():
    while True:
        try:
            bill = float(input("Enter the bill amount: $"))
            if bill > 0:
                return bill
            else:
                print("Incorrect input, use a positive number.")
                bill_amount()
        except:
            print("Error, try again. Make sure you are using a number.")

#Asks for and validates tip percentage
def tip_percentage(bill):
    while True:
        try:
            tip = float(input("Enter the tip percentage: %"))
            if tip > 0:
                return tip / 100 * bill
            else:
                print("Incorrect input, try again")
                tip_percentage(bill)
        except:
            print("Error, try that again. Make sure you are using just a number.")

#Calculates the tip from percentage given
def calculate_tip(bill, tip): 
    tip_calculate = bill * tip
    return tip_calculate

#Calculates the total, bill + tip
def calculate_total(bill, tip):
    total_calculation = bill + tip
    return total_calculation

#Displays the summary of the total
def display_summary(bill, tip, total_calculation): # Issues
    print("---Tip Calculator Summary---")
    print("")
    print(f"Bill Amount: ${bill:.2f}")
    print(f"Tip Amount: ${tip:.2f}")
    print(f"Total Bill: ${total_calculation:.2f}")
    print("")

# Tip Calculator, displays header and puts together functions to create one 
def main():
    print("")
    print("---Welcome to the Tip Calculator!---")
    print("")
    bill = bill_amount()
    tip = tip_percentage(bill)
    print("")
    total_calculation = calculate_total(bill, tip)
    calculate_tip(bill, tip)
    display_summary(bill, tip, total_calculation)

#Main function called to run program
main()
