#write a function that calculates with the enhanced eucledean algorithm given two numbers
def enhanced_euclidean_algorithm(a,b):
    if a == 0:
        return (b,0,1)
    elif b == 0:
        return (a,1,0)
    else:
        g,y,x = enhanced_euclidean_algorithm(b%a,a)
        return (g,x-(b//a)*y,y)
    
if __name__ == "__main__":
    print(enhanced_euclidean_algorithm(13,57))
    print("The greatest common divisor of {} and {} is {}".format(13,57,enhanced_euclidean_algorithm(13,57)[0]))
    print("The coefficients of {} and {} are {} and {}".format(13,57,enhanced_euclidean_algorithm(13,57)[1],enhanced_euclidean_algorithm(13,57)[2]))
    print("{}*{} + {}*{} = {}".format(13,enhanced_euclidean_algorithm(13,57)[1],57,enhanced_euclidean_algorithm(13,57)[2],enhanced_euclidean_algorithm(13,57)[0]))
