

debug = True
debug = False


from Interval import Interval   # hxl: comment out this line for submission

# hxl: Note: If the intervals line up on a loop (like 1 ~ 12 on the clock)...
#            Simple break down the cross-origin intervals into two halves upon origin,
#            and then merge them back at the end.

class Solution:
    
    # @param intervals, a list of sorted Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        
        if len(intervals) == 0:
            return [newInterval]
        
        r = []
        overlapWithNewInterval = Interval(newInterval.start, newInterval.end)
        didAddNewInterval = False
        
        for i in intervals:
            if (i.start < overlapWithNewInterval.start
                  and i.end < overlapWithNewInterval.start):
                r.append(i)
            elif (i.start < overlapWithNewInterval.start
                  and i.end >= overlapWithNewInterval.start
                  and i.end <= overlapWithNewInterval.end):
                overlapWithNewInterval.start = i.start 
            elif (i.start < overlapWithNewInterval.start
                  and i.end > overlapWithNewInterval.end):
                return intervals
            elif (i.start >= overlapWithNewInterval.start
                  and i.end <= overlapWithNewInterval.end):
                pass
            elif (i.start >= overlapWithNewInterval.start
                  and i.start <= overlapWithNewInterval.end
                  and i.end >= overlapWithNewInterval.end):
                overlapWithNewInterval.end = i.end
            else:   # hxl: i is after overlapWithNewInterval
                if didAddNewInterval == False:
                    r.append(overlapWithNewInterval)
                    didAddNewInterval = True
                r.append(i)
        
        # hxl: It's possible that the new interval is not added yet!
        if didAddNewInterval == False:
            r.append(overlapWithNewInterval)
            didAddNewInterval = True
        return r
    