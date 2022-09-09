# Write a function to compute 5/0 and use try/except to catch the exceptions.

def trydivisor():
    '''
    a = 5
    b = 0e
    '''
    a = int(input('Enter your A value here : '))
    b = int(input('Enter your B value here : '))
    
    try:
        a/b
        print('Result is: ', a/b)
    except ZeroDivisionError:
        
        print("Please don't divide by zero")
    
    
trydivisor()
