print('''
 Name:  Karar Khalil
 This program calculates the actual temperature based on the relative humidity and dew point.
 ''')

from math import log 
#display the welcome message
print("----Welcome to the Actual Temperature Calculator v1.02----")

#input reletive humidity in % and dew point in fahrenheit
RH= float(input("Enter the Relative Humidity (%)  "))
dew_f = float(input("Enter the Dew Point in (F) "))
dew_c = (dew_f - 32) * 5/9               #converting to celsius

#calculate the actual temperature in celsius
T = 243.04 * (((17.625 * dew_c) / (243.04 + dew_c)) - log(RH / 100)) / (17.625 + log(RH / 100) - ((17.625 * dew_c) / (243.04 + dew_c)))

#convert the actual temperature to fahrenheit and print the result
ActualTemp = (T * 9/5) + 32
print(f"The Actual Temperature is: , {ActualTemp :.3f}F")
#display the thank you message
print("----Thank you for using the Actual Temperature Calculator v1.02----")











