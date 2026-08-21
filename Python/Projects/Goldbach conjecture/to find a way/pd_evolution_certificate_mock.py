PD = []

EN = 2
ien = 2
LIMIT = 101
ns = False
pairs = False
pair = 0


def np(x):
    x = int(x)
    if x not in PD:
        print(f"Adding new prime {x} in PD...")
        PD.append(x)
        PD.sort()
        print(f"PD = {PD}")


def pd_certificate(n):
    if n < 2:
        return False, None

    for prime in PD:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False, prime

    return True, None


def original_style_en(current_ien):
    if current_ien < 3:
        return 2
    return current_ien if current_ien % 2 == 1 else current_ien - 1


def original_style_pair(current_ien, _en):
    if pairs:
        return pair
    return _en


def formula_pair(current_ien, _en):
    f = current_ien + 1 if current_ien % 2 == 0 else current_ien
    np1 = original_style_pair(current_ien, _en)
    np2 = f - np1
    return f, np1, np2


print("Mock of how the original file could look if a certificate gate were inserted.")
print("This version follows the original state-machine rhythm and prints a formula-driven pair step.")

while ien < LIMIT:
    print("=========================")
    print(f"Next ien = {ien}")
    print(f"Current PD = {PD}")

    if PD == []:
        print("No primes found yet. Adding Exceptional number (2).")
        np(2)
        ien += 1
        continue

    _en = original_style_en(ien)
    print(f"_en = {ien} -> {_en}")
    print("Formula:")
    print(f"  _en is derived from ien using the original ending rule")
    print(f"  certificate rule: _en survives only if no prime in PD divides it up to sqrt(_en)")

    f, np1, np2 = formula_pair(ien, _en)
    print("Pair formula:")
    print(f"  f = {ien} + 1 if {ien} is even, otherwise f = {ien}")
    print(f"  np1 = {np1}")
    print(f"  np2 = f - np1 = {f} - {np1} = {np2}")
    print(f"  pair check: {f} = {np1} + {np2}")

    certified, divisor = pd_certificate(_en)
    if certified:
        print(f"Certificate: {_en} survives")
        np(_en)
    else:
        print(f"Certificate: {_en} fails")
        print(f"Blocking divisor = {divisor}")
        print(f"Preview: {_en} = {divisor} * {_en // divisor}")

    print()

    ns = False
    pairs = False
    pair = 0
    ien += 2


print(f"Final PD = {PD}")
print("Mock complete. In the real file, the certificate would sit right before each np(...) call.")