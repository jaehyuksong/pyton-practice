num = int(input('Enter a positive integer : '))

if num > 0:			# If num is positive
    print('num : ', num)
    if num % 2 == 0:    	            # If the remainder of num divided by 2 is 0
        print('num is even number')
    else:                 	            # If the remainder of num divided by 2 is not 0
        print('Num is an odd number')
else:
    print('Num is not a positive number.')
