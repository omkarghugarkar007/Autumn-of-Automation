import numpy as np

def naive_method(days, Price):

	#Assuming if you invested a day, what will be the profits and store in array and then trying to maximize the profits considering all the days

	Max_Profit = np.zeros((1,days-1))

	for i in range(days-1):

		selling_price = 0

		for j in range(i+1,days):

			if int(Price[j]) > int(selling_price):

				selling_price = Price[j]

		Profit = int(selling_price) - int(Price[i])

		Local_Max = Profit

		Max_Profit[0,i] = int(Local_Max)

	Max_day = np.argmax(Max_Profit)

	return int(Max_day), int(Max_Profit[0,Max_day])


#Take number of days as integer input and then store stock prices in an Array

#print("Enter number of Days")
days = int(input())

Price = np.zeros((1, days))

Values = input()

Price = Values.split(" ")

day, Profit = naive_method(days, Price)

print(Profit)
print(day + 1)