# insertion sort

input = raw_input('Enter any two integer number separated by space')
input_list = input.split()
input_num = [float(a) for a in input_list]

n = len(input_num)
for j in xrange(1,n):
    key = input_num[j]
    i = j-1
    while i>=0 and input_num[i]>key:
        input_num[i+1] = input_num[i]
        i = i-1
    input_num[i+1] = key
print input_num

