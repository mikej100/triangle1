def num(string):
    ''' Convert to number, caller must catch exception if cannot.'''
    try:
        return int(string)
    except ValueError:
            return float(string)

input_string = "12.a"
try:
    number_ = num(input_string)
except ValueError:
    print ("Bad number")
else:
    print (number_)