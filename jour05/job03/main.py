def long(txt:str = ""):
    if txt == "":
        return 0
    else:
        return 1 +long(txt[:-1])
print(long("salut moi c'est maxence"))
