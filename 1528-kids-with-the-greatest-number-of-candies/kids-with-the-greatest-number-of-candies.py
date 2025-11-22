class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        fin_list = []

        for i in candies:
            if i+extraCandies >= max_num:
                fin_list.append(True)
            else:
                fin_list.append(False)

        return fin_list