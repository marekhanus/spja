def fizzbuzz(num):
    """
    Return 'Fizz' if `num` is divisible by 3, 'Buzz' if `num` is divisible by 5, 'FizzBuzz' if `num` is divisible both by 3 and 5.
    If `num` isn't divisible neither by 3 nor by 5, return `num`.
    Example:
        fizzbuzz(3) # Fizz
        fizzbuzz(5) # Buzz
        fizzbuzz(15) # FizzBuzz
        fizzbuzz(8) # 8
    """
    if (num % 3) == (num % 5) == 0:
        return 'FizzBuzz'
    elif (num % 3) == 0:
        return 'Fizz'
    elif (num % 5) == 0:
        return 'Buzz'
    else:
        return num
