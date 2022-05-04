"""
trick: zeroTo20, tens -> dont write "" as the first element firstly
trick: "Hundred" instead of " Hundred " first

on the top of my mind is that the number cou be large,
we are going to have result like forty three billion forty two million
the number before the billion and the million can be resolved in a similar way
so we should have a helper function to translate the number before the (thousand, million, billion)

and in the helper function, we are always going to have numbers less than one thousand
we could have some number Hundred and forty/sixty one/fourteen
"""

class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        zeroTo20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve",
                    "Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands = ["","Thousand","Million","Billion"]

        def helper(num):
            res = ""
            if num < 20:
                res = zeroTo20[num] + " "
            elif num < 100:
                res = tens[num//10] + " " + helper(num%10)
            elif num >= 100:
                res = zeroTo20[num//100] + " Hundred " + helper(num%100)
            return res

        res = ""
        for i in range(len(thousands)):
            if num%1000 != 0:
                res = helper(num%1000) + thousands[i] + " " + res
            num //= 1000
        return res.strip()