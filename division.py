from random import randint
import numpy as np

num_ex = 10

x = np.array([randint(0,100) for i in range(0,num_ex)])
y = np.array([randint(0,100) for i in range(0,num_ex)])

z = x * y

print(x)
print(y)
print(z)

with open('division_exercises.txt','w') as f:
    for i in range(0, num_ex):
        f.write('{:>5} : {:>5} = \n\n\n\n\n\n\n\n\n\n\n\n\n\n'.format(z[i],x[i]))

with open('division_answers.txt','w') as f:
    for e in y:
        f.write('{}\n\n'.format(e))
