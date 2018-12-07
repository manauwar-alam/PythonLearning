class subset :
    def f1(self, s1):
        return self.f2([], sorted(s1))
    
    def f2(self, cur, s1):
        if s1:
            return self.f2(cur, s1[1:]) + self.f2(cur + [s1[0]], s1[1:])
        return [cur]
    
a = []
n = int(input("Enter number of element of set : "))

for i in range(0, n):
    b = int(input("Enter element : "))
    a.append(b)
 
    

# Calling the method using class sub
print("Subsets : ")
print(subset().f1(a))



