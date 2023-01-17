import re

re.search('and', 'telma and luise')

search_pattern = re.compile(r'ma')
re.search(search_pattern,'telma and luise')

re.findall('3', '4324324325432')
re.search('3', '4324324325432')
re.match('4', '4324324325432')
re.split('3', '4324324325432')
re.sub('3','three','4324324325432')
re.findall('ba.', 'bath bokf ba baaaal bathroom')

from sympy import symbols, solve
from sympy.plotting import plot
x = symbols('x')
plot(x+5)
plot(x**4+4*x**3+2*x**2+x+100)
sol=solve(x**2-5*x+6, dict=True)
sol

from sympy import FiniteSet
l={1,2,3}
s1=FiniteSet(*l)
s2=FiniteSet(2,3,4)
us=s1.union(s2)
is1=s1.intersect(s2)
is1
s1=FiniteSet(1,2,3,4,5,6,7,8,9,10)
s2=FiniteSet(3,6,9)
p=len(s2)/len(s1)
p

from sympy import symbols, limit
x = symbols('x')
limit((1 + x)/x,x,3)

from sympy import symbols, diff
x = symbols('x')
e=(x**3-4*x)/x
d=diff(e)
d

from sympy import symbols, integrate
x = symbols('x')
e=(x**3-4*x)/x
i=integrate(e)
i