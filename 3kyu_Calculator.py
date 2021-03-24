"""
Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7

Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.

"""

class Calculator(object):
    
    def evaluate(self, string):
        if ")" in string:
            ans = self.order(string)
            while ")" in ans:
                ans = self.order(ans)
            ans = self.resolve(ans)
        else:
            ans = self.resolve(string)
        return float(ans)
    
    def order(self,string):
        ind = string.index(")")
        exp = ""
        b = ind
        while b > 0:
            b -= 1
            n = string[b]
            if n == "(":
                break
            exp = n + exp
        
        ans = string[:b] + self.resolve(exp) + string[ind+1:]
        return ans
    
    def resolve(self,string):
        spl = self.chop(string)
                
        while len(spl)>1:
            spl = self.reduce(spl)
            
        return spl[0]


    def chop(self,string):
        string = string + " "
        enc_n = False
        all_n = []
        n = ""
        for i in string:
            if i.isnumeric():
                enc_n = True
                n += i
            elif not enc_n:
                n += i
            elif i == ".":
                n += i
            elif i in " +-*/":
                enc_n = False
                all_n.append(n.replace(" ", ""))
                n = ""
        return all_n
    
    def reduce(self,all_n):
        if len(all_n) == 1:
            return all_n
        
        for cnt,val in enumerate(all_n):
            if "*" in val or "/" in val:
                new_el = self.calc(all_n[cnt-1],all_n[cnt])
                all_n[cnt] = new_el
                all_n.pop(cnt-1)
                return all_n
        
        new_el = self.calc(all_n[0],all_n[1])
        all_n[0] = new_el
        all_n.pop(1)
        return all_n
        
            
            
    def calc(self,n1,n2):
        if n2[0].isnumeric():
            op = "+"
            n2 = float(n2)
        else:
            op = n2[0]
            n2 = float(n2[1:])
        # op = n2[0]
        n1 = float(n1)
        
        
        if op == "+":
            ans = n1 + n2
        elif op == "-":
            ans = n1 - n2
        elif op == "*":
            ans = n1 * n2
        elif op == "/":
            ans = n1 / n2
        
        ans = round(ans,8)
        return str(ans)