def insertion(arr):
    """Insertion sorting algo."""
    for i in range(1,len(arr)):
        current=arr[i]
        j=i-1
        while(j>=0 and arr[j]>current):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=current;
    return arr

if __name__ == '__main__':
    arr=[4,3,6,2,8,1,9,5,0,7,-1]
    print(insertion(arr))

"""We belive the first element of the array to be already sorted 
and then whenever we see an element smaller than the sorted element we insert the smaller one to the currect index and shift the already sorted elements rightwards"""
"Best case = O(n)" \
"worst case O(n**2)"
