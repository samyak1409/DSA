"""
https://leetcode.com/problems/frequency-tracker
"""


from collections import Counter


class FrequencyTracker:
    """"""

    # Put all the numbers in a hash map (or just an integer array given the number range is small) to maintain each
    # number’s frequency dynamically.
    # Put each frequency in another hash map (or just an integer array given the range is small, note there are only
    # 200000 calls in total) to maintain each kind of frequency dynamically.
    # Keep the 2 hash maps in sync.

    # 1) Optimal (2 HashMaps: for numbers and frequencies): TC = O(1); SC = O(n)

    """
    def __init__(self):
        # First of all we need 2 hashmaps to track, and lookup the frequencies in O(1):
        self.freq_of_num: Counter[int] = Counter()  # tracks freq of numbers
        self.freq_of_freq: Counter[int] = Counter()  # tracks freq of frequencies

    def add(self, number: int) -> None:
        # 1) For decreasing curr freq of freq-of-num (as we're adding one more num):
        # Get current freq of this num:
        freq = self.freq_of_num[number]
        # Only if freq of freq is there, else it'll go in -ve:
        if self.freq_of_freq[freq]:
            # Decrease the freq of freq:
            self.freq_of_freq[freq] -= 1
        # 2) Increase the freq of num:
        self.freq_of_num[number] += 1
        # 3) For increasing new freq of freq-of-num:
        # Get new freq of this num:
        freq = self.freq_of_num[number]
        # Increase freq of freq:
        self.freq_of_freq[freq] += 1

    def deleteOne(self, number: int) -> None:
        # Only if freq of num is there, else it'll go in -ve (as "data structure may not contain number", so if we
        # decreased w/o checking freq, then in the future if num is added, it's freq will be(come) 0 instead of 1):
        if self.freq_of_num[number]:
            # 1) For decreasing curr freq of freq-of-num (as we're deleting one num):
            # Get current freq of this num:
            freq = self.freq_of_num[number]
            # (No need of checking if the freq of freq is there or not as we've already checked above that freq of num
            # is there, hence freq of freq would also be.)
            # Decrease the freq of freq:
            self.freq_of_freq[freq] -= 1
            # 2) Decrease the freq of num:
            self.freq_of_num[number] -= 1
            # 3) For increasing new freq of freq-of-num:
            # Get new freq of this num:
            freq = self.freq_of_num[number]
            # Increase freq of freq:
            self.freq_of_freq[freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        # Just return True if freq is there (> 0) else False:
        return bool(self.freq_of_freq[frequency])
    """

    # Note: In `add`, `if self.freq_of_freq[freq]:` is not required. Think why.
    # Because, freq of freq will only not be there in case where num is occurring first time, and if num is occurring
    # first time then we'll have its freq of freq = 0. And see the constraint "1 <= frequency <= 10^5".

    # In short:

    def __init__(self):
        # First of all we need 2 hashmaps to track, and lookup the frequencies in O(1):
        self.freq_of_num: Counter[int] = Counter()  # tracks freq of numbers
        self.freq_of_freq: Counter[int] = Counter()  # tracks freq of frequencies

    def add(self, number: int) -> None:
        # Decrease curr freq of freq-of-num (as we're adding one more num):
        self.freq_of_freq[self.freq_of_num[number]] -= 1
        # Increase the freq of num:
        self.freq_of_num[number] += 1
        # Increase new freq of freq-of-num:
        self.freq_of_freq[self.freq_of_num[number]] += 1

    def deleteOne(self, number: int) -> None:
        # Only if freq of num is there, else it'll go in -ve (as "data structure may not contain number", so if we
        # decreased w/o checking freq, then in the future if num is added, it's freq will be(come) 0 instead of 1):
        if self.freq_of_num[number]:
            # Decrease curr freq of freq-of-num (as we're deleting one num):
            self.freq_of_freq[self.freq_of_num[number]] -= 1
            # Decrease the freq of num:
            self.freq_of_num[number] -= 1
            # Increase new freq of freq-of-num:
            self.freq_of_freq[self.freq_of_num[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        # Just return True if freq is there (> 0) else False:
        return bool(self.freq_of_freq[frequency])


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
