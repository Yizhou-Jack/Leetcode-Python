def solution(digits):
    n = len(digits)
    candidate = []
    for i in range(n):
        candidate.append(digits[i])
        candidate.append("")
    # candidate: ["1", "", "2", "", "3", "", "4", "", "5", "", "6", ""]
    res = []

    def checkValidIp(candidate):
        nonlocal res
        ip = "".join(candidate)
        ipSplitList = ip.split(".")
        flag = True
        for i in range(4):
            if int(ipSplitList[i]) > 255 or (len(ipSplitList[i]) > 1 and ipSplitList[i][0] == "0"):
                flag = False
                break
        if flag:
            res.append("".join(candidate))

    def helper(digits, candidate, track, index):
        if len(track) == 3:
            checkValidIp(candidate)
            return
        for i in range(index, len(digits)-1):
            track.append(i*2+1)
            candidate[i*2+1] = "."
            helper(digits, candidate, track, i+1)
            candidate[i*2+1] = ""
            track.pop()

    helper(digits, candidate, [], 0)
    return res

digits = "123456"
res = solution(digits)
print(res)