word = 'sangmyung university'
d=dict()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1

print d

{'a': 1, ' ': 1, 'e': 1, 'g': 2, 'i': 2, 'm': 1, 'n': 3, 's': 2, 'r': 1, 'u': 2, 't': 1, 'v': 1, 'y': 2}

len(d)
Out[2]: 13

d.keys()
Out[3]: ['a', ' ', 'e', 'g', 'i', 'm', 'n', 's', 'r', 'u', 't', 'v', 'y']

d.values()
Out[4]: [1, 1, 1, 2, 2, 1, 3, 2, 1, 2, 1, 1, 2]

%matplotlib inline
import matplotlib 
import matplotlib.pyplot as plt

plt.bar(range(len(d)),d.values(),align='center')
plt.xticks(range(len(d)),list(d.keys()))
plt.show()
