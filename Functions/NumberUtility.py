import random
from typing import List

class NumberUtility:
    @staticmethod
    def sum_even_numbers(n: int, use_while: bool = False) -> int:
        if use_while:
            total, i = 0, 2
            while i <= n:
                total += i
                i += 2
            return total
        else:
            return sum(range(2, n + 1, 2))
    
    @staticmethod
    def generate_random_numbers(n: int, min_val: int = 1, max_val: int = 1000) -> List[int]:
        return [random.randint(min_val, max_val) for _ in range(n)]
    
    @staticmethod
    def generate_unique_random_numbers(n: int, min_val: int = 1, max_val: int = 1000) -> List[int]:
        if n > (max_val - min_val + 1):
            raise ValueError(f"Cannot generate {n} unique numbers in range {min_val}-{max_val}")
        return random.sample(range(min_val, max_val + 1), n)
    
    @staticmethod
    def select_random_numbers(n: int, x: int, min_val: int = 1, max_val: int = 1000) -> List[int]:
        if x > n:
            raise ValueError("Cannot select more numbers than available")
        original_list = NumberUtility.generate_unique_random_numbers(n, min_val, max_val)
        return random.sample(original_list, x)
