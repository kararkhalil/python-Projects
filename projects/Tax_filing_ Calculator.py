
 #Name:  Karar Khalil
 #Date:  2/23/2025

# This program calculates the tax based on the filing status and income of the user.
# The program first asks the user to enter their filing status and income, then calculates the tax based on the given tax brackets.
# The tax brackets are hardcoded in the program, and the program uses if-elif statements to determine the tax based on the user's input.
# The program also includes input validation to ensure that the user enters a valid filing status and income.

#Title screen
TITLE = "Tax Calculator V1.0"
print("*-*-*-*-*-*-*- Welcome to", TITLE, "*-*-*-*-*-*-*-" )
#asking for input and validating it, exiting program before it starts if invalid
status = int(input('please enter your filing status, (0) for Single, (1) for Married filing joint, \
(2) for Married filing seprate, (3) for Head of house hold: '))
if status < 0:
    print("Invalid status")
    exit()
else:
    if status > 3:
        print("Invalid status")
        exit()
 #asking for the income after validating the status       
income = float(input('Please enter your income: '))
single = 0
married_joint = 1
married_seprate = 2
headofhouse = 3
#calculating the tax based on the status and income, starting with the single status.
tax = 0
if status == 0:
	if income <= 11600.0:
		tax = income * 0.10
	elif income <= 47150.0:
		tax = 11600.0 * 0.10
		tax += (income - 11600.0) * 0.12
	elif income <= 100525.0:
		tax = 11600.0 * 0.10
		tax += (47150.0 - 11600.0) * 0.12
		tax += (income - 47150.0) * 0.22
	elif income <= 191950.0:
		tax = 11000.0 * 0.10
		tax += (47150.0 - 11600.0) * 0.12
		tax += (100525.0 - 47150.0) * 0.22
		tax += (income - 100525.0) * 0.24
	elif income <= 243725.0:
		tax = 11600.0 * 0.10
		tax += (47150.0 - 11600.0) * 0.12
		tax += (100525.0 - 47150.0) * 0.22
		tax += (191950.0 - 100525.0) * 0.24
		tax += (income - 191950.0) * 0.32
	elif income <= 609350.0:
		tax = 11600.0 * 0.10
		tax += (47150.0 - 11600.0) * 0.12
		tax += (100525.0 - 47150.0) * 0.22
		tax += (191950.0 - 100525.0) * 0.24
		tax += (243725.0 - 191950.0) * 0.32
		tax += (income - 243725.0) * 0.35
	else:
		income >= 609351.0 #if the income is greater than used here as it was the last in the list
		tax = 11600.0 * 0.10
		tax += (47150.0 - 11600.0) * 0.12
		tax += (100525.0 - 47150.0) * 0.22
		tax += (191950.0 - 100525.0) * 0.24
		tax += (243725.0 - 191950.0) * 0.32
		tax += (609350.0 - 243725.0) * 0.35
		tax += (income - 609350.0) * 0.37
#Here going to the married joint status
elif status == 1:
	if income <= 23200.0:
		tax = income * 0.10
	elif income <= 94300.0:
		tax = 23200.0 * 0.10
		tax += (income - 23200.0) * 0.12
	elif income <= 201050.0:
		tax = 23200.0 * 0.10
		tax += (94300.0 - 23200.0) * 0.12
		tax += (income - 94300.0) * 0.22
	elif income <= 383900.0:
		tax = 23200.0 * 0.10
		tax += (94300.0 - 23200.0) * 0.12
		tax += (201050.0 - 94300.0) * 0.22
		tax += (income - 201050.0) * 0.24
	elif income <= 487450.0:
		tax = 23200.0 * 0.10
		tax += (94300.0 - 23200.0) * 0.12
		tax += (201050.0 - 94300.0) * 0.22
		tax += (383900.0 - 201050.0) * 0.24
		tax += (income - 383900.0) * 0.32
	elif income <= 731200.0:
		tax = 23200.0 * 0.10
		tax += (94300.0 - 23200.0) * 0.12
		tax += (201050.0 - 94300.0) * 0.22
		tax += (383900.0 - 201050.0) * 0.24
		tax += (487450.0 - 383900.0) * 0.32
		tax += (income - 487450.0) * 0.35
	else:
		income >= 731201.0
		tax = 23200.0 * 0.10
		tax += (94300.0 - 23200.0) * 0.12
		tax += (201050.0 - 94300.0) * 0.22
		tax += (383900.0 - 201050.0) * 0.24
		tax += (487450.0 - 383900.0) * 0.32
		tax += (731200.0 - 487450.0) * 0.35
		tax += (income - 731200.0) * 0.37
#going to the married seprate status
elif status == 2:
    if income <= 11600.0:
        tax = income * 0.10
        tax += (income - 11600.0) * 0.12
    elif income <= 47150.0:
        tax = 11600.0 * 0.10
        tax += (income - 11600.0) * 0.12
    elif income <= 100525.0:
        tax = 11600.0 * 0.10
        tax += (47150.0 - 11600.0) * 0.12
        tax += (income - 47150.0) * 0.22
    elif income <= 191950.0:
        tax = 11600.0 * 0.10
        tax += (47150.0 - 11600.0) * 0.12
        tax += (100525.0 - 47150.0) * 0.22
        tax += (income - 100525.0) * 0.24
    elif income <= 243725.0:
        tax = 11600.0 * 0.10
        tax += (47150.0 - 11600.0) * 0.12
        tax += (100525.0 - 47150.0) * 0.22
        tax += (191950.0 - 100525.0) * 0.24
        tax += (income - 191950.0) * 0.32
    elif income <= 365600.0:
        tax = 11600.0 * 0.10
        tax += (47150.0 - 11600.0) * 0.12
        tax += (100525.0 - 47150.0) * 0.22
        tax += (191950.0 - 100525.0) * 0.24
        tax += (243725.0 - 191950.0) * 0.32
        tax += (income - 243725.0) * 0.35
    else:
        income >= 365601.0
        tax = 11600.0 * 0.10
        tax += (47150.0 - 11600.0) * 0.12
        tax += (100525.0 - 47150.0) * 0.22
        tax += (191950.0 - 100525.0) * 0.24
        tax += (243725.0 - 191950.0) * 0.32
        tax += (365600.0 - 243725.0) * 0.35
        tax += (income - 365600.0) * 0.37
#here going to the head of house hold status and using else as it cant be any other option
else:
    status == 3
    if income <= 16550.0:
        tax = income * 0.10
    elif income <= 63100.0:
        tax = 16550.0 * 0.10
        tax += (income - 16550.0) * 0.12
    elif income <= 100500.0:
        tax = 16550.0 * 0.10
        tax += (63100.0 - 16550.0) * 0.12
        tax += (income - 63100.0) * 0.22
    elif income <= 191950.0:
        tax = 16550.0 * 0.10
        tax += (63100.0 - 16550.0) * 0.12
        tax += (100500.0 - 63100.0) * 0.22
        tax += (income - 100500.0) * 0.24
    elif income <= 243700.0:
        tax = 16550.0 * 0.10
        tax += (63100.0 - 16550.0) * 0.12
        tax += (100500.0 - 63100.0) * 0.22
        tax += (191950.0 - 100500.0) * 0.24
        tax += (income - 191950.0) * 0.32
    elif income <= 609350.0:
        tax = 16550.0 * 0.10
        tax += (63100.0 - 16550.0) * 0.12
        tax += (100500.0 - 63100.0) * 0.22
        tax += (191950.0 - 100500.0) * 0.24
        tax += (243700.0 - 191950.0) * 0.32
        tax += (income - 243700.0) * 0.35
    else: 
        income >= 609351.0
        tax = 16550.0 * 0.10
        tax += (63100.0 - 16550.0) * 0.12
        tax += (100500.0 - 63100.0) * 0.22
        tax += (191950.0 - 100500.0) * 0.24
        tax += (243700.0 - 191950.0) * 0.32
        tax += (609350.0 - 243700.0) * 0.35
        tax += (income - 609350.0) * 0.37
#printing the tax and thanking the user for using the program
print(f"Tax is ${tax:.2f}")
print("*-*-*-*-*-*-*- Thank you for using", TITLE, "*-*-*-*-*-*-*-")
