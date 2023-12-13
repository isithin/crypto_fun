from typing import Set, List, Tuple

class Relation:
    def __init__(self, m: Set[int], n: Set[int], l: Set[Tuple[int, int]]):
        self.m = m
        self.n = n
        self.l = l

    def adjacency_matrix(self) -> List[List[int]]:
        #return [[l if (i,j) in self.l else 0 for j sorted(self.n)] for sorted(self.m)]
        rows = len(self.m)
        cols = len(self.n)
        ad_m = [[0 for _ in range(0,cols)] for _ in range(0,rows)]
        sorted_m = sorted(self.m)
        sorted_n = sorted(self.n)
        for tuple in self.l:
            x = tuple[0]
            y = tuple[1]
            a = sorted_m.index(x)
            b = sorted_n.index(y)
            ad_m[a][b] = 1
        return ad_m

    def __str__ (self):
        return str(self.adjacency_matrix())
    
    def __eq__(self, other) -> bool:
        return self.m == other.m and self.n == other.n and self.l == other.l
    
    
class Mono_Set_Relation(Relation):
    def __init__(self, m: Set[int], l: Set[Tuple[int, int]]):
        super().__init__(m, m, l)
    
    def is_refleive(self) -> bool:
        for x in self.m:
            if (x,x) not in self.l:
                return False
        return True
    
    def is_antisymmetric(self) -> bool:
        for (a,b) in self.l:
            if a is not b and (b,a) in self.l:
                return False
        return True
    
    def is_symmetric(self) -> bool:
        for (a,b) in self.l:
            if (b,a) not in self.l:
                return False
        return True
    
    def is_transitive(self) -> bool:
        for (a,b) in self.l:
            for c in [y for (x,y) in self.l if x==b]:
                if (a,c) not in self.l:
                    return False
        return True
    
    def is_order(self) -> bool:
        return self.is_refleive() and self.is_antisymmetric() and self.is_transitive()
    
    def is_equivalence_relation(self) -> bool:
        return self.is_refleive() and self.is_symmetric and self.is_transitive
    

class Function(Relation):
    def __init__(self, m: Set[int], n: Set[int], l: Set[Tuple[int, int]]):
        super().__init__(m, n, l)
        if not self.is_function():
            raise Exception("Is not a function")

    def is_function(self) -> bool:
        for x in self.m:
            x_maps = [b for (a,b) in self.l if a==x]
            if len(x_maps)!=1:
                return False
        return True
                    


if __name__ == '__main__':
    r = Relation({1,2,3},{1,2,3},{(1,1),(1,2),(2,2),(3,2),(3,1)})
    momor = Mono_Set_Relation({1,2,3},{(1,1),(1,2),(2,2),(3,2),(3,1)})
    print(momor.is_refleive())
    print(momor.is_antisymmetric())
    print(momor.is_transitive())
    