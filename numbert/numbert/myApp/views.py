from django.shortcuts import render


def proper_divisors(request, number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return render(request, 'result.html', {'title': 'Proper Divisors', 'result': divisors})

def classify_numbers(request, start, end):
    numbers_range = range(start, end + 1)
    result = {
        'perfect_numbers': [num for num in numbers_range if sum([i for i in range(1, num) if num % i == 0]) == num],
        'deficient_numbers': [num for num in numbers_range if sum([i for i in range(1, num) if num % i == 0]) < num],
        'abundant_numbers': [num for num in numbers_range if sum([i for i in range(1, num) if num % i == 0]) > num]
    }
    values=list(result.values())
    return render(request, 'result.html', {'title': 'Number Classification', 'result':values})