import time
from binary_search_tree import BinarySearchTree

start_time = time.time()
bst = BinarySearchTree(0)
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

'''
assignment's original code:

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

def convertNameToNumber(name):
  numString = ''
  for c in range(0,len(name)):
    numString = numString + str(ord(name[c]))
  return int(numString)

print(convertNameToNumber('Alex'))


duplicates = []
counter = 0
for name_1 in names_1:
  counter+=1
  print(counter)
  bst.insert(convertNameToNumber(name_1))
for name_2 in names_2:
  if bst.contains(convertNameToNumber(name_2)):
    duplicates.append(name_2)
#redo with binary search

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

