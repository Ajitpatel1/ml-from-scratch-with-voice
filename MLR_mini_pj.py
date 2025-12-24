import numpy as np 
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.spvoice")
import time

x1 = np.array([2 , 3 , 3 , 4 , 4 , 5, 2 , 3 , 4])
x2 = np.array([1 , 1 , 2 , 2 , 2 , 2 , 1 , 1 , 2])
x3 = np.array([1 , 1 , 1 , 1 , 2 , 2 , 1 , 1 , 2])

X = np.column_stack((x1 , x2 , x3))
# print(X)

y = np.array([35, 45, 55, 65, 75, 90, 38, 48, 78])

onee = np.ones((X.shape[0] , 1))
x_b = np.hstack((onee , X))
# print(x_b)

theta = np.linalg.inv(x_b.T @ x_b) @ x_b.T @ y
# print(theta)
b0 , b1 , b2 , b3 = theta

speak.Speak("Enter your name ")
name_input = input("Enter your name : ")

speak.Speak("Enter the number of  Bedroom ")
bedroom = int(input("Enter the number of  Bedroom : "))

speak.Speak("Enter the number of  hall ")
hall = int(input("Enter the number of  Hall : "))

speak.Speak("Enter the number of  kitchen ")
kitchen = int(input("Enter the number of kitchen : "))

speak.Speak("Plese wait 5 second iam just Calculutaing your House price  ")
print("Plese wait 5 second iam just Calculutaing your House price.......  ")

time.sleep(5)


predicted_price_calculution = (b0 + b1 * bedroom + b2 * hall + b3 * kitchen)

speak.Speak("Congratulation" + name_input) 

speak.Speak(f"Your predicted house price is {predicted_price_calculution:.2f} lakh rupees")


print(f"your predicted price is : {predicted_price_calculution:.2f} Lakh Rupees : ")