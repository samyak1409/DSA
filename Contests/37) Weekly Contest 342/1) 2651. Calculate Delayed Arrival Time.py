"""
https://leetcode.com/problems/calculate-delayed-arrival-time
"""


def find_delayed_arrival_time(arrival_time: int, delayed_time: int) -> int: return (arrival_time+delayed_time) % 24
