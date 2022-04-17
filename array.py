#`problem 1. print your first and last name`
print('Alisha Gapas')

#`problem 2. In the array.py create an array named 'cars' with the following elements in this order  ---- Ford,Chrysler,Dodge,Ram,Jeep,Chevy,GMC`
car = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']

 #'problem 3. print the array to the console'
print(car)

#'problem 4. print the length of the array to the console'
print(len(car))

#'problem 5. Append Buick to the Array'
car.append('Buick')

#'problem 6. print the array to the console'
print(car)

#'problem 7. print the 4th element in the array (Not index 4, element 4)'
print(car[4])

#'problem 8. Insert 'Toyota' into element 3 in the array'
car.insert(3, 'Toyota')

#'problem 9. print the array to the console'
print(car)

#'problem 10. Remove element 5 of the array (hint look at options for pop())'
car.pop(5)

#'problem 11. print the array to the console'
print(car)

#'problem 12. Sort the array in ascending order'
car.sort()

#'problem 13. print the array to the console'
print(car)

#'problem 14. Sort the array in descending order'
car.sort(reverse = True)

#'problem 15. print the array to the console'
print(car)

#'problem 16. create a variable called my_array_length with a value of the cars array length (spelling, capitalization, and spaces matter)'
my_array_length = len(car)

#'problem 17. create a variable called array_string with a value of 'The length of my array is ' (spelling, capitilization, and spaces matter)'
array_string = 'The length of my array is '
x = str(my_array_length)

#'problem 18. print array_string concatenated with my_array_length to the console'
print(array_string + x)