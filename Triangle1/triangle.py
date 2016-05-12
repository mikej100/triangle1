'''Triangle tester
    Mike Jennings 2016-05
'''
def parse_input(input_string):
    print("parseInput")
    return "error"

def user_input():
    done = False          
    while not done:                 # Repeat until the done flag gets set
        
        input_block = input("Enter your numbers:")
        result = parse_input("blue")
        
        done = input("Another? ").lower() != 'y'    # != is 'not equal'

    print("Done!")
    
if __name__ == "__main__":
    print("Hello world!")
    user_input()
        