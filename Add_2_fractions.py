from math import gcd

def add_fractions(a, b, c, d):
 numerator = a * d + b * c
 denominator = b * d
 greatest_common_divisor = gcd(numerator, denominator)
 numerator //= greatest_common_divisor
 denominator //= greatest_common_divisor
 return numerator, denominator

arr = list(map(int, input().split()))
a, b, c, d = arr[0], arr[1], arr[2], arr[3]

result_numerator, result_denominator = add_fractions(a, b, c, d)

print(result_numerator,result_denominator)