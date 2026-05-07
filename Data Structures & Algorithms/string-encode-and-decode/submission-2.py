class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []

        for s in strs:
            
            padded = s.ljust(200)
            
            # OR
            # buf = list(s[:100])
            # buf.extend(" " for _ in range(100 - len(buf)))
            # padded = "".join(buf)

            encoded.append(f"{len(s)}.{padded}")

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:

        strs = []
        i = 0
        next_dot = 0
        while i < len(s) - 1:
            next_dot = s.find('.', i)
            s_len = int(s[i:next_dot])
            strs.append(s[next_dot+1:next_dot+1+s_len])
            i = next_dot + 201

        return strs
