for arun in 'college':
    print(arun)
for bag in ['pencil', 'eraser', 'sharpner', 'books']:
    print(bag)

heroes = [324, 34, 3534, 234]
total = 0
for hero in heroes:
    total += hero
print(f"Total number of heroes is {total}")

for x in range(0,2):
    for y in range(0,3):
        print(f"({x},{y})")

#nested loops
F = [2, 2, 2, 2, 5]
for eff in F:
    output = ''
    for count in range(eff):
        output = output + 'x'
    print(output)

#lists
name = ['john', 'harry', 'sita', 'gita']
name[2] = 'ram'
print(name[1:4])
print(name[:])
print(name[2:])
print(name[:2])

#The largest number in pr
digits = [3, 53, 32, 45, 454, 45, 2, 34]
max = 0

for digit in digits:
    if digit > max:
        max = digit
        
print(f" the greatest number is {max}")

#2D list
mattix = [
    [1, 2, 3],
    [3, 3, 5],
    [2, 4, 6]
]
mattix[1][2] = 65
print(mattix[2])
print(mattix[1][2])
print(mattix)
print(mattix[2][0])

for row in mattix:
    for item in row:
        row[2] = 0
        print(row)
        print(item)
#list methods
numberss = [2, 53, 5, 4, 6, 45, 5, 53]
print(numberss)
numberss.append(40)
numberss.remove(5)
numberss.insert(5, 3243)
numberss.reverse()
numberss.pop()
print(numberss)
print(numberss.index(53))
print(543 in numberss )
print(numberss.count(53))
numberss.sort()
print(numberss)
numberss.reverse()
print(numberss)

#Program
words = [1, 3, 4, 6, 3, 4, 15]
print(words)
unique = []
for number in words:
    if number not in unique:
        unique.append(number)
        for n in unique:
            if n < 4:
                unique.remove(n)
print(unique)

#Tuples are kind of list but unlike list we cannot modify them and remove they are immutable. instead of bracket, we use paranthessis.
hello = (2, 5, 45, 34)
print(hello)
print(hello.index(45))
print(hello.count(5))

#unpacking
list = [3, 5, 6, 5]
a, b, *c = list
print(a)
print(b)
print(*c)

tuple = ('arun', 'graduate', 26)
name, qualification, age = tuple
print(name)
print(qualification)
print(age)


z = [3, 23, 343, 4, 32, 3, 4]
print(z)
p = 0
x = []
for u in z:
    if u > p:
        p = u
for r in z:
    if r not in x:
        x.append(u)
for t in x:
    if t in x:
        x.remove(t)

print(f"the geatest number is {p}")
print(x)