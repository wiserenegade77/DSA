class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1) , len(str2)

        def isDivisor(l):
            if l1 % l or l2 % l:
                return False
            f1 , f2 = l1//l, l2//l
            return f1*str1[:l] == str1 and f2*str1[:l] == str2 

        # reverse iterating for shortest value 
        # time complexity min(n,m)*(n+m)
        for i in range(min(l1,l2),0,-1):
            if isDivisor(i):
                return str1[:i]
        return ""