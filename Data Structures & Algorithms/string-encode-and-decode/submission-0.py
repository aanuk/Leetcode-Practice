class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Step 1: read digits until we hit '#'
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # the length of the next string

            # Step 2: jump past the '#', grab `length` characters
            start = j + 1
            end = start + length
            result.append(s[start:end])

            # Step 3: move i to right after this string
            i = end

        return result