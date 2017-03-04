# karatsuba_multiplication
import timeit

#input = raw_input('Enter any two integer number separated by space')
#input_list = input.split()
#input_list = ['3141592653589793238462643383279502884197169399375105820974944592','2718281828459045235360287471352662497757247093699959574966967627']
input_list = ['1234','5678']
x = input_list[0]
y = input_list[1]
#count the number of digit in x

n_x = len(x)
n_y = len(y)
if n_x<=1 or n_y<=1:
    step5 = int(x)*int(y)
else:
    #split the x, y by n/2
    a = x[:n_x/2]
    b = x[n_x/2:]
    c = y[:n_x/2]
    d = y[n_x/2:]
    #print a,b,c,d
    # step 1
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    start = timeit.default_timer()
    step1 = a*c
    step2 = b*d
    step3 = (a+b)*(c+d)
    step4 = step3-step2-step1
    step5 = step1*10**(n_x)+step4*10**(n_x/2)+step2
    stop = timeit.default_timer()
    print stop-start
print step5


start2 = timeit.default_timer()
print int(x)*int(y)
stop2 = timeit.default_timer()
print stop2 - start2

def karatuba(x,y):
    n_x = len(x)
    if n_x <= 1:
        step1 = a * c
        step2 = b * d
        step3 = (a + b) * (c + d)
        step4 = step3 - step2 - step1
        step5 = step1 * 10 ** (n_x) + step4 * 10 ** (n_x / 2) + step2
    else:


