class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        a = [0] * num_people
        k = 1   
        while candies != 0:
            for i in range(num_people):
                if candies < k:
                    a[i] += candies
                    candies = 0
                    break
                a[i] += k
                candies -= k
                k += 1   
        return (a)