"""
https://leetcode.com/problems/reward-top-k-students
"""


def top_students(positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
    """"""

    from heapq import heappush, heappop
    from itertools import chain

    positive_feedback, negative_feedback = set(positive_feedback), set(negative_feedback)  # allow fast lookup

    points = []
    stud_id = {}
    count = 0

    for r, s_id in zip(report, student_id):

        point = 0
        for w in r.split():
            if w in positive_feedback:
                point += 3
            elif w in negative_feedback:
                point -= 1
        
        heappush(points, point)
        count += 1
        if count > k:
            heappop(points)
        
        stud_id[point] = chain(stud_id.get(point, []), [s_id])
    
    # print(points, stud_id)
    
    ans = []
    last = None
    
    while points:
        p = heappop(points)
        if p != last:
            ans.extend(sorted(stud_id[p], reverse=True))
            last = p
    
    return ans[::-1][:k]
