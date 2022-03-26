class DSA():


    def lsearch(seq,v):
        """LINEAR SEARCHING"""
        if seq==[]: print("No element in the list")
        for i in range(len(seq)):
            if seq[i]==v:
                return(True,i)
        return (False)

    def lin_sch_st(sting,chars):
        """Linear search in a String"""
        if len(sting)==0:
            return(False)
        for i in range(len(sting)):
            if chars==sting[i]:
                return(True,i)
        return(False)

    def minnum(seq):
        """This program gives the minimum number in the sequence of a number"""
        if len(seq)==0:
            return False
        min=seq[0]
        for i in seq:
            if i<min:
                min=i
        return min

    '''Binary search'''

def bsearch(seq,v,l,r):
    """ This is a binary sraech algorythem this will Search the number you want:: enter the v==number you want to find"""
    if r-l==0:
        return(False)
    mid=(l+r)//2
    if (seq[mid]==v):
        return(True,mid)
    if v<seq[mid]:
        return(bsearch(seq,v,l,mid))
    if v>seq[mid]:
        return bsearch(seq, v, mid + 1, r)


    """SORTING ALGO"""

    def bubble(arr):
        """Bubble sort"""
        for i in range(len(arr)-1,0,-1):
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr


    def selsort(seq):
        '''SELECTION SORTING'''
        """This will sort the sequence in assending order"""
        for start in range(len(seq)):
            minpos=start
            for i in range(start,len(seq)):
                if seq[i]<seq[minpos]:
                    minpos=i
            seq[start],seq[minpos]=seq[minpos],seq[start]
        return seq


    def insertion_sort(seq):
        '''Insertion sorting::'''
        '''This will sort the given seq by insertion sorting method'''
        for i in range(1,len(seq)):
            pos=i
            while pos>0 and seq[pos]<seq[pos-1]:
                seq[pos],seq[pos-1] = seq[pos-1],seq[pos]
                pos=pos-1
        return seq


if __name__ == '__main__':
    DSA.lsearch()