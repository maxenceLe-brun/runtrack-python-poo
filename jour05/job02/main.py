"""
def ozef(x, n):
    print(x**n)
"""
def pow(x, n):
    if n<0:return 1/pow(x,n*-1)
    if n == 0:return 1
    if n>0:return x*pow(x,n-1)
print(pow(5,3))
print(pow(5,-5))
