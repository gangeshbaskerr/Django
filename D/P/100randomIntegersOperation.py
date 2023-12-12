''' Generate 100 random integers in a given range and store them in a list.
Create a function that checks for primes in the list of random numbers and
returns a list of primes sorted in ascending order. Create another function
that returns a tuple of sum, mean and median of prime list elements.
Write a program to produce the output similar to the following interactive
user interface along with your name IN UPPER CASE, register no in parenthesis
and the current time stamp.'''


import random
import datetime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(random_list):
    return sorted([num for num in random_list if is_prime(num)])

def calculate_stats(primes):
    total = sum(primes)
    mean = total / len(primes)
    if len(primes) % 2 == 0:
        median = (primes[len(primes)//2 - 1] + primes[len(primes)//2]) / 2
    else:
        median = primes[len(primes)//2]
    return total, mean, median

def main():
    first_name = input("Enter First name (in lower case): ")
    last_name = input("Enter Last name (in lower case): ")
    reg_no = input("Enter register No: ")
    start_range = int(input("Enter start range: "))
    end_range = int(input("Enter end range: "))

    random_list = [random.randint(start_range, end_range) for _ in range(100)]
    primes = get_primes(random_list)
    stats = calculate_stats(primes)

    print("\nRandom List:", " ".join(map(str, random_list)))
    print("Sorted Primes List:", " ".join(map(str, primes)))
    print("Sum_mean_median:", " ".join(map(str, stats)))

    current_time = datetime.datetime.now().strftime("%B %d, %Y (%A) %I:%M %p")
    print("\nDone by", f"{first_name.upper()} {last_name.upper()} ({reg_no})")
    print("Time stamp:", current_time)

if __name__ == "__main__":
    main()

  
