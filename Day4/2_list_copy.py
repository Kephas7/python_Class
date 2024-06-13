a=[1,2,3,4]
b=a #this is passes by reference 
print(a) #[1,2,3,4,5]

a=["1","a","b"]
a.insert(3,"hello")
print(a)