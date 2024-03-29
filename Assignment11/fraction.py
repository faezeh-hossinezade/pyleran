class fraction:
    def __init__(self,numerator1, denominator1,numerator2, denominator2):
        self.num1=numerator1
        self.den1=denominator1
        self.num2=numerator2
        self.den2=denominator2
    
    
    # methods     
    def findGCD(self):
        gcd = 0
        for i in range(1, int(min(self.num1, self.num2)) + 1):
            if self.num1 % i == 0 and self.num2 % i == 0:
                gcd = i
        return gcd
    
    def selfGCD(self,num,den):
        gcd = 0
        for i in range(1, int(min(num, den)) + 1):
            if num % i == 0 and den % i == 0:
                gcd = i
        return gcd
    
   
    def sum(self):
        common_deno=self.findGCD()
        lcm = (self.den1 * self.den2) // common_deno
        sum = (self.num1 * lcm // self.den1) + (self.num2 * lcm // self.den2)
        num3 = sum // common_deno
        lcm = lcm // common_deno
        print(self.num1, "/", self.den1, " + ", self.num2, "/", self.den2, " = ", num3, "/", lcm)
        
    def sub (self):
        common_deno=self.findGCD()
        lcm = (self.den1 * self.den2) // common_deno
        sum = (self.num1 * lcm // self.den1) - (self.num2 * lcm // self.den2)
        num3 = sum // common_deno
        lcm = lcm // common_deno
        print(self.num1, "/", self.den1, " - ", self.num2, "/", self.den2, " = ", num3, "/", lcm)
        
        
    def mul(self):
        mul2=self.den1*self.den2
        mul1=self.num1*self.num2
        print(self.num1, "/", self.den1, " * ",self.num2, "/", self.den2, " = ", mul1, "/", mul2)
        
    
    def div (self):
        div2=self.den1*self.num2
        div1=self.num1*self.den2
        print(self.num1, "/", self.den1, " * ", self.num2, "/", self.den2, " = ", div1, "/", div2)
        
    def convrtnumber(self):
        frac1=self.num1/self.den1
        frac1=float(frac1)
        frac2=self.num2/self.den2
        frac2=float(frac2)
        print("The result obtained for Frac1 = ", frac1, "\nThe result obtained for Frac2 = ", frac2)
    
        
    def simplify_fraction(self,num,den):
    
        if den == 0:
            print("Division by 0 - result undefined") 
        else:
            common_divisor = self.selfGCD(num,den)
            (reduced_num, reduced_den) = (num/ common_divisor, den/ common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.
            if reduced_den == 1:
                print ("%d/%d is simplified to %d" % (num, den, reduced_num))
            elif common_divisor == 1:
                print("%d/%d is already at its most simplified state" % (num, den)) 
            else:
                print("%d/%d is simplified to %d/%d" % (num,den, reduced_num, reduced_den)) 
        

num1, den1 = map(int, list(input("Enter numerator and denominator of first number : ").split(" ")))
num2, den2 = map(int, list(input("Enter numerator and denominator of second number: ").split(" ")))
fraction_1 = fraction(num1, den1, num2, den2)
fraction_1.sum()
fraction_1.mul()
fraction_1.div()
fraction_1.sub()
fraction_1.convrtnumber()
fraction_1.simplify_fraction(num1,den1)
fraction_1.simplify_fraction(num2,den2)