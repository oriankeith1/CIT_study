# Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example Let us assume the following comma separated input sequence is given to the program: 100,150,180
# The output of the program should be: 18,22,24


import sys, math

if len(sys.argv) == 2:
    values = sys.argv[1].split(',')
    for num in values:
        print(int(math.sqrt((2 * 50 * int(num))/30)), end = ',')
else:
    print('Pass a comma separated list of values as argument')