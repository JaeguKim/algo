class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        minX = newInterval[0]; maxY = newInterval[1]
        idx = -1
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[1] and newInterval[1] <= intervals[i][1]:
                idx = i
                maxY = intervals[i][1]
                break
            elif newInterval[1] < intervals[i][0]:
                idx = i-1
                break
            else:
                idx = i
        
        idxToDelete = []
        print('idx : {}'.format(idx))
        for i in range(idx,-1,-1):
            if newInterval[0] < intervals[i][0]:
                idxToDelete.append(i)
            else:
                if intervals[i][0] <= newInterval[0] and newInterval[0] <= intervals[i][1]:
                    idxToDelete.append(i)
                    minX = intervals[i][0]
                break
        print('minX : {}, maxY : {}'.format(minX,maxY))
        startIdx = len(intervals)+1; endIdx = -1
        if len(idxToDelete) > 0:
            startIdx = idxToDelete[-1]; endIdx = idxToDelete[0]
        newList = []
        for i in range(len(intervals)):
            if startIdx <= i and i <= endIdx:
                continue
            else:
                newList.append(intervals[i])
        newList.append([minX,maxY])
        newList = sorted(newList,key=lambda x:x[0])
        return newList