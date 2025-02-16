# Problem Statement
# Design an iterator to flatten a 2D vector. Implement the class Vector2D with the following methods:

# Vector2D(List[List[int]] vec): Initializes the object with a 2D vector vec.
# next() -> int: Returns the next element in the 2D vector.
# hasNext() -> bool: Returns True if there are still elements to iterate, otherwise False.
# You must implement the Vector2D class without fully flattening the 2D vector into a 1D list.
# Example vec = [[1,2], [3], [4,5,6]]
# output [1, 2, 3, 4, 5, 6]
from typing import List

class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.iterator = (num for row in vec for num in row)
        self.next_val = next(self.iterator, None)

    def next(self) -> int:
        if self.next_val is None:
            raise Exception("No more elements")
        value = self.next_val
        self.next_val = next(self.iterator, None)
        return value

    def hasNext(self) -> bool:
        return self.next_val is not None

