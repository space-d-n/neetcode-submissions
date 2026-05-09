class Solution:

    def encode(self, strs: List[str]) -> str:
        # example ["Hello","World"] -> "5.Hello<up_to_200>5.World"

        encoded = []
        for s in strs:
            padded = s.ljust(200)
            encoded.append(f"{len(s)}.{padded}")
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        i = 0
        next_dot = s.find('.')
        result = []
        
        while i < len(s) - 1:
            # find next from the i
            next_dot = s.find('.', i)
            next_len = int(s[i: next_dot])
            result.append(s[next_dot + 1: next_dot + 1 + next_len])
            i = next_dot + 201

        return result
        
