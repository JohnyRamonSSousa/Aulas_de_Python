x = 10

def global_sun(y):
    global X
    x = 15
    return x + y

print(x)

print(global_sun(20))

print(x)