#
# https://leetcode.com/problems/integer-to-roman/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'
        }

        vals = sorted(mapping.keys(), reverse = True)
        res = ''
        for i in vals:
            while num >= i:
                num -= i
                res += mapping[i]
        return res
