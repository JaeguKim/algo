class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n = len(startTime)
        res = 0
        for i in range(n):
            if queryTime>=startTime[i] and queryTime<=endTime[i]:
                res+=1
        return res

