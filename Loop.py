# for i in (1,2,3,4,5):
#     print(i)

# skip the if condition block, will verify
for i in range(0,5):
    if (i%2):
        pass
        print(i)

# The else block is executed only if the for loop completes 
# without encountering a break statement.
for i in range(10):
    for j in range(10):
        if (i % 2 == 0):
            break
    else: # this else block act as a part of For Loop
        print("For loop executed properly for ", str(i))