from django.shortcuts import render


def index(request):
    pairs = [(150, 290), (220, 284), (1184, 1210), (1350, 1851)]
    results = []

    for pair in pairs:
        result = are_amicable(pair[0], pair[1])
        results.append((pair, result))

    return render(request, 'index.html', {'results': results})


def proper_divisors(num):
    return [i for i in range(1, num) if num % i == 0]


def classify_number(num):
    divisors_sum = sum(proper_divisors(num))
    if divisors_sum == num:
        return "Perfect"
    elif divisors_sum < num:
        return "Deficient"
    else:
        return "Abundant"


def are_amicable(num1, num2):
    return sum(proper_divisors(num1)) == num2 and sum(proper_divisors(num2)) == num1


def proper_divisors_view(request, number):
    divisors = proper_divisors(number)
    return render(request, 'proper_divisors.html', {'number': number, 'divisors': divisors})






