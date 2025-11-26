def main():
    n = 5

    a, b = 0, 1
    sum_fib = 0

    for i in range(n):
        sum_fib += a
        a, b = b, a + b

    print("Sum of first", n, "Fibonacci numbers is:", sum_fib)


if __name__ == "__main__":
    main()