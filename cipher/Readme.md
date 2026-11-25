# Classical and Modern Ciphers - Caesar, RSA and Vigenère

A brief reference to three famous ciphers: the Caesar, the RSA and the Vigenère.

Table of Contents

- Caesar Cipher
- RSA Cipher
- Vigenère Cipher
- Quick Comparison

---

Caesar Cipher

A shift cipher which replaces each plaintext letter with a letter a fixed number of places down the alphabet. The shift length is the key.

- Encryption: C = (P + k) mod 26
- Decipher: P = ( C k) mod 26
- Example: with k=3, HELLO becomes KHOOR (HK, EH, LO, LO, OR).
- There are only 25 key patterns so "brute force" can break it immediately. Frequency analysis is also relatively straightforward.

---

RSA Cipher

$Asymmetric (public-key) algorithm. It employs a set of keys: a public key for encryption and a private key for decryption. Its security relies on the intractability of factoring the product of two large prime numbers.

# Key Generation

1. Select two very large primes, p and q.
2. Compute n = p × q.
3. Compute φ(n) = (p 1)(q 1).
4. Select e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1.
5. Calculate d such that d 1 e (mod φ(n)).

- Public key: (e, n)
- Private key: (d, n)
- Encryption: C = M^e mod n
- Decryption: M = C^d mod n

# Small Example

P = 3 q = 11 n = 33, φ = 20 Choose e = 3 then d = 7 (3 7 = 21 1 mod 20)

- Encrypting M = 4 gives C = 4³ mod 33 = 31.
- Decrypting gives 31⁷ mod 33 = 4.

# Strengths and Weaknesses

- Pro: Secure with large keys (2048 bits or larger) and you do not have to send a shared secret first.
- Weakness: It is slower than symmetric cipher and is usually used to exchange keys for symmetric encryption.

---

Vigenere Cipher

A polyalphabetic substitution cipher. Uses a keyword, each of whose characters makes a different Caesar shift for the matching character of the message. The keyword is repeated to be as long as the message.

- Encryption:Cᵢ = (Pᵢ + Kᵢ) mod 26
- Decryption: Pᵢ = (Cᵢ Kᵢ) mod 26



# Advantages and Disadvantages

- Strength: Better than Caesar at concealing letter frequency, because the same plaintext letter maps onto many different ciphertext symbols.
- Weakness: Still breakable by Kasiski analysis or the index of coincidence to determine the length, then attack each position separately as a Caesar cipher.

---

Quick Comparison

| Feature       | Caesar                      | Vigenère                    | RSA                         |
| ------------- | --------------------------- | --------------------------- | --------------------------- |
| **Type**      | Monoalphabetic substitution | Polyalphabetic substitution | Asymmetric public-key       |
| **Key**       | Single number               | Keyword                     | Public and private key pair |
| **Security**  | Very weak                   | Weak (large keys)           | Strong                      |
| **Use Today** | Educational                 | Educational                 | TLS, digital signatures     |
