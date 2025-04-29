print('''
 Name:  Karar Khalil
 This program calculates the relative humidity based on the actual temperature and dew point.
 ''')

from math import log, exp 
#display the welcome message
print("----Welcome to the Reletive Humidity Calculator v1.02 ----")

#input reletive humidity in % and dew point in fahrenheit
AT= float(input("Enter the Actual Temperature in (F) "))
AT_c = (AT - 32) * 5/9                    #converting to celsius
dew_f = float(input("Enter the Dew Point in (F) "))
dew_c = (dew_f - 32) * 5/9                #converting to celsius

#calculate the relative humidity
RH = 100 * (exp((17.625 * dew_c) / (243.04 + dew_c)) / exp((17.625 * AT_c) / (243.04 + AT_c)))

#display the relative humidity
print(f"The Reletive Humidity is: , {RH :.3f}%")

#display the thank you message
print("----Thank you for using the Relative Humidity Calculator v1.02----")

