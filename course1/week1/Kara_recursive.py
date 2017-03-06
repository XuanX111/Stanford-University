# karatsuba_multiplication
import timeit
import math

# input = raw_input('Enter any two integer number separated by space')
# input_list = input.split()
# input_list = ['3141592653589793238462643383279502884197169399375105820974944592','2718281828459045235360287471352662497757247093699959574966967627']

def Kara(x,y):

    # count the number of digit in x
    n_x = len(x)
    n_y = len(y)

    if(n_x==0 or n_y==0):
        return 0
    if n_x <= 1 or n_y<= 1:
        step5 = int(x) * int(y)
    else:
        if n_x % 2 != 0:
            x = '0' + x
            n_x = n_x + 1
        if n_y % 2 !=0:
            y = '0' + y
            n_y = n_y + 1

        # split the x, y by n/2
        a = x[:n_x/2]
        b = x[n_x/2:]
        c = y[:n_x/2]
        d = y[n_x/2:]

        if (len(a) == 0):
            a='0'
        if (len(b) == 0):
            b='0'
        if (len(c) == 0):
            c='0'
        if (len(d) == 0):
            d='0'


        step1 = Kara(a,c)
        step2 = Kara(b,d)
        step3 = Kara(str(int(a)+int(b)),str(int(c)+int(d)))
        step4 = step3 - step2 - step1
        step5 = step1 * 10 ** (n_x) + step4 * 10 ** (n_x / 2) + step2

    return step5

#input_list = ['1234000000', '5678000000']
#2718281828459045 2353602874713526 62497757 24709369 99595749 66967627
input_list = ['3141592653589793238462643383279502884197169399375105820974944592','2718281828459045235360287471352662497757247093699959574966967627']
print len(input_list[1])
print int(input_list[0])*int(input_list[1])
x = input_list[0]
y = input_list[1]
product = Kara(x,y)
print product

