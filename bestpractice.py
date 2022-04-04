#!/usr/bin/env python3
'''
A multi-line comment to describe the script, made triple quotes
'''

def main():  # all code should appear within a function
    '''
    all functions have multi-line comments to describe them
    '''
    
    my_string = 'your code would go here' # vars use _ not camelCase
    print(my_string)  # print to standard_out


# calling main() using this technique allows others to import your code
if __name__ == '__main__':
    main()