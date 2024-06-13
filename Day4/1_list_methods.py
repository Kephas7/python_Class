a=[(1,12),(4,1),(12,10),(3,0)]
def get_second_element(x):
    return x[1]

a.sort(key=get_second_element)
print(a) #[(3, 0), (4, 1), (12, 10), (1, 12)]

#Sort the above list based on last item of each tuple
a=[(1,2,12),(3,1,14),(1,1),(5,2,0)]
def get_last_element(x):
    return x[-1]

a.sort(key=get_last_element,reverse=True)# both key and reverse can be used
print(a)

#reverse
a=[(1,2,12),(3,1,14),(1,1),(5,2,0)]
print(a.reverse())
print(a)