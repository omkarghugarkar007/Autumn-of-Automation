#Function to count number of digits in a number
def Number_of_digits(number):

	quotient = int(number)
	count = 1
	while(quotient >= 10):

		quotient = quotient/10
		count = count + 1 

	return count

print("Enter a Palindrome number to get next smallest Palindrome number")
num = int(input())

#Work only if give number is Palindrome
if str(num) == str(num)[::-1]:

	Digits = Number_of_digits(num)

	string = str(num)
	front_half = ''

#To calculate the next Palindrome number, there exist 3 possible cases

#Case 1: Entire number consist of 9, eg:999,99,9,etc.

	if Digits == (Number_of_digits(num + 1) - 1):

		print(num + 2)

#Case 2: Number of digits in given Number is even

	elif Digits%2 == 0:

		for i in range(int(len(string)/2)):

			front_half = front_half + string[i]

		front_half = int(front_half) + 1

		next_half = str(front_half)[::-1]

		print(str(front_half) + next_half)

#Case 3: Number of Digits in given Number is Odd

	else:

		for i in range(int(len(string)/2+1)):

			front_half = front_half + string[i]

		front_half = int(front_half) + 1

		next_half = str(int(front_half/10))[::-1]

		print(str(front_half) + next_half)

#Error message for non-palindrome number

else:

	print("Entered Number is not Palindrome Number")











