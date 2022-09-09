import sys

if len(sys.argv) == 2:
    my_list = sys.argv[1].split(',')
    print(my_list)
    print(tuple(my_list))
else: 
    print('Pass in Comma Separated Values in argument.')
    
    
    
# Operation: python n9.py 32,323,234,3234,3231
