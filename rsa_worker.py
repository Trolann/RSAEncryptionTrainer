import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def generate_rsa_keys():
    primes = [i for i in range(2, 18) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
    p, q = random.sample(primes, 2)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    e = random.choice([3, 5, 7, 11, 13, 17])
    while gcd(e, phi_n) != 1:
        e = random.choice([3, 5, 7, 11, 13, 17])
    
    d = mod_inverse(e, phi_n)


    print(f"Given:\n- p = {p} (prime number)\n- q = {q} (prime number)\n- e = {e} (public exponent)\n")

    user_public_key = input("Enter the public key as a tuple in the format (e, n): ")
    user_private_key = input("Enter the private key as a tuple in the format (d, n): ")

    try:
        user_e, user_n = map(int, user_public_key.strip('()').split(','))
        user_d, user_n_private = map(int, user_private_key.strip('()').split(','))

        if user_e == e and user_n == n:
            print("Public key is correct!")
        else:
            print(f"Public key is incorrect. The correct public key is ({e}, {n}).\n")

        if user_d == d and user_n_private == n:
            print("Private key is correct!")
        else:
            print(f"Private key is incorrect. The correct private key is ({d}, {n}).\n")

    except (ValueError, TypeError):
        print("Invalid input format. Please enter the keys as tuples in the specified format.")

    print("\nStep-by-step solution:")
    print("Step 1: Calculate modulus n = p × q")
    print(f"n = {p} × {q} = {n}\n")

    print("Step 2: Calculate φ(n) = (p - 1) × (q - 1)")
    print(f"φ(n) = ({p} - 1) × ({q} - 1) = {phi_n}\n")

    print("Step 3: Verify that e and φ(n) are coprime")
    if gcd(e, phi_n) == 1:
        print(f"gcd({e}, {phi_n}) = 1, so e and φ(n) are coprime.\n")
    else:
        print(f"gcd({e}, {phi_n}) != 1, so e and φ(n) are not coprime. Choose a different value for e.\n")

    print("Step 4: Calculate d such that ed = 1 mod φ(n)")
    print(f"{e} × d = 1 (mod {phi_n})")
    print(f"{e} × {d} = {e*d} = 1 (mod {phi_n})\n")

    print("Therefore, the public and private keys are:")
    print(f"Public key: (e, n) = ({e}, {n})")
    print(f"Private key: (d, n) = ({d}, {n})")

generate_rsa_keys()