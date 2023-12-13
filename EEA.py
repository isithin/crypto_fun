def enhanced_euclidean_algorithm(a,b):
    if a == 0:
        return (b,0,1)
    elif b == 0:
        return (a,1,0)
    else:
        g,y,x = enhanced_euclidean_algorithm(b%a,a)
        return (g,x-(b//a)*y,y)
    
if __name__ == "__main__":
    a = 7
    b = 40
    print(enhanced_euclidean_algorithm(a,b))
    print("The greatest common divisor of {} and {} is {}".format(a,b,enhanced_euclidean_algorithm(a,b)[0]))
    print("The coefficients of {} and {} are {} and {}".format(a,b,enhanced_euclidean_algorithm(a,b)[1],enhanced_euclidean_algorithm(a,b)[2]))
    print("{}*{} + {}*{} = {}".format(13,enhanced_euclidean_algorithm(a,b)[1],b,enhanced_euclidean_algorithm(a,b)[2],enhanced_euclidean_algorithm(a,b)[0]))
