inv = 0

def countSplitInv(alist):
    #print alist
    global inv

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        countSplitInv(lefthalf)
        countSplitInv(righthalf)

        i = 0
        j = 0
        k = 0


        # count the split inversion in merge sortd
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] > righthalf[j]:
                alist[k] = righthalf[j]
                j = j+1
                inv = inv + len(lefthalf)-i

            else:
                alist[k] = lefthalf[i]
                i = i+1
            k = k+1

        while i<len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j<len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
        #print inv
    return inv


alist = [54,26,93,17,77,31,44,55,20]
inv = countSplitInv(alist)
print alist
print inv

