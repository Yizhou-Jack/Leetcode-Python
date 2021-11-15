"""
Decode the Slanted Ciphertext
"""

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText)//rows
        res = []
        for offset in range(cols):
            i = 0
            j = offset
            while i*cols+j < len(encodedText):
                res.append(encodedText[i*cols+j])
                i += 1
                j += 1
        return "".join(res).rstrip()