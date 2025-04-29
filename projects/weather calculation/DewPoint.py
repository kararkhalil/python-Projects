print('''
 Name:  Karar Khalil
 This program calculates the dew point temperature in fahrenheit based on the relative humidity and actual temperature in fahrenheit
 ''')

from math import log 
#display the welcome message
print("----Welcome to the Dow point Calculator v1.02----")

#input reletive humidity in % and dew point in fahrenheit
RH= float(input("Enter the Relative Humidity (%)  "))
AT_f = float(input("Enter the Actual Temperature in (F) "))
AT_c = (AT_f - 32) * 5/9               #converting to celsius

#calculate the actual temperature in celsius
TD = 243.04 * (log(RH/100) + ((17.625*AT_c) / (243.04+AT_c))) / (17.625 - log(RH/100) - ((17.625*AT_c) / (243.04+AT_c)))


#convert the actual temperature to fahrenheit and print the result
Dew = (TD * 9/5) + 32
print(f"The Dew point Temperature is: , {Dew :.3f}F")
#display the thank you message
print("----Thank you for using the Dew Point Calculator v1.02----")
