def bin_search(seq,tar):
    """binary search algo. normal method"""
    start=0
    end=len(seq)-1
    while(start<=end):
        mid=(start+end)//2
        if tar<arr[mid]:
            end=mid-1
        if tar>arr[mid]:
            start=mid+1
        if tar==arr[mid]:
            return(True,mid)
    return False

def bsearch(seq,v,l,r):
    """without looping"""
    """ This is a binary search algo. this will Search the number you want:: enter the v=number you want to find"""
    if r-l==0:
        return(False)
    mid=(l+r)//2
    if (seq[mid]==v):
        return(True,mid)
    if v<seq[mid]:
        return(bsearch(seq,v,l,mid))
    if v>seq[mid]:
        return bsearch(seq, v, mid + 1, r)
    return False

if __name__ == '__main__':
    arr=[1,2,3,4,5,66,77,78,79,88,89,99,100]
    k=bin_search(arr,12)
    print(k)
    