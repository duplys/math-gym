from random import randint
import numpy as np

num_ex = 20

x = np.array([randint(0,100) for i in range(0,num_ex)])
y = np.array([randint(0,100) for i in range(0,num_ex)])

    
print(x)
print(y)


with open('binary_to_decimal_exercises.txt','w') as f:
    for i in range(0, num_ex):
        f.write('{:b} = \n\n'.format(x[i]))

with open('binary_to_decimal_answers.txt','w') as f:
    for e in x:
        f.write('{:b} = {}\n\n'.format(e, e))


with open('decimal_to_binary_exercises.txt','w') as f:
    for i in range(0, num_ex):
        f.write('{} = \n\n'.format(y[i]))

with open('decimal_to_binary_answers.txt','w') as f:
    for e in y:
        f.write('{} = {:b}\n\n'.format(e, e))
