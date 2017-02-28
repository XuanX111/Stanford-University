# karatsuba_multiplication
import timeit

input = raw_input('Enter any two integer number separated by space')
input_list = input.split()
start = timeit.default_timer()
x = input_list[0]
y = input_list[1]
#count the number of digit in x
n_x = len(x)
n_y = len(y)
if n_x<=2 or n_y<=2:
    step5 = int(x)*int(y)
else:
    #split the x, y by n/2
    a = x[:n_x/2]
    b = x[n_x/2:]
    c = y[:n_y/2]
    d = y[n_y/2:]
    #print a,b,c,d
    # step 1
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    step1 = a*c
    step2 = b*d
    step3 = (a+b)*(c+d)
    step4 = step3-step2-step1
    step5 = step1*10**(n_x)+step4*10**(n_x/2)+step2
stop = timeit.default_timer()
print step5
print stop-start

start2 = timeit.default_timer()
print int(x)*int(y)
stop2 = timeit.default_timer()
print stop2 - start2