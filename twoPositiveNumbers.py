def two_positives(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2

print(two_positives(2, 4, -3))  # Output: True
print(two_positives(-4, 6, 8))  # Output: True
print(two_positives(4, -6, 9))  # Output: True
print(two_positives(-4, 6, 0))  # Output: False
print(two_positives(4, 6, 10))  # Output: False
print(two_positives(-14, -3, -4))  # Output: False
