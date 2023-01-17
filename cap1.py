# %%
# Ex.1 funzione fatt
def fatt(x):
    res = 1
    for i in range(1, x + 1):
        res = res * i
        #print(x, " ", res)
    print(x, "!=", res)
for k in range(1, 6):
    fatt(k)

# Ex.4 
def printAst(x):
    for i in range(x, 0, -1):
        res = ""
        for j in range(i, 0, -1):
            res = res + "*"
        print(res)
        print("")
printAst(5);

# Ex.7
str="123-456-7890"
print(''.join(str.split("-")))

# Ex.8
nomeFile = input("Nome del file? ")
with open(nomeFile, 'w') as f:
    f.write("Hello World\n")
with open(nomeFile, 'r') as f:
    f.read()
with open(nomeFile, 'a') as f:
    f.write("This is the next line")
with open(nomeFile, 'r') as f:
    c = f.read()
    print(c)
    
    