# 🔤 Cheating at Scrabble

**A Python program that identifies every valid Scrabble word within a rack, including those formed with wildcards, and returns them scored and ranked.**

## 📌 Overview

In Scrabble, players construct words from a rack of letter tiles, with each word scoring points according to the value of its tiles. A Scrabble cheater automates the search for the optimal play. Rather than relying on what a player can recall, it evaluates the entire official Scrabble dictionary against a given rack and returns every valid word, scored and ranked from highest to lowest.

## 🎯 The Challenge

Matching words to a rack is simple when every tile is a fixed letter. A few things make it harder:

- **Wildcards multiply the possibilities:** a wildcard can stand in for any letter, and a rack can hold two, which sharply increases the number of words to check
- **Scoring has to be deliberate:** a wildcard scores zero, so when a word can be made with or without one, the version built from real letters (the higher score) is the one that should be returned
- **Performance matters:** the program must return results in under 30 seconds even when the rack holds two wildcards

## 📋 Constraints

- **Standard Python library only:** no third-party packages

## 🗂️ Data

| Source | Description |
| --- | --- |
| SOWPODS word list (`sowpods.txt`) | The official list of valid Scrabble English words, one per line, kept in the repository so the program runs standalone. |

## 🗃️ Files

| File | Description |
| --- | --- |
| `scrabble.py` | The main program. `run_scrabble` finds every valid word in the rack, scores it, and ranks the results. |
| `wordscore.py` | Holds `score_word`, which returns the Scrabble score for a given word. |

## 🚀 Implementation Details

The program reads the official Scrabble word list, tests every word against the rack by consuming its letters (so a wildcard can stand in for any missing letter), then scores the matches and sorts them by score and alphabetically. Each step is detailed below.

### 🔹 Input Validation

- Accepts 2 to 7 characters: letters in any case, plus the wildcards `*` and `?`
- Rejects racks that are too short or long, contain invalid characters, or hold more than two wildcards, returning a specific message for each case rather than raising an exception

### 🔹 Word Matching

- Reads the SOWPODS word list once into memory
- Tests each word by consuming letters from a copy of the rack, rather than a simpler letter-count check, so that wildcards can stand in for any letter
- Spends a wildcard only when a needed letter is not already in the rack. Because a word spelled with real letters keeps its full score while wildcards count zero, this returns the higher-scoring version when a word can be formed either way

### 🔹 Scoring

- Delegates scoring to a separate `wordscore.py` module through an imported `score_word` function, keeping the scoring logic modular and reusable
- Applies standard Scrabble letter values; letters supplied by a wildcard score zero

### 🔹 Output

- Returns `(score, word)` tuples sorted by score descending, then alphabetically, all in uppercase, along with the total count of valid words

## 🧠 Skills Demonstrated

- **Algorithm design:** a letter-consumption matching routine that treats wildcards as any-letter substitutions
- **Modular code:** separating scoring into an imported module to keep responsibilities clean
- **Input validation:** returning helpful, specific error messages instead of raising exceptions
- **Python fundamentals:** file I/O, string processing, and custom-key sorting, written to PEP 8

## 🧰 Stack

Python.
