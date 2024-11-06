'''
Generators are a powerful feature in Python that allow you to create iterators in a more concise and memory-efficient way compared to traditional iterators
1. Large Data Processing: When working with large datasets that cannot fit entirely into memory, generators allow you to process data in chunks, yielding results one at a time. This reduces memory usage and improves performance.

2. Infinite Sequences: Generators can be used to create sequences of infinite length. This is useful for tasks such as generating prime numbers, Fibonacci sequences, or iterating through all possible combinations.

3. Lazy Evaluation: Generators enable lazy evaluation, meaning that values are computed only when needed. This is especially useful when dealing with expensive or time-consuming computations.


'''


def fab(num):
    start, next = 0,1
    while next <= num:
        yield(start)
        start, next = next, start+next
    

result = fab(50)

print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))


# or

print(type(result)) #<class 'generator'>

for i in range(7):
    print(next(result))

'''
result

<generator object fab at 0x7b1c90729700>
0
1
1
2
3
5
8
13
21
Traceback (most recent call last):
  File "<main.py>", line 20, in <module>
StopIteration

'''