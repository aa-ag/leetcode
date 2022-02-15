from tracemalloc import start
from typing import List


def fizzBuzz(n: int) -> List[str]:
    answer = list()

    for i in range(1, n + 1):
        if i % 3 == 0:
            answer.append("Fizz")
        else:
            answer.append(i)
    return answer
        

print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))