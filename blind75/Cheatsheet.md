# Python Input Patterns Cheat Sheet

Built-in funcs in Python:
len(arr)

sum(arr)

max(arr)

min(arr)

abs(-5)

round(3.14)

sorted(arr)

reversed(arr)

zip(a, b)

enumerate(arr)

---


int(input())

list(map(int, input().split()))

a, b = map(int, input().split())

for \_ in range(t):

enumerate()

zip()

input().strip()

## 1. Single Integer

```
n = int(input())
```

Input:

```text
5
```

---

## 2. Single Float

```
x = float(input())
```

Input:

```text
3.14
```

---

## 3. Single String

```
s = input()
```

Input:

```text
hello
```

---

## 4. Two Integers

```
a, b = map(int, input().split())
```

Input:

```text
10 20
```

---

## 5. Three Integers

```
a, b, c = map(int, input().split())
```

Input:

```text
1 2 3
```

---

## 6. List of Integers

```
arr = list(map(int, input().split()))
```

Input:

```text
1 2 3 4 5
```

Output:

```
[1, 2, 3, 4, 5]
```

---

## 7. List of Strings

```
words = input().split()
```

Input:

```text
apple banana mango
```

Output:

```
['apple', 'banana', 'mango']
```

---

## 8. Character Input

```
ch = input()
```

Input:

```text
a
```

---

## 9. Array with Size

```
n = int(input())
arr = list(map(int, input().split()))
```

Input:

```text
5
1 2 3 4 5
```

---

## 10. Multiple Test Cases

```
t = int(input())

for _ in range(t):
    n = int(input())
```

Input:

```text
3
10
20
30
```

---

## 11. Matrix Input

```
n = int(input())

matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
```

Input:

```text
3
1 2 3
4 5 6
7 8 9
```

---

## 12. Matrix Using List Comprehension

```
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
```

---

## 13. Fixed Rows and Columns

```
rows, cols = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(rows)]
```

Input:

```text
2 3
1 2 3
4 5 6
```

---

## 14. Read Entire Line

```
line = input().strip()
```

---

## 15. Read Digits as List

```
digits = list(map(int, input()))
```

Input:

```text
12345
```

Output:

```
[1, 2, 3, 4, 5]
```

---

## 16. Read String as Character List

```
chars = list(input())
```

Input:

```text
hello
```

Output:

```
['h', 'e', 'l', 'l', 'o']
```

---

## 17. Fast Input

```
import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
```

---

## 18. Dictionary Input

```
n = int(input())

d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = value
```

Input:

```text
3
a 1
b 2
c 3
```

---

## 19. Set Input

```
s = set(map(int, input().split()))
```

Input:

```text
1 2 2 3 3 4
```

Output:

```
{1, 2, 3, 4}
```

---

## 20. Coordinates

```
x, y = map(int, input().split())
```

Input:

```text
10 20
```

---

## 21. Nested Lists

```
n = int(input())

data = []

for _ in range(n):
    name = input()
    marks = float(input())

    data.append([name, marks])
```

---

## Most Important Patterns

```
int(input())

input()

map(int, input().split())

list(map(int, input().split()))

for _ in range(t):

matrix = [list(map(int, input().split())) for _ in range(n)]

input().strip()

enumerate(arr)

zip(a, b)
```
