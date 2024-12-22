Elements = [0,1,2,3,4,5,6,7,8,9]

green = ["green",]
blue = ["blue",]
yellow = ["yellow",]
red = ["red",]

for i in range(len(Elements)*4):
    if len(green) == 1:
        for n in range(len(Elements)):
            green.append(Elements[n])
            print(green)
print(green)