"""
https://leetcode.com/problems/reward-top-k-students
"""


def top_students(positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int],
                 k: int) -> list[int]:
    """"""

    # 1) Optimal (Smartly use tuple to achieve required sort order): TC = O(n*log(n)); SC = O(n)
    # Hash the positive and negative feedback words separately.
    # Calculate the points for each student’s feedback.
    # Sort the students accordingly to find the top k among them.
    # https://leetcode.com/problems/reward-top-k-students/solutions/2946490/python-use-set-for-fast-access
    # https://leetcode.com/problems/reward-top-k-students/solutions/2947200/tedious

    # 1.-1) WA because: "In case more than one student has the same points, the one with the lower ID ranks higher."
    # `dict` preserves the insertion order even then it's WA because `student_id` isn't sorted at the first place.
    """
    positive_feedback, negative_feedback = set(positive_feedback), set(negative_feedback)  # allow fast lookup

    points = {}
    for report_str, s_id in zip(report, student_id):
        '''
        point = 0
        for word in report_str.split():
            if word in positive_feedback:
                point += 3
            elif word in negative_feedback:
                point -= 1
        points[s_id] = point
        '''
        # One-liner:
        points[s_id] = sum(3*(word in positive_feedback)-1*(word in negative_feedback) for word in report_str.split())
    # print(points)  #debugging

    # print(sorted(points, key=lambda id_: points[id_], reverse=True))  #debugging
    return sorted(points, key=lambda id_: points[id_], reverse=True)[:k]
    """

    # 1.0) To fix this, we can use sorted dict instead of normal dict:
    """
    from sortedcontainers import SortedDict

    positive_feedback, negative_feedback = set(positive_feedback), set(negative_feedback)  # allow fast lookup

    points = SortedDict()
    for report_str, s_id in zip(report, student_id):
        '''
        point = 0
        for word in report_str.split():
            if word in positive_feedback:
                point += 3
            elif word in negative_feedback:
                point -= 1
        points[s_id] = point
        '''
        # One-liner:
        points[s_id] = sum(3*(word in positive_feedback)-1*(word in negative_feedback) for word in report_str.split())
    # print(points)  #debugging

    # print(sorted(points, key=lambda id_: points[id_], reverse=True))  #debugging
    return sorted(points, key=lambda id_: points[id_], reverse=True)[:k]
    """

    # 1.1) Better: Smartly use tuple to achieve required sort order:
    """
    positive_feedback, negative_feedback = set(positive_feedback), set(negative_feedback)  # allow fast lookup

    points = {}
    for report_str, s_id in zip(report, student_id):
        '''
        point = 0
        for word in report_str.split():
            if word in positive_feedback:
                point += 3
            elif word in negative_feedback:
                point -= 1
        points[s_id] = point
        '''
        # One-liner:
        points[s_id] = sum(3*(word in positive_feedback)-1*(word in negative_feedback) for word in report_str.split())
    # print(points)  #debugging

    # print(sorted(points, key=lambda id_: (-points[id_], id_)))  #debugging
    return sorted(points, key=lambda id_: (-points[id_], id_))[:k]
    """

    # 1.2) Turns out that we don't need dict:

    positive_feedback, negative_feedback = set(positive_feedback), set(negative_feedback)  # allow fast lookup

    points = []
    for report_str, s_id in zip(report, student_id):
        '''
        point = 0
        for word in report_str.split():
            if word in positive_feedback:
                point += 3
            elif word in negative_feedback:
                point -= 1
        points.append((-point, s_id))
        '''
        # One-liner:
        points.append((-sum(3*(word in positive_feedback)-1*(word in negative_feedback) for word in report_str.split()),
                       s_id))
    # print(points)  #debugging

    # print([s_id for _, s_id in sorted(points)])  #debugging
    return [s_id for _, s_id in sorted(points)[:k]]
