PD = []

EN = 2
LIMIT = 101


def smallest_divisor(n):
    if n % 2 == 0:
        return 2 if n != 2 else n
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n


def pd_certificate(n):
    if n < 2:
        return False, None

    for prime in PD:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False, prime

    return True, None


def np(x):
    x = int(x)
    if x not in PD:
        print(f"\n Adding new prime   {x}   in PD...")
        PD.append(x)
        PD.sort()
        print(f"\nPD = {PD}\n")


print("\nPrime extractor copy based on the original file.\n")
print("This version keeps the PD list but lets PD itself certify what can join it.\n")

for candidate in range(2, LIMIT + 1):
    print(f"=========================\nCandidate = {candidate}\nCurrent PD = {PD}\n")

    if candidate == 2:
        print("2 is the seed prime. PD certifies it as the first anchor.")
        np(candidate)
        continue

    certified, divisor = pd_certificate(candidate)

    if certified:
        print(f"{candidate} survives the PD certificate. Adding it to PD.")
        np(candidate)
    else:
        divisor = divisor if divisor is not None else smallest_divisor(candidate)
        print(f"{candidate} does not survive the PD certificate.")
        print(f"Blocking divisor found = {divisor}")
        print(f"Factorization preview: {candidate} = {divisor} * {candidate // divisor}")

print(f"\nFinal prime list extracted into PD = {PD}\n")