# scar-log: Learning Python in 2026

> A developer's honest diary of learning Python the hard way—without AI spoon-feeding, with actual struggle, and actual growth.

---

## The Context

Started March 16, 2026 knowing how to do basic math: `2 + 2`.

That was literally it.

By March 18, I'd built 4 working programs, understood loops, dictionaries, string slicing, and the actual mechanics of how code works.

This repo documents that journey. Not the polished version. The real one.

---

## What's Here

### Day 0: The Calculator Kid
**Time spent:** 5-6 hours
**What I built:**
- Simple calculator (basic if/elif)
- Temperature converter with loops
- Grade calculator with lists and averaging

**What I learned:**
- Variables and input/output
- Loops (for loops)
- Lists and `.append()`
- Conditionals that actually make sense

**The realization:** Code doesn't get faster the more you write it. Understanding does.

---

### Day 1: Three Hours and a Dictionary
**Time spent:** 3 hours
**What I built:**
- To-do list app with dictionaries
- Learned `.zip()` to pair lists
- Learned `del` to remove dictionary items

**What I learned:**
- Dictionaries (key-value pairs)
- Why `zip()` creates tuples
- Why dictionaries need hashable keys
- Difference between `.remove()` (lists) and `del` (dicts)

**The struggle:** Spent 45 minutes debugging why `.remove()` wasn't working on dictionaries. Learned it's the wrong tool entirely.

**The realization:** 3 hours for 30 lines isn't slow when you actually understand every line.

---

### Day 2: The Slow Grind
**Time spent:** 1 hour 8 minutes (but felt longer)
**What I built:**
- Number guessing game with while loops
- Random number generation
- Attempt counting

**What I learned:**
- `while` loops (the confusing version)
- `random.randint()`
- Loop flow and when conditions matter
- Why loop order matters (ask first, then check)

**The struggle:** While loops didn't click. Tried for loops first. Hit errors. Looked at someone's code. Finally understood the pattern.

**The realization:** 1 hour 8 minutes felt like failure until I realized I actually understood it. Speed doesn't matter when understanding is the goal.

---

### Day 3: The Pace Shift
**Time spent:** 47 minutes + 20 minutes
**What I built:**
- Smart calculator with loops (47 min)
- Palindrome checker with string slicing (20 min)

**What I learned:**
- How to structure loops based on user input (`while ask != "quit"`)
- String slicing: `[::-1]` and why it works
- The difference between struggling then understanding vs. copying then moving on

**The struggle:** Spent 25 minutes trying to figure out string reversal. Didn't get it. Read an explanation. Understood the mechanism. Built it clean in 20 minutes.

**The realization:** Struggle first, understand second = real learning. Struggle is the investment, not the failure.

---

### Day 4: Running on Empty
**Time spent:** ~10 minutes (incomplete)
**What I started:**
- Password strength checker

**The truth:** Exhausted. Pushed anyway. Got nowhere. Learning that forcing it doesn't work.

---

## The Code

All programs are in `/day-X/main.py` folders.

They're messy. They're not optimized. They're *real*.

Each one taught me something. Not from tutorials. From building, breaking, fixing, and understanding.

---

## The Real Numbers

| Day | Task | Time | Lines | Status |
|-----|------|------|-------|--------|
| 0 | 3 challenges | 5-6h | ~30 | ✅ Working |
| 1 | To-do app | 3h | ~30 | ✅ Working |
| 2 | Guessing game | 1h 8m | ~20 | ✅ Working |
| 3 | Calculator + Palindrome | 67m | ~40 | ✅ Working |
| 4 | Password checker | 10m | ~10 | 🔄 WIP |

**Pattern:** As understanding deepens, speed increases naturally. Not forced.

---

## What I Actually Learned

**Not just Python syntax:**
- How to read error messages
- How to debug my own code
- When to look things up vs. when to think it through
- That rest is part of learning
- That struggle before understanding = deep learning
- That speed comes from understanding, not from grinding

---

## The Learning Style

- **No spoon-feeding:** Asked for guidance, not code
- **Hunted for answers:** Used forums, documentation, Google
- **Understood before coding:** Read explanations, then implemented
- **Documented honestly:** Shared the struggle, not just wins
- **Rested when needed:** Knew when to stop, not when to push

---

## What's Next

- Day 4: Finish password checker
- Day 5+: More complex programs (file I/O, APIs, maybe data structures)
- Week 2: Start building the PDF extraction tool
- Month 2: Web scraping + API integration
- Month 3-4: Full project assembly

---

## The Meta Thing

This README is as much about *how* I'm learning as *what* I'm learning.

Because honestly? The speed of learning matters less than the depth.

A week from now, I'll look at this code and it'll feel obvious. But right now, it's everything.

---

*Last updated: March 18, 2026*

*"Three hours felt like wasting time until I realized I was actually learning. That changes everything."*

---

## Files

```
scar-log/
├── day-0/
│   ├── calculator.py
│   ├── temp_converter.py
│   └── grade_calculator.py
├── day-1/
│   └── todo_list.py
├── day-2/
│   └── guessing_game.py
├── day-3/
│   ├── calculator_loop.py
│   └── palindrome_checker.py
├── day-4/
│   └── password_checker.py (WIP)
└── README.md (this file)
```

---

**Follow along. This is real learning. Messy, slow, honest, and actually working.**