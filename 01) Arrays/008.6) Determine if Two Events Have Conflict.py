"""
https://leetcode.com/problems/determine-if-two-events-have-conflict
"""


def have_conflict(event1: list[str], event2: list[str]) -> bool:
    """"""

    # 1) Optimal (Convert time to int and compare): TC = O(1); SC = O(1)
    # Parse time format to some integer interval first
    # How would you determine if two intervals overlap?

    """
    # Helper Function:
    def get_parsed(event: list[str]) -> list[str]: 
        return [h*60+m for h, m in [map(int, time.split(':')) for time in event]]
    
    # Convert time interval to integer interval:
    event1, event2 = get_parsed(event1), get_parsed(event2)
    # print(event1, event2)  #debugging
    
    # Compare:
    return min(event1, event2)[1] >= max(event1, event2)[0]
    """

    # 1.1) Turns out we can directly compare the string only:
    # https://leetcode.com/problems/determine-if-two-events-have-conflict/solutions/2734120/java-c-python-easy-1-liner-solutions

    return min(event1, event2)[1] >= max(event1, event2)[0]
