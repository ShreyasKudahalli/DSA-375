# Word Break and Segmentation
Word Break and Segmentation problems focus on determining how a string can be divided into valid words or prefixes from a given dictionary. These problems often combine Dynamic Programming, Tries, and DFS to efficiently explore possible partitions while avoiding redundant computations. Common tasks include checking whether a string can be segmented, generating all valid sentences, replacing words using prefixes, or finding optimal decompositions. By leveraging prefix matching and memoization, word segmentation techniques efficiently solve a wide range of text processing, autocomplete, and natural language problems.


## 1️⃣ Replace Words

### 📌 Problem Statement

You are given:

* `dictionary[]` → a list of root words
* `sentence` → a sentence consisting of words separated by spaces

👉 Replace every word in the sentence with the **shortest root** from the dictionary that is a prefix of the word.

If no root matches, keep the original word unchanged.

👉 Return the modified sentence.

---

### 🚀 Approach: Trie + Prefix Search

#### 🔹 Key Idea

A **Trie (Prefix Tree)** is ideal for prefix matching.

1. Insert all root words into the Trie.
2. For each word in the sentence:

   * Traverse the Trie character by character.
   * As soon as a word-ending node is reached:

     * Return the current prefix.
3. If no prefix exists:

   * Return the original word.

Since we stop at the first valid root, we automatically obtain the **shortest matching root**.

---

### 🧠 Algorithm

1. Build a Trie using all dictionary roots.
2. Split the sentence into words.
3. For each word:

   * Search for the shortest root in the Trie.
   * Replace the word if a root exists.
4. Join all processed words back into a sentence.
5. Return the modified sentence.

---

### 📊 Complexity Analysis

| Type              | Complexity |
| ----------------- | ---------- |
| Trie Construction | O(T)       |
| Word Replacement  | O(S)       |
| Space Complexity  | O(T)       |

Where:

* `T` = total characters in the dictionary
* `S` = total characters in the sentence

---

### 📎 Example

```text id="example"
Input:

dictionary = ["cat","bat","rat"]

sentence =
"the cattle was rattled by the battery"
```

Output:

```text id="output"
"the cat was rat by the bat"
```

---

### 🔍 Dry Run

```text id="dryrun"
Dictionary:

cat
bat
rat

Word: "cattle"

c → a → t*

Root found: "cat"

Replace:

cattle → cat
```

---

### 🌳 Visualization

```text id="visual"
(root)
 ├── c
 │    └── a
 │         └── t*
 │
 ├── b
 │    └── a
 │         └── t*
 │
 └── r
      └── a
           └── t*

* = End of Root Word
```

Sentence transformation:

```text id="transform"
cattle  → cat
rattled → rat
battery → bat
```

---

### ✅ Key Points

* Trie enables efficient prefix matching.
* Stop traversal at the first word-ending node.
* Guarantees the shortest root replacement.
* Faster than checking every dictionary word for each sentence word.

---

### ⚠️ Edge Cases

* Empty dictionary
* No matching roots
* Multiple roots matching the same word
* Single-word sentence
* Root equal to the entire word

---

### 🏁 Conclusion

The Replace Words problem is a classic application of Tries for prefix searching. By storing dictionary roots in a Trie and stopping at the earliest valid prefix, the algorithm efficiently replaces words with their shortest matching roots while maintaining linear performance with respect to the input size.


---


## 2️⃣ Word Break

### 📌 Problem Statement

You are given:

* `s` → a string
* `wordDict[]` → a dictionary of valid words

👉 Determine whether the string can be segmented into a sequence of one or more dictionary words.

👉 A dictionary word may be reused multiple times.

👉 Return `True` if segmentation is possible, otherwise return `False`.

---

### 🚀 Approach: Trie + DFS + Memoization

#### 🔹 Key Idea

The problem asks whether the string can be partitioned into valid dictionary words.

To optimize prefix searching:

* Store all dictionary words in a **Trie**.

To avoid recomputing states:

* Use **memoization** on the starting index.

At every position:

* Traverse the Trie character by character.
* Whenever a valid word ends:

  * Recursively check the remaining substring.

---

### 🧠 Algorithm

1. Build a Trie from all dictionary words.
2. Define `dfs(start)`:

   * Determines whether `s[start:]` can be segmented.
3. If `start == n`:

   * Entire string is segmented successfully.
4. Traverse the Trie starting from index `start`.
5. Whenever a word ending is reached:

   * Recursively solve the remaining substring.
6. Store results in memoization map.
7. Return `dfs(0)`.

---

### 📊 Complexity Analysis

| Type              | Complexity |
| ----------------- | ---------- |
| Trie Construction | O(T)       |
| DFS + Memoization | O(n²)      |
| Space Complexity  | O(T + n)   |

Where:

* `T` = total characters in dictionary words
* `n` = length of string `s`

---

### 📎 Example

```text id="example"
Input:

s = "leetcode"

wordDict = ["leet","code"]

Output:
True
```

---

### 🔍 Dry Run

```text id="dryrun"
String:

leetcode

Start at index 0:

"leet" ✓

Remaining:

"code"

"code" ✓

Reached end of string.

Answer = True
```

---

### 🌳 Visualization

```text id="visual"
leetcode

leet | code
  ✓      ✓

Entire string segmented successfully.
```

Trie structure:

```text id="trie"
(root)
 ├── l → e → e → t*
 └── c → o → d → e*

* = End of Word
```

---

### ✅ Key Points

* Trie enables efficient prefix matching.
* DFS explores possible segmentations.
* Memoization avoids repeated computations.
* Dictionary words can be reused multiple times.

---

### ⚠️ Edge Cases

* Empty string
* Empty dictionary
* No valid segmentation
* Repeated word usage
* Overlapping prefixes

---

### 🏁 Conclusion

The Word Break problem combines Trie-based prefix searching with DFS and memoization to efficiently determine whether a string can be segmented into valid dictionary words. This approach avoids redundant work while enabling fast prefix checks, making it highly effective for large dictionaries and long strings.

