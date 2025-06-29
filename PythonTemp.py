import random
import string
import time
import math
import sys
import os
from datetime import datetime

# Utility functions
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def print_banner():
    print("=" * 50)
    print(" PythonTemp Utility Script ")
    print("=" * 50)

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def list_primes(limit):
    return [x for x in range(2, limit) if is_prime(x)]

def write_random_file(filename, lines=10):
    with open(filename, 'w') as f:
        for _ in range(lines):
            f.write(random_string(16) + '\n')

def read_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return
    with open(filename, 'r') as f:
        for line in f:
            print(line.strip())

def show_menu():
    print("1. Print current time")
    print("2. Calculate factorial")
    print("3. Fibonacci number")
    print("4. List primes")
    print("5. Write random file")
    print("6. Read file")
    print("7. Exit")

def main():
    print_banner()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            print("Current time:", current_time())
        elif choice == '2':
            n = int(input("Enter n: "))
            print(f"Factorial of {n} is {factorial(n)}")
        elif choice == '3':
            n = int(input("Enter n: "))
            print(f"Fibonacci number at position {n} is {fibonacci(n)}")
        elif choice == '4':
            limit = int(input("List primes up to: "))
            print(list_primes(limit))
        elif choice == '5':
            filename = input("Filename: ")
            lines = int(input("Number of lines: "))
            write_random_file(filename, lines)
            print(f"Wrote {lines} lines to {filename}")
        elif choice == '6':
            filename = input("Filename: ")
            read_file(filename)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
        print()
        time.sleep(1)

if __name__ == "__main__":
    main()
