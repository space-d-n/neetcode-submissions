class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_pile = max(piles)

        l = 1
        r = max_pile

        while l <= r:

            m = (r + l) // 2

            mh = 0

            for pile in piles:
                mh += math.ceil(pile / m)

            if (mh > h):
                l = m + 1
            elif (mh <= h):
                r = m - 1

        return l
            
