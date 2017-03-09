def find_max_crossing_subarray(A,low,mid,high):
    left_sum = float('inf')
    sum = 0
    for i in xrange(mid,low):
        sum +=A[i]
        if sum>left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('inf')
    sum = 0
    for j in xrange(mid+1,high):
        sum +=A[j]
        if sum>right_sum:
            right_sum = sum
            max_right = j
    return(max_left,max_right,left_sum,right_sum)
#class maxsum:
#    def __init__(self,first,last,pay):

def find_maximum_subarray(alist,low,high):

    if high==low:
        return(low,high,alist[low])
    else:
        mid = (low+high)/2
        (left_low,left_high,left_sum) = find_maximum_subarray(alist,low,mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(alist,mid,high)
        (cross_low,cross_high,cross_sum) = find_max_crossing_subarray(alist,low,mid,high)
    if left_sum>=right_sum and left_sum>=cross_sum:
        return (left_low,left_high,left_sum)
    if right_sum>=left_sum and right_sum>=cross_sum:
        return (right_low,right_high,right_sum)
    else:
        return (cross_low,cross_high,cross_sum)





