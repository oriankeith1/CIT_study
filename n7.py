# Write a function called show_stars(rows). If rows is 5, it should print the following:

def show_stars(rows):

    # outer loop
    for i in range(rows + 1):  # to cater for the last row , add 1.
        
        # nested loop
        for j in range(i):
            
            # display *
            print('*', end = '')
            
        # newline after each row
        print('')
        
show_stars(rows=5)