# yandex-contest
Warm-up-2023
**Task 1.Not at least on the segment**

Time limit: 1 second
Memory limit: 64Mb
Input: standard input or input.txt
Output: standard output or output.txt

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
10 5

1 1 1 2 2 2 3 3 3 10

0 1

0 3

3 4

7 9

3 7
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
