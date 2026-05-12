class TimeMap:

    vals: dict[list[tuple[str, int]]]

    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.vals:
            self.vals[key] = []

        self.vals[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.vals:
            return ""

        values = self.vals[key]
        print(values)

        if values[0][1] > timestamp:
            return ""

        if timestamp > values[-1][1]:
            return values[-1][0]

        l = 0
        r = len(values) - 1
        
        while l <= r:

            m = (l + r) // 2

            print(f"{l}-{m}-{r}")

            if (values[m][1] == timestamp):
                return values[m][0]
            elif (values[m][1] > timestamp):
                r = m - 1
            elif (values[m][1] < timestamp):
                l = m + 1

        return values[r][0]
