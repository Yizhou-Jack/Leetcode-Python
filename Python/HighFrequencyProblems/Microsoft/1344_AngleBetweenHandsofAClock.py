class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourAngle = 360/12*(hour+minutes/60)
        minuteAngle = 360*(minutes/60)
        subRes = abs(hourAngle-minuteAngle)
        res = subRes if subRes <= 180 else 360-subRes
        return res