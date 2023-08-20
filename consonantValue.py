def solve(lowercaseString):
    vowels = 'aeiou'
    max_value = 0
    current_value = 0

    for char in lowercaseString:
        if char not in vowels:
            current_value += ord(char) - ord('a') + 1
            max_value = max(max_value, current_value)
        else:
            current_value = 0

    return max_value

