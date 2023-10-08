from random import randint
import numpy as np

num_ex = 20

x = np.array([randint(0,100) for i in range(0,num_ex)])
y = np.array([randint(0,100) for i in range(0,num_ex)])


def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise TypeError, "expected integer, got %s" % type(input)
    if not 0 < input < 4000:
        raise ValueError, "Argument must be between 1 and 3999"
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)


def roman_to_int(input):
    """ Convert a Roman numeral to an integer. """
    
    if not isinstance(input, type("")):
        raise TypeError, "expected string, got %s" % type(input)
    input = input.upper(  )
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]
            # If the next place holds a larger number, this value is negative
            if i+1 < len(input) and nums[input[i+1]] > value:
                sum -= value
            else: sum += value
        except KeyError:
            raise ValueError, 'input is not a valid Roman numeral: %s' % input
    # easiest test for validity...
    if int_to_roman(sum) == input:
        return sum
    else:
        raise ValueError, 'input is not a valid Roman numeral: %s' % input



    
print(x)
print(y)


with open('roman_to_decimal_exercises.txt','w') as f:
    for i in range(0, num_ex):
        f.write('{:>5} = \n\n'.format(int_to_roman(int(x[i]))))

with open('roman_to_decimal_answers.txt','w') as f:
    for e in x:
        f.write('{:>5} = {}\n\n'.format(int_to_roman(int(e)), e))


with open('decimal_to_roman_exercises.txt','w') as f:
    for i in range(0, num_ex):
        f.write('{} = \n\n'.format(y[i]))

with open('decimal_to_roman_answers.txt','w') as f:
    for e in y:
        f.write('{} = {}\n\n'.format(e, int_to_roman(int(e))))
