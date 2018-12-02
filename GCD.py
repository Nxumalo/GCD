def gcd(x ,y):
    while(x != 0):
        if(x<y):
            exchange = x
            x = y
            y = exchange
        x %= y
    return y
                                
x = gcd(400,300)
print(x)
