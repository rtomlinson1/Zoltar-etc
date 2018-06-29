# Write a program that prints the numbers from 1 to 20. But for multiples
# of three print “Fizz” instead of the number and
# for the multiples of five print “Buzz”. For numbers
# which are multiples of both three and five print “FizzBuzz”.

for number in range(1, 21):
    string = ""

    if number % 3 == 0:
        string = string + "Fizz"

    if number % 5 == 0:
        string = string + "Buzz"

    if number % 3 != 0 and number % 5 != 0:
        string = number
        
    print(string)

