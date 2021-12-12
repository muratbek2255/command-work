class My_math: 
 
    def __init__(self,a,b): 
        self.a = a if a > 0 else 1 
        self.b = b if b > 0 else 1
 
 
    def addition(self): 
        return self.a+self.b 
 
    def multiplication(self): 
        return self.a*self.b 
 
    def division(self): 
        if self.b == 0:  
            raise ValueError() 
        return self.a/self.b 
 
 
    def subtraction(self): 
        return self.a-self.b 
 
m1=My_math(a=0,b=1) 
print(m1.addition()) 
print(m1.multiplication()) 
print(m1.division()) 
print(m1.subtraction())