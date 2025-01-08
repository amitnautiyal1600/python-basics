def is_prime(num):
    for digit in range(2, num):
        if num % digit == 0 :
            return False
    return True


print(is_prime(73))
print(is_prime(75))