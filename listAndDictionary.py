from array import array

scores=array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

# Arrays: simple types such as numbers,Must be the same type
# Lists: store anything,store any type

scores=[]
scores.append(98)   # Add new item to the end
scores.append(99)
print(scores)
print(scores[1])    #  Collections are zero-indexed

names=['Susan','Christopher']
print(len(names))  # Get the number of items
names.insert(0,'Bill')  # insert before index
print(names)
names.sort()
print(names)

presenters=names[0:2]   # Get the first two items
# starting index and number of items of retrieve
print(presenters)

# Dictionaries: key/value pairs,storage order not guaranteed
# Lists: zero-based index,storage order guaranteed

# lesson 2
christopher={}
christopher['first']='Christopher'
christopher['last']='Harrison'

susan={'first': 'Susan','last': 'Ibach'}

print(christopher)
print(susan)

print()

people=[christopher,susan]
people.append({'first': 'Bill','last':'Gates'})
presenters=people[0:2]
# print(people)
# print()
# print(presenters)
print(len(presenters))
print()