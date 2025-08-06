#Sum Even Numbers

number_added = 0

for number in range (0,6):
	user_number = int(input('Enter a number:'))
	if user_number % 2 == 0:
		number_added = number_added + user_number
		
print(f'The sum of all even numbers is: {number_added}')