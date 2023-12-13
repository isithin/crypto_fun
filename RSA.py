from ModMultGroup import ModMultGroup
from math import gcd

# represents an RSA implementation based on our prebuilt factor group
class RSA:
    # constructor with primes p, q, (n=p*q,e) is the public key
    def __init__(self, p: int, q: int, e: int) -> None:
        self.p = p
        self.q = q
        self.e = e
        self.n = p*q
        self.phi = (p-1)*(q-1)
        self.factor_group = ModMultGroup(self.n)
        if gcd(self.phi, self.e) != 1:
            raise Exception("e is not coprime to phi(n)")

    # encrypts a message m with RSA
    def encrypt(self, m: int) -> int:
        c = self.factor_group.power(m, self.e)
        return c

    # decrypts a ciphertext c
    def decrypt(self, c: int) -> int:
        d = ModMultGroup(self.phi).inverse(self.e)
        m = c**d % self.n
        return m
    
# represents an RSA-based signature scheme
class Signature:
    # constructor receives RSA implementation to be used for signing
    def __init__(self, rsa) -> None:
        self.rsa = rsa

    # trivial implementation of a hash (not cryptographically secure,
    # just to show the case)
    def hash(self,m):
        return (m+1)%self.rsa.n
    
    # signs a message m
    def sign(self, m):
        h = self.hash(m)
        s = self.rsa.encrypt(h)
        return s

    # verifies both the integrity of the message m and the validity 
    # of the signature
    def verify(self, m, s):
        h = self.hash(m)
        h2 = self.rsa.decrypt(s)
        return h==h2

# represents an implementation of the DH key exchange
class Diffie_Hellman: 
    # constructor receives n for the cyclic group (Z/nZ)* and a primitive root g
    def __init__(self, n: int, g: int) -> None:
        self.n = n
        self.g = g
        self.factor_group = ModMultGroup(n)

    # calculates the keys that are subsequently exchanged
    def key_generation(self, alpha: int, beta: int):
        ga = self.factor_group.power(self.g, alpha)
        gb = self.factor_group.power(self.g, beta)
        return (ga,gb)

    # calculates the final shared secret based on the exchanged keys
    def key_exchange(self, alpha: int, beta: int, ga: int, gb: int):
        gab = self.factor_group.power(ga, beta)
        gba = self.factor_group.power(gb, alpha)
        return gab == gba

if __name__=='__main__':
    p = 17
    q = 7
    e = 7
    m = 2
    rsa = RSA(p,q,e)
    print(f"encryption of {m} in RSA with public key n={p*q} and e={e} yields {rsa.encrypt(m)}")
    print(f"decryption of {rsa.encrypt(m)} yields {rsa.decrypt(rsa.encrypt(m))}")

    sig = Signature(rsa)
    s = sig.sign(m)
    print(f"signature for message {m} yields {s} where hash was {sig.hash(m)}")
    print(f"verification of signature yields {sig.verify(m,s)}")

    n = 11
    g = 2
    dh = Diffie_Hellman(n,g)
    alpha = 3
    beta = 4
    (ga,gb) = dh.key_generation(alpha, beta)
    print(f"DH key generation for alpha = {alpha} and beta = {beta} in group (Z/{n}Z)^* with primitive root {g} yields {(ga,gb)}")
    print(f"DH key exchange yields {dh.key_exchange(alpha, beta, ga, gb)}")

    