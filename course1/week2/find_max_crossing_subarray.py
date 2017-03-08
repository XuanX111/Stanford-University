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
