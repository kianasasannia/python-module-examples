import random as rn

print( rn.random() )
print( rn.uniform(1, 25) )
print( rn.randint(4, 32) )
print( rn.randrange(1, 25, step=4) )
names = ['jack', 'mark', 'kevin', 'anna']
print( rn.choice(names) )

list1=['a','b','s','d']
Char=rn.choice(list1)
if Char=='a':
    print('alice')
if Char=='b':
    print('Benjamin')
if Char=='s':
    print('Shaan')
if Char=='d':
    print('david')

while 1:
    print(rn.randint(1,20))

rn.seed(1)
# generate some random numbers
print(rn.random(), rn.random(), rn.random())
# reset the seed
rn.seed(1)
# generate some random numbers
print(rn.random(), rn.random(), rn.random())

rn.seed(1)
# prepare a sequence
sequence = ["a","b","c","d"]
print(sequence)
# make choices from the sequence
for _ in range(10):
	selection = rn.choice(sequence)
	print(selection)

rn.seed(11)
# prepare a sequence
sequence = ["a","b","c","d"]
print(sequence)
# select a subset without replacement
subset = rn.sample(sequence, 3)
print(subset)

