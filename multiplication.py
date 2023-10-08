import codecs
from random import randint
import numpy as np

num_ex = 10

x = np.array([randint(0,100) for i in range(0,num_ex)])
y = np.array([randint(0,100) for i in range(0,num_ex)])

z = x * y

print(x)
print(y)
print(z)

with codecs.open('multiplication_exercises.txt','w', encoding='utf8') as f:
    for i in range(0, num_ex):
        if x[i] >= y[i]:
            f.write(u'{:>5} {} {} \n\n\n\n\n\n\n\n\n\n\n\n\n\n'.format(x[i],u'\u22c5',y[i]))
        else:
            f.write(u'{:>5} {} {} \n\n\n\n\n\n\n\n\n\n\n\n\n\n'.format(y[i],u'\u22c5',x[i]))

with open('multiplication_answers.txt','w') as f:
    for e in y:
        f.write('{}\n\n'.format(e))
