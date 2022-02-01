#Sequences

#Lists use square brackets

thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
authors = ["Ernest Hemingway","Langston Hughes","Frank Herbert","Toni Morrison",
    "Emily Dickson","Stephen King"]

#you can join lists by adding or append or extend
newlist = thislist + authors
print('using plus:', newlist)

newlist = thislist.copy()
for x in authors:
  newlist.append(x)
print('using append:', newlist)

newlist = thislist.copy()
newlist.extend(authors)
print('using extend:', newlist)


