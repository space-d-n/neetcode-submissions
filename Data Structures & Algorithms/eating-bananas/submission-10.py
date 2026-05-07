class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

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
            
