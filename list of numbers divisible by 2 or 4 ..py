#list 1-20 divisible by 2 and 4
div=[]
for x in range(1,20):
    if(x%2==0 or x%4==0):
        div.append(x)
print(div)
