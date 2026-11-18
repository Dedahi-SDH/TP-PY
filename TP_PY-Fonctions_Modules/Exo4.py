x = 10

def f(x):
    x = x + 1
    return x

def g():
    global x
    x = x * 2

print(f(x))
#11
print(x)
#10
g()
#20
print(f(5))
#6