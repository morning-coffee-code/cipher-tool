# cipher-tool
# Cipher Tool — Encrypt, Decrypt & Crack

THIS IS A pure-Python, console-based encryption/decryption and cryptanalysis
tool. **No `tkinter`, no SQL/database, no files** — every key, message,
and history entry lives only in Python variables in RAM for the
duration of the program (**volatile memory**). The instant the
program exits, everything is gone — nothing is ever written to disk.

## Features

### 1. Encrypt / Decrypt
Choose from four ciphers:
- **Caesar** — classic fixed-shift substitution cipher
- **Vigenère** — keyword-based polyalphabetic cipher
- **Custom** — an original two-layer cipher built for this project
  (keyed substitution + columnar transposition), stronger than a
  single classic cipher against basic frequency analysis
- **RSA** — real public-key cryptography implemented from scratch
  using only `random`/`math` (prime generation, modular inverse,
  modular exponentiation) — no cryptography libraries used

### 2. Crack Unknown Cipher (the "wow factor")
Given ciphertext **with no key provided**, the tool cracks it automatically:
- **Caesar** — brute-forces all 26 shifts and scores each result using
  chi-squared letter-frequency analysis + common-word matching, then
  shows every attempt in a table with the winning shift highlighted
- **Vigenère** — estimates the key length using the Index of
  Coincidence, then cracks each column of the message independently
  as its own mini Caesar cipher, recovering the full keyword

### 3. Session History (in-memory only)
View every operation performed so far in the session. This list is
volatile — it exists only in RAM and disappears the moment you quit.

## How to run in VS Code
1. Open this folder in VS Code (`File > Open Folder...`)
2. Make sure Python 3 is installed — no `pip install` needed at all,
   this project uses only the standard library
3. Open `main.py`
4. Run it with the **Run ▶** button, or in a terminal:
   ```
   python main.py
   ```
5. Follow the on-screen menu

## Project structure
```
cipher_tool/
├── main.py                          # Console menu, ties everything together
├── ciphers/
│   ├── caesar.py                    # Caesar cipher encrypt/decrypt
│   ├── vigenere.py                  # Vigenère cipher encrypt/decrypt
│   ├── custom_cipher.py             # Original shift + transposition cipher
│   └── rsa_cipher.py                # RSA built from scratch
├── cryptanalysis/
│   ├── frequency_analysis.py        # English letter-frequency scoring
│   └── brute_force.py               # Caesar & Vigenère auto-cracking
└── README.md
```

## Why this fits an award-style project
- **Pure Python** — standard library only (`random`, `math`, `string`),
  zero external dependencies, zero setup for judges to worry about
  
- **No SQL/database, no camera/image analysis** — session data lives
  purely in memory, satisfying a "text-only, in-memory" constraint
  
- **Real cryptography concepts**: number theory (RSA), statistics
  (chi-squared test), and classic cipher design — strong material for
  a project report
  
- **Demoable live**: type a message, encrypt it, then feed the
  ciphertext into "Crack" mode and watch the tool recover the
  original message without ever being told the key

## Possible extensions
- Add a "known-plaintext attack" mode for the Custom cipher
- Support cracking messages with punctuation/numbers preserved
- Add a difficulty/scoring system that times how fast each cipher
  gets cracked, for a live "cipher battle" demo
