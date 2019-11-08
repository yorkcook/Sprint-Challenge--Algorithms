# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

This problem seems similar to the looking for a name in the phonebook example that we had during lecture. I would do the same type of binary search as that example, which would give it a runtime of O(log n). This means the length of time grows proportional to the growth of items to be searched.

We would split the building in half and drop an egg. If it doesn't break we repeat the process of splitting the floors but go with the half that is higher. If the egg does break then we would split the lower half of floors. Repeat the process until we find floor f.
