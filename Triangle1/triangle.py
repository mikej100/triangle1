'''Triangle tester
    Mike Jennings 2016-05
'''


def equilateral(sides):
    ''' Test for equilateral.'''
    result = len(set(sides)) ==1
#    result = sides[0] == sides[1] == sides[2]
    return result

def parse_input(input_string):
    print("parseInput")
    return "error"

def isosceles(sides):
    ''' Test for isosceles (includes equilateral).'''
    result = len(set(sides)) <=2
    return result

def right_angle(sides):
    ''' Test for right angle.'''
    ss = sorted(sides)
    result = ss[0]**2 + ss[1]**2 == ss[2]**2

def side_too_long(sides):
    ''' Test for one side >= other two lengths.'''
    ss = sorted(sides)
    result = ss[0] + ss[1] <= ss[2]
    return result


#def number(string):
#    ''' Convert to number, caller catch ValueError if not number.'''
#    try: 
#        num = int(string)
#    result = num
#    except ValueError:
#        result = NOT_A_TRIANGLE
    

         #
    #except ValueError:    # don't allow floats
    #    try:
    #        return float(string)

       

#def get_three_items(input_string):
#    '''extract three space separated strings as list'''
#    input_list = input_string.split()
#    if len(input_list) != 3:
         

def test_for_triangle(input_items):
    ''' Test three input string items for being a triangle'''
    input_nums = []
    for items in input_list:
        try:
            number = int(item)
            if number <0:
                result = NOT_A_TRIANGLE
            else:
                input_nums.add(num(item))
        except ValueError:
            result = NOT_A_TRIANGLE
        
    if result != NOT_A_TRIANGLE:      # If we have three numbers, test for triangle.
        if side_too_long(input_nums):
            result = NOT_A_TRIANGLE
        elif equilateral(input_nums):
            result = "Equilateral"  
        elif isosceles(input_nums):
            result = "Isosceles"
        else:
            result = "Squalene"
    
                    
    
    
def user_input():
    done = False          
    while not done:                 # Repeat until the done flag gets set
        
        input_block = input("Enter three positive integers:")
        
        input_list = input_block.split
        if len(input_list) != 3:
            result = NOT_A_TRIANGLE
        else:
            result = test_for_triangle(input_list)
    
        print 'Computer says {result}'.format(**locals())
        
        done = input("Another? ").lower() != 'y'    # != is 'not equal'

    print("Done!")
    
if __name__ == "__main__":
    print("Hello world!")
    user_input()
        