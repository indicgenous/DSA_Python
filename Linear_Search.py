class search():

    def lin_search(seq,tar):
        """LINEAR SEARCHING"""
        if seq == []: print("No element in the list")
        for i in range(len(seq)):
            if seq[i] == tar:
                return (True, i)
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

if __name__ == '__main__':
    arr=[34,56,7,2,1,4,8,9,0,45,3]
    target=3
    k=search.lin_search(arr,target)
    print(k)