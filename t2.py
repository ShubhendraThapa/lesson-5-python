lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:",len(lst))
print("First Element:", lst[0])
print("Lat Element:",lst[-1])
lst.append('papaya')
print("Updated List:",lst)

lst.remove('Guava')
print("Updated List:", lst)

lst.sort()
print("Sorted list:", lst)

lst.pop(1)
print("Updated List:",lst)

lst.reverse()
print("Reversed List:",lst)

print("Multiplication List:",lst*2)

lst = lst[:4]
print("Sliced List:",lst)

lst.clear()
print("Updated List:",lst)



