class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list = []
        str =''
        for i in word1:
            list.append(i)
        index =1

        for m in word2:
            list.insert(index,m)
            index+=2

        for z in list:
            str += z

        return str