st = "Hi, my name is Biprajit Debnath. I am from West Bengal."
console = 80
count = 0
while(console>=0):
    req = ""
    for i in st:
        if(i==" "):
            console = console - 2
            count = count + 2
            req = req + i
        else:
            console = console - 5
            count = count+5
            req = req + i
    print(req)


