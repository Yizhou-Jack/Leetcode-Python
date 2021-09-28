"""
Unique Email Addresses
"""
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            localName, domainName = email.split("@")
            localName = localName.split("+")[0]
            localName = "".join(localName.split("."))
            address = localName + "@" + domainName
            res.add(address)
        return len(res)
