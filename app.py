def reverse_string(string):
    return string[::-1]
print(reverse_string("hello"))

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
print(count_vowels("application"))

def sum_of_digits(number):
    return sum([int(digit) for digit in str(number)])
print(sum_of_digits(123))