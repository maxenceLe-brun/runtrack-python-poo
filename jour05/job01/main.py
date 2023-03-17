def factorielle(n, total = 1):
    if n<=0:print("ERROR")
    elif n>1:a(n-1, total*n)
    else:print(total)
factorielle(5)
factorielle(0)
