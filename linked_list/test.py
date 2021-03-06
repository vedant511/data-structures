from linked_list.LinkedList import List

lst = List()

print('=====ADD======')
print(lst.is_empty())
lst.add(31)
lst.add(77)
lst.add(17)
lst.add(93)
lst.add(26)
lst.add(54, pos=10)
lst.add(54, pos=5)
lst.add(95)
lst.add(11)
lst.add(2)
lst.add(28)
lst.add(18)
print(lst.get_size())
print(lst.traverse())
print(lst.is_empty())
print(lst.head.data)

print('=====REMOVE=====')
lst.remove(54)
lst.remove(31)
lst.remove(100)
print(lst.get_size())

print('=====SEARCH=====')
print(lst.search(93))
print(lst.search(5))

print('=====INDEX=====')
print(lst.index(17))
print(lst.index(55))

print('======POP======')
print(lst.pop())
print(lst.pop(pos=10))
print(lst.pop(pos=5))
