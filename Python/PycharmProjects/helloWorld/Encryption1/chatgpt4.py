import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_random_characters():
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    numerical_characters = '0123456789'

    random_category = random.choice([upper_case, lower_case, special_characters, numerical_characters])
    return random.choice(random_category)

def get_prime_lists():
    prime_numbers = [2, 3, 5, 7, 11, 13]  # 6 prime numbers as specified
    return prime_numbers, list(reversed(prime_numbers))

def apply_formula(char, prime):
    result = ""

    for i in range(prime):
        if i < prime // 2:
            result += chr(ord(char) + i)
        else:
            result += chr(ord(char) - (i - prime // 2))

    result += generate_random_characters()

    return result

def main():
    user_input = input("Enter a phrase to apply the formula: ")
    ascending_primes, descending_primes = get_prime_lists()
    result = ""

    for char_index, char in enumerate(user_input):
        prime_index = char_index % len(ascending_primes)
        prime = ascending_primes[prime_index]

        result += apply_formula(char, prime)

    print("Result:", result)

if __name__ == "__main__":
    main()
