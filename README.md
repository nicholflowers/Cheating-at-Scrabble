# 🔤 Cheating at Scrabble

**A Python program that finds every valid Scrabble word you can build from a rack, scores each one, and ranks the results, wildcards included.**

## 📌 Overview

This is the classic "what can I make from these tiles?" problem. Given a rack of two to seven letters, with optional wildcards, the program searches the official Scrabble word list, finds every word the rack can form, scores each by Scrabble letter values, and returns them ranked from highest scoring to lowest.

## 🎯 What It Does

- Finds all valid Scrabble words that can be built from a 2 to 7 letter rack
- Scores each word by official Scrabble letter values and ranks by score, then alphabetically
- Supports wildcards (`*` and `?`), each standing in for any letter and scored as zero
- Validates input and returns clear, helpful error messages instead of crashing

## 📋 Constraints

- **Standard library only:** no third-party packages
- **Wildcards:** at most two per rack (`*` and `?`), each scored as zero
- **Performance:** must return results for a rack with two wildcards in under 30 seconds
- **Error handling:** invalid input returns a clear message describing the problem. The program does not crash or surface a raw error trace.

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

### 🔹 Input Validation

- Accepts 2 to 7 characters: letters in any case, plus the wildcards `*` and `?`
- Rejects racks that are too short or long, contain invalid characters, or hold more than two wildcards, returning a specific message for each case rather than raising an exception

### 🔹 Word Matching

- Reads the SOWPODS word list once into memory
- For each candidate word, consumes letters from a copy of the rack to test whether the word can be formed
- Falls back to a wildcard (`*` or `?`) when a needed letter is not otherwise available in the rack

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

Python (standard library only)
