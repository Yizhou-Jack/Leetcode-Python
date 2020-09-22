class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if len(IP.split(".")) == 4:
            ipSplit = IP.split(".")
            for segment in ipSplit:
                if segment.isdigit() and len(segment) > 0 and segment[0] != '0' and 0 <= int(segment) <= 255:
                    continue
                elif len(segment) == 1 and segment[0] == '0':
                    continue
                else:
                    return "Neither"
            return "IPv4"
        elif len(IP.split(":")) == 8:
            ipSplit = IP.split(":")
            for segment in ipSplit:
                sList = list(segment)
                for s in sList:
                    if s.isalpha() and s.upper() > 'F':
                        return "Neither"
                if len(segment) == 0 or len(segment) > 4:
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"

solution = Solution()
res = solution.validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334")
print(res)