# yandex-contest
Warm-up-2023

**Task A.Not at least on the segment**

```
Time limit: 1 second

Memory limit: 64Mb

Input: standard input or input.txt

Output: standard output or output.txt
```

A sequence of integers a1, a2, ..., an is given.
Queries are defined: to report any element of the sequence in the range from L to R, **inclusive**,
that is not equal to the minimum on this range.

**Input format:**
The first line contains two integers N, 1 ≤ N ≤ 100, and M, 1 ≤ M ≤ 1000 —
the length of the sequence and the number of queries, respectively.
The second line contains the sequence itself, 0 ≤ ai ≤ 1000.
Starting from the third line, M queries are listed, each consisting of the boundaries
of the range L and R, where L, R are array indices, numbered from zero.

**Output format:**
For each query, output in a separate line the answer — any element in the range [L, R],
except for the minimum. If such an element does not exist, output "NOT FOUND".

**Example**
Input:

10  5

1  1  1  2  2  2  3  3  3  10

0  1

0  3

3  4

7  9

3  7

Output:

NOT FOUND

2

NOT FOUND

10

3

*All test cases passed.*

*Time: 299ms*

*Memory: 28.32 Mb*

In the first line, we read two integers, n and m.
Here, n represents the length of the sequence, and m indicates the number of queries.
In the second line, we read the sequence itself. Then, we list m queries in the subsequent lines.
For each query, we output any element in the range [ L, R ], except for the minimum.
If such an element does not exist, we output "NOT FOUND".

**Task B.Add Two Fractions**

```
Time limit: 1 second

Memory limit: 64Mb

Input: standard input or input.txt

Output: standard output or output.txt
```

Given two rational fractions: a/b and c/d. Add them and represent the result as an irreducible fraction m/n.

**Input format:**
The program receives 4 natural numbers a, b, c, d as input, each of which is no larger than 100.

**Output format:**
The program should output two natural numbers m and n such that m/n=a/b+c/d and the fraction m/n is irreducible.

**Example**
Input:

1  2  1  2

Output:

1  1

*All test cases passed.*

*Time: 200ms*

*Memory: 28.31 Mb*

First, we import the gcd function from the math library.
Then, we create a function called add_fractions that takes the numerators and denominators of two fractions as input.
Inside the function, we compute the new numerator and denominator of the sum of the fractions in the variables numerator and denominator, respectively.
We then find the greatest common divisor of the numerator and denominator using the gcd function and divide both the numerator and denominator by the greatest common divisor. Finally, we return the simplified numerator and denominator.

Next, we read the input numbers into an array and assign each value to the variables a, b, c, and d.
We then call the add_fractions function, and the resulting numerator and denominator are printed to the screen.

**Task D.Anagrams?**

```
Time limit: 1 second

Memory limit: 64Mb

Input: standard input or input.txt

Output: standard output or output.txt
```

Given two strings, check if one string is an anagram of another. An anagram of a string is formed by rearranging the characters of the string.

**Input format:**

Each string consists of lowercase Latin letters and its length is at most 100000. The strings are given in separate lines.

**Output format:**

Print "YES" if one string is an anagram of another, otherwise print "NO".

**Example**
Input:

dusty

study

Output:

YES

*All test cases passed.*

*Time: 271ms*

*Memory: 31.40 Mb*

First, we define a function that takes 2 arrays of letters in each word. Then, we sort them. If 2 arrays are same, the function will return "Yes".
In other cases it will return "NO".

In input we separate each letter and append it in list. In output we print the function with our input words.

**Task G.The rabbit learns geometry**

```
Time limit: 4 seconds

Memory limit: 80Mb

Input: standard input or input.txt

Output: standard output or output.txt
```

The curious rabbits love exploring geometry as they hop around the garden beds. Our rabbit is no exception. Today, it decided to study a new shape: a square.

The rabbit dashes across a garden bed, which is a **grid of N × M cells**. Some of these cells contain carrots, while others do not.

Let's assist our inquisitive rabbit in finding **the side length of the largest square** that can be completely filled with carrots.

**Input format:**

The first line contains two natural numbers, N and M (where 1 ≤ N, M ≤ 1000). Following that, there are N lines, each with M numbers separated by spaces. A number is 0 if there's no carrot in the cell, or 1 if there is a carrot.

**Output format:**

Print a single number, representing the side length of the maximum square filled with carrots.

**Example**

Input:

4 5

0 0 0 1 0

0 1 1 1 0

0 0 1 1 0

1 0 1 0 0

Output:

2

*All test cases passed.*

*Time: 421ms*

*Memory: 43.04 Mb*

First, we create a matrix dp that will store the maximum side length of a square filled with carrots for each cell on the field.

Next, we fill the dp matrix as follows:

* If a cell contains a carrot, its maximum side length is 1.
    
* If a cell does not contain a carrot, its maximum side length is 0.
    
* If a cell contains a carrot and its neighbors also contain carrots, its maximum side length is the minimum of its neighbors' maximum side lengths + 1.

Finally, we find the maximum side length of a square in the dp matrix and output it. 🥕
