"""
Accounts Merge
"""
import collections

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, index):
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1, index2):
        self.parent[self.find(index2)] = self.find(index1)

class Solution:
    def accountsMerge(self, accounts):
        email2Index = {}
        email2Name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email2Index:
                    email2Index[email] = len(email2Index)
                    email2Name[email] = name

        uf = UnionFind(len(email2Index))
        for account in accounts:
            index1 = email2Index[account[1]]
            for email in account[2:]:
                index2 = email2Index[email]
                uf.union(index1, index2)

        index2Email = collections.defaultdict(list)
        for email, index in email2Index.items():
            index = uf.find(index)
            index2Email[index].append(email)

        res = []
        for emails in index2Email.values():
            res.append([email2Name[emails[0]]] + sorted(emails))
        return res
