"""
l = ''
t = ''
while t != '/end':
    t = input("Say Something: ")
    if t == '/end':
        break
    else:
        l = l + ' ' + t

print(l)



# Default & Non-Default Argument
def fun(a, b=5):
    return a * b


print(fun(6))
""


def fun(**a):
    return (a)


print(fun(a=10, b=20, c=30, d=50))
"""

dic = {'Name': 'Vivek', 'Age': 18}

for i in dic.values():
    print(i)