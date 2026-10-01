n = int(input("Enter number of elements: "))
a = []
for i in range(n):
       x = 6
       a.append(x)

print("List elements are", a)
x = int(input("Enter element to insert: "))
pos = int(input("Enter index position: "))
a.insert(pos, x)
print("List after insertion:", a)

x = int(input("Enter element to remove: "))
pos = int(input("Enter remove position: "))
a.remove(x)
print("List after removal:", a)


x = int(input("delete element by its index: "))
pos = int(input("delete position: "))
a.pop(pos)
print("List after removal of ele by its its index:", a)


a.sort()
print("List after ascending of ele by its its index:", a)

a.reverse()
print("List after reversel of ele by its its index:", a)

