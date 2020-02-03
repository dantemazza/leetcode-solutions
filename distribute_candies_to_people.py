class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        n = 1
        res = [0 for x in range(num_people)]
        while True:
            for i in range(num_people):
                if n < candies:     
                    res[i] += n 
                    candies -= n
                    n += 1
                else:
                    res[i] += candies
                    return res
                
           
        
