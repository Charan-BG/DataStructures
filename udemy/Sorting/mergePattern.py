"""
Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:
Input: intervals = [[2,5],[3,6],[9,11],[20,21]]
Output: [[2,6],[9,11],[20,21]]

Input: intervals = [[1,3],[3,9],[10,11]]
Output: [[1,9],[10,11]]
"""

def merge_interval(intervals):
    intervals.sort(key=lambda x:x[0])

    result= [intervals[0]]

    for start,end in intervals[1:]:
        last_end=result[-1][1]
        if start<=last_end:
            result[-1][1] = max(end,last_end)
        else:
            result.append([start,end])

    return result


intervals=[[2,5],[3,6],[9,15],[11,12],[16,18]]
intervals=[[2,5],[3,6],[9,15],[11,12],[16,18],[6,7]]
print(merge_interval(intervals))