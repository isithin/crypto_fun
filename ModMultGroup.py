from math import gcd
#from mathplotlib import pyplot as plt

# the class represents the multiplicative group of integers modulo n
class ModMultGroup:
    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        self.group_members = self.group_members()
        self.multiplication_table = self.multiplication_table()
    
    # calculates the coprimes of modulus
    def group_members(self) -> list[int]:
        coprimes = []
        for i in range(self.modulus):
            if gcd(i, self.modulus) == 1:
                coprimes.append(i)
        return coprimes
        

    # calculates either a list of lists (one row and on ecolumn per element of the group)
    # in row x, column y th product of x and y is written
    # or (instead of lists of lists) a dictionasy with the elements of the group as keys and the list of 
    # products with the other elements as values
    def multiplication_table(self):
        table = {}
        for i in self.group_members:
            table[i] = []
            for j in self.group_members:
                table[i].append((i*j) % self.modulus)
        return table
 
    # look up in the multiplication table
    def fast_mult(self, x: int, y: int) -> int:
        if x not in self.group_members or y not in self.group_members:
            return None
        return self.multiplication_table[x%self.modulus][self.group_members.index(y%self.modulus)]
    
    # calculate the inverse of x in the group
    def inverse(self, x: int) -> int:
        for i in self.group_members:
            if self.fast_mult(x,i) == 1:
                return i

    # calculate phi(modulus)
    def eulerphi(self) -> int:
        return len(self.group_members)
        
    # calculate x^n in (Z/nZ)*
    def power(self, x: int, n: int) -> int:
        if n < 0:
            return self.inverse(self.power(x, -n))
        if x not in self.group_members:
            return None
        return (x**n) % self.modulus
    
    def order(self, x: int) -> int:
        if x%self.modulus not in self.group_members:
            return None
        return self.power(x).index(1)
    
    def powers(self, n: int):
        return [self.power(n,y) for y in range(0,self.eulerphi()+1)]

    def is_primitive_root(self,n:int):
        nmod = n%self.modulus
        powers = self.powers(nmod)
        return set(powers) == set(self.group_members)

    def all_primitive_roots(self)-> list[int]:
        return [x for x in self.group_members if self.is_primitive_root(x)]
    
    
    # do a scatter plot that shows all powers n^i in (Z/nZ)*
    def plot_powers(self, n: int):
        args = []
        values = []
    

if __name__ == "__main__":
    g = ModMultGroup(10)
    print("All group members:")
    print(g.group_members)
    print("Multiplication table:")
    print(g.multiplication_table)
    print("Fast multiplication of 3 and 7:")
    print(g.fast_mult(3,7))
    print("Inverse of 3:")
    print(g.inverse(3))
    print("Eulerphi:")
    print(g.eulerphi())
    print("Powers of 3:")
    print(g.power(3,3))
    print("All primitive roots:")
    primroots = g.all_primitive_roots()
    for element in primroots:
        print(element)

