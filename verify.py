from sympy import isprime, totient


def main() -> None:
    n = 6_148_888_817
    steps = 0

    while not isprime(n):
        n = int(totient(n)) + 1
        steps += 1

    print(steps, n)

    if (steps, n) != (68, 9_500_401):
        raise RuntimeError(
            f"Unexpected result: expected (68, 9500401), got ({steps}, {n})"
        )


if __name__ == "__main__":
    main()
