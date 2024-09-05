# RSA Key Generator for Information Security Course

This Python script is designed for a university-level information security class to help students practice and understand the RSA algorithm. It generates small-scale RSA public and private keys using common prime numbers and values typically seen in exam questions.

## Purpose

- Educational tool for understanding RSA key generation
- Practice with manual calculations using exam-style numbers
- Step-by-step breakdown of the RSA algorithm process

## Features

- Uses small, "common sense" prime numbers (between 2 and 17) often found in exam questions
- Calculates public and private keys using simplified values
- Allows user input to check understanding and practice manual calculations
- Provides a detailed step-by-step solution for verification

## Usage

1. Run the script:
   ```
   python rsa_key_generator.py
   ```

2. The script will display given values for p, q, and e. These will be small primes and common public exponents you might encounter in exam questions.

3. Calculate the public key (e, n) manually and enter it when prompted.

4. Calculate the private key (d, n) manually and enter it when prompted.

5. The script will check your answers and provide feedback.

6. A step-by-step solution will be displayed, showing the calculations for n, φ(n), and d.

## Example Output

```
Given:
- p = 11 (prime number)
- q = 13 (prime number)
- e = 7 (public exponent)

Enter the public key as a tuple in the format (e, n): (7, 143)
Enter the private key as a tuple in the format (d, n): (103, 143)
Public key is correct!
Private key is correct!

Step-by-step solution:
Step 1: Calculate modulus n = p × q
n = 11 × 13 = 143

Step 2: Calculate φ(n) = (p - 1) × (q - 1)
φ(n) = (11 - 1) × (13 - 1) = 120

Step 3: Verify that e and φ(n) are coprime
gcd(7, 120) = 1, so e and φ(n) are coprime.

Step 4: Calculate d such that ed = 1 mod φ(n)
7 × d = 1 (mod 120)
7 × 103 = 721 = 1 (mod 120)

Therefore, the public and private keys are:
Public key: (e, n) = (7, 143)
Private key: (d, n) = (103, 143)
```

## Important Note

This script intentionally uses small prime numbers and simplified values for educational purposes. These are the types of numbers you might encounter in exam questions or homework problems. In real-world applications, much larger prime numbers are used to ensure security. This tool is designed for learning and exam preparation, not for generating secure keys for actual use.

## License

This project is open source and available under the [MIT License](LICENSE).
