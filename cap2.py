# esercitazioni 
# liste
colors = ['violet', 'indigo', 'red', 'blue', 'green', 'yellow']
print(colors)
colors.append('white')
print(colors)
colors.insert(3, 'pink')
print(colors)
colors.extend(['purple', 'magenta'])
colors
print(colors.pop())
print(colors)
del colors[1]
print(colors)
colors.remove('blue')
print(colors)
print(colors.index('white'))
print(len(colors))
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)
colors1=[color for color in colors if 'o' and 'h' in color]
print(colors1)
colors2=map(lambda x:x.upper(), colors)
print(list(colors2))
colors3=filter(lambda x:len(x)<5, colors)
print(list(colors3))
print(colors)
colors_ids=[1,2,3,4,5,6,7]
colors5 = list(zip(colors_ids, colors))
print(colors5)
for i, j in zip(colors_ids, colors):
    print("id:", i, "value:", j, sep="  ")
for index, item in enumerate(colors):
    print("id:", index, "value:", item, sep=" ")

a=(1,2,3)
b=1,2,3
c=1,
a.count(1)
a.index(1)
x,y,z=a
a[::-1]
x=dict([('color','pink'),('flower','rose')])
v1=range(4)
print(v1)
x.keys()
x.values()
x.items()
x.get('color')

a={1,2,3}
len(a)
print(a)

class Rectagle:
    sides = 4
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        print("Area:", self.length * self.breadth)
        
myR = Rectagle(4,5);
myR.area();

len("hello")
len(a)
len(x)

class Mother:
    def __init__(self, fname, sname):
        self.firstname=fname
        self.surname=sname
    def nameprint(self):
        print("Name:",self.firstname+" "+self.surname) 
class Child(Mother):
    pass

c=Child('Giuseppe','Cinque')
c.firstname

#Ex.2
x=43

#Ex.4
sent="Every cloud has a silver lining"
sent.count("a") + sent.count("e") + sent.count("i") + sent.count("o") + sent.count("u")

#Ex.5
i=[0,1,2,3,4,5]
j=['a','b','c','d','e','f']
x={i:j for i,j in zip(j,i)}
x

#Ex.7
eatables={'chocolate':2,'ice cream':3}
if eatables.__contains__('biscuits') == False:
    eatables.setdefault('biscuits',4)
    
#Ex.8
x=list(range(1,20,2))
x.append(21)
x.insert(3,23)
x.extend(list(range(2,20,2)))
x.index(15)
x.pop()
x
del x[9]
x
y=[z for z in x if z <= 13]
y
def square(n):
    return n * n
  
# We double all numbers using map()
result = map(square, y)
result0 = list(result)

result1 = [x/2 if x%2==0 else x for x in result0]
print(list(result1))