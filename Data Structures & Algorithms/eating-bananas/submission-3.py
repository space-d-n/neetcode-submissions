class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_pile = 0

        for pile in piles:
            if pile > max_pile:
                max_pile = pile

        l = 1
        r = max_pile
        min_k = max_pile

        while l <= r:

            m = (r + l) // 2

            mh = 0

            for pile in piles:
                mh += math.ceil(pile / m)

            if (mh > h):
                l = m + 1
            elif (mh <= h):
                r = m - 1
                if m < min_k:
                    min_k = m

        return min_k
            
