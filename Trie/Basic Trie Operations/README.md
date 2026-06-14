# Basic Trie Operations

Basic Trie Operations form the foundation of efficient string processing and prefix-based searching. A Trie (Prefix Tree) stores characters in a hierarchical structure where common prefixes are shared among multiple words, enabling fast insertion, exact word lookup, and prefix matching. Core operations such as **Insert**, **Search**, and **StartsWith** typically run in linear time with respect to the length of the input string, making Tries particularly useful for dictionaries, autocomplete systems, spell checkers, word search problems, and various advanced string-matching applications.


## 1️⃣ Implement Trie (Prefix Tree)

### 📌 Problem Statement

Design a **Trie (Prefix Tree)** that supports the following operations:

* `insert(word)` → Inserts a word into the Trie.
* `search(word)` → Returns `True` if the exact word exists.
* `startsWith(prefix)` → Returns `True` if any word starts with the given prefix.

👉 Implement all operations efficiently.

---

### 🚀 Approach: Trie Data Structure

#### 🔹 Key Idea

A Trie stores words character by character in a tree-like structure.

Each node contains:

* `children` → mapping from character to next node
* `flag` → indicates whether a complete word ends at this node

Benefits:

* Fast word insertion
* Fast exact search
* Fast prefix search

---

### 🧠 Algorithm

#### Insert

1. Start from the root.
2. For each character:

   * Create a child node if it doesn't exist.
   * Move to the child node.
3. Mark the final node as the end of a word.

#### Search

1. Start from the root.
2. Traverse every character.
3. If any character is missing:

   * Return `False`
4. After traversal:

   * Return whether the final node is marked as a complete word.

#### startsWith

1. Start from the root.
2. Traverse every character of the prefix.
3. If any character is missing:

   * Return `False`
4. Otherwise:

   * Return `True`

---

### 📊 Complexity Analysis

| Operation  | Complexity |
| ---------- | ---------- |
| insert     | O(L)       |
| search     | O(L)       |
| startsWith | O(L)       |

Where:

* `L` = length of the word or prefix

---

### 📎 Example

```text id="example"
Operations:

insert("apple")

search("apple")
search("app")

startsWith("app")

insert("app")

search("app")
```

Output:

```text id="output"
True
False
True
True
```

---

### 🔍 Dry Run

```text id="dryrun"
Insert "apple"

root
 └── a
      └── p
           └── p
                └── l
                     └── e*

search("apple")

Path exists
Word end found

Result = True

search("app")

Path exists
Word end not found

Result = False

insert("app")

Mark second 'p' as word end

search("app")

Result = True
```

---

### 🌳 Visualization

```text id="visual"
(root)
  |
  a
  |
  p*
  |
  p
  |
  l
  |
  e*

* = End of Word
```

After inserting:

```text
apple
app
```

Both words share the same prefix path.

---

### ✅ Key Points

* Trie stores characters instead of complete words.
* Shared prefixes reduce memory usage.
* Exact search requires reaching a word-ending node.
* Prefix search only requires a valid path.
* Efficient for dictionary and autocomplete problems.

---

### ⚠️ Edge Cases

* Empty string insertion
* Searching a prefix as a complete word
* Duplicate insertions
* Single-character words
* Non-existing prefixes

---

### 🏁 Conclusion

The Trie (Prefix Tree) is a powerful data structure for storing and searching strings efficiently. By organizing characters hierarchically and sharing common prefixes, it supports insertion, exact word lookup, and prefix matching in linear time relative to the length of the input string.


---


## 2️⃣ Design Add and Search Words Data Structure

### 📌 Problem Statement

Design a data structure that supports the following operations:

* `addWord(word)` → Adds a word to the dictionary.
* `search(word)` → Returns `True` if the word exists in the dictionary.

Special Rule:

* The search word may contain the wildcard character `'.'`.
* `'.'` can represent any single lowercase letter.

👉 Return whether the search pattern matches any previously added word.

---

### 🚀 Approach: Trie + DFS Backtracking

#### 🔹 Key Idea

A **Trie (Prefix Tree)** efficiently stores words character by character.

Each Trie node contains:

* `children` → mapping of characters to child nodes
* `flag` → indicates whether a word ends at this node

For searching:

* Normal characters follow a single path.
* Wildcard `'.'` explores all possible child nodes using DFS.

---

### 🧠 Algorithm

#### Add Word

1. Start from the root.
2. For every character:

   * Create a new node if needed.
   * Move to the child node.
3. Mark the last node as a word ending.

#### Search Word

1. Start DFS from the root.
2. If current character is a letter:

   * Move to the corresponding child.
3. If current character is `'.'`:

   * Recursively explore all children.
4. If end of word is reached:

   * Return whether current node marks a valid word.

---

### 📊 Complexity Analysis

| Operation            | Complexity        |
| -------------------- | ----------------- |
| addWord              | O(L)              |
| search (normal word) | O(L)              |
| search (with '.')    | O(26ᴸ) worst case |

Where:

* `L` = length of the word

---

### 📎 Example

```text id="example"
Operations:

addWord("bad")
addWord("dad")
addWord("mad")

search("pad")
search("bad")
search(".ad")
search("b..")
```

Output:

```text id="output"
False
True
True
True
```

---

### 🔍 Dry Run

```text id="dryrun"
Dictionary:

bad
dad
mad

Search ".ad"

'.' → can match:
b
d
m

Checking:

bad ✓
dad ✓
mad ✓

Result = True
```

---

### 🌳 Visualization

```text id="visual"
Trie:

(root)
 ├── b
 │    └── a
 │         └── d*
 │
 ├── d
 │    └── a
 │         └── d*
 │
 └── m
      └── a
           └── d*

* = end of word
```

---

### ✅ Key Points

* Trie enables efficient prefix-based storage.
* Wildcard `'.'` requires DFS exploration.
* Word endings are tracked using a boolean flag.
* Search combines Trie traversal with backtracking.

---

### ⚠️ Edge Cases

* Empty string search
* Single-character words
* Multiple wildcards
* Wildcard-only patterns
* Searching for non-existent words

---

### 🏁 Conclusion

This problem combines the efficiency of a Trie with DFS backtracking to support wildcard searches. While normal searches follow a single path, the `'.'` character branches into multiple possibilities, making recursive exploration the natural solution. The resulting data structure supports fast insertion and flexible pattern matching.


---


## 3️⃣ Search Suggestions System

### 📌 Problem Statement

You are given:

* `products[]` → a list of product names
* `searchWord` → the word being typed by the user

For every prefix of `searchWord`:

👉 Return at most **3 lexicographically smallest products** that start with that prefix.

If no matching products exist, return an empty list for that prefix.

---

### 🚀 Approach: Trie + Prefix Suggestions

#### 🔹 Key Idea

To efficiently provide suggestions for every typed character:

1. Sort all products lexicographically.
2. Build a Trie.
3. At each Trie node, store up to the first **3 smallest products** passing through that prefix.
4. While typing the search word:

   * Traverse the Trie.
   * Retrieve stored suggestions from the corresponding node.

Since products are inserted in sorted order, the first three products reaching a node automatically become the required suggestions.

---

### 🧠 Algorithm

1. Sort the products array.
2. Create a Trie.
3. Insert every product:

   * Create nodes as needed.
   * Store up to 3 suggestions at every prefix node.
4. Traverse the Trie using the search word.
5. For each character:

   * If the prefix exists:

     * Append stored suggestions.
   * Otherwise:

     * Append empty lists for remaining prefixes.

---

### 📊 Complexity Analysis

| Type              | Complexity |
| ----------------- | ---------- |
| Sorting           | O(n log n) |
| Trie Construction | O(T)       |
| Search            | O(m)       |
| Space Complexity  | O(T)       |

Where:

* `n` = number of products
* `T` = total characters across all products
* `m` = length of `searchWord`

---

### 📎 Example

```text id="example"
Input:

products =
["mobile","mouse","moneypot","monitor","mousepad"]

searchWord = "mouse"
```

Output:

```text id="output"
[
 ["mobile","moneypot","monitor"],
 ["mobile","moneypot","monitor"],
 ["mouse","mousepad"],
 ["mouse","mousepad"],
 ["mouse","mousepad"]
]
```

---

### 🔍 Dry Run

```text id="dryrun"
Sorted Products:

mobile
moneypot
monitor
mouse
mousepad

Typing:

"m"
→ [mobile,moneypot,monitor]

"mo"
→ [mobile,moneypot,monitor]

"mou"
→ [mouse,mousepad]

"mous"
→ [mouse,mousepad]

"mouse"
→ [mouse,mousepad]
```

---

### 🌳 Visualization

```text id="visual"
(root)
  |
  m
  |
  o
  |
  ├── b → mobile
  ├── n → moneypot, monitor
  └── u
       └── s
            └── e
                 ├── mouse
                 └── mousepad
```

Each node stores:

```text id="suggestions"
Top 3 lexicographically smallest products
for that prefix
```

---

### ✅ Key Points

* Trie efficiently handles prefix searches.
* Products are sorted before insertion.
* Each node stores only 3 suggestions.
* Query time is proportional to the search word length.
* Ideal for autocomplete and search recommendation systems.

---

### ⚠️ Edge Cases

* No matching prefix
* Single product
* Duplicate prefixes
* Search word longer than all products
* Empty products list

---

### 🏁 Conclusion

The Search Suggestions System combines sorting with a Trie to efficiently provide autocomplete recommendations. By storing the top three lexicographically smallest products at every prefix node, each search query can retrieve suggestions in constant time per character, making the solution highly scalable for large product catalogs.


---


## 4️⃣ Longest Common Prefix

### 📌 Problem Statement

You are given:

* `strs[]` → an array of strings

👉 Return the **longest common prefix** shared among all strings.

If there is no common prefix, return an empty string `""`.

---

### 🚀 Approach: Trie Traversal

#### 🔹 Key Idea

A **Trie (Prefix Tree)** naturally groups strings by their common prefixes.

After inserting all words into the Trie:

* Continue traversing as long as:

  * The current node has exactly **one child**
  * The current node is **not the end of a word**

The traversed characters form the longest common prefix.

---

### 🧠 Algorithm

1. Create an empty Trie.
2. Insert all strings into the Trie.
3. Start traversal from the root.
4. While:

   * Current node has exactly one child.
   * Current node is not the end of a word.
5. Append the character to the answer.
6. Move to the child node.
7. Return the constructed prefix.

---

### 📊 Complexity Analysis

| Type              | Complexity |
| ----------------- | ---------- |
| Trie Construction | O(T)       |
| Trie Traversal    | O(LCP)     |
| Space Complexity  | O(T)       |

Where:

* `T` = total number of characters in all strings
* `LCP` = length of the longest common prefix

---

### 📎 Example

```text id="example"
Input:

strs = ["flower","flow","flight"]

Output:
"fl"
```

---

### 🔍 Dry Run

```text id="dryrun"
Insert:

flower
flow
flight

Trie:

root
 └── f
      └── l
           ├── o
           └── i

Traversal:

root → f → l

At node 'l':
Multiple children found

Stop.

Answer = "fl"
```

---

### 🌳 Visualization

```text id="visual"
(root)
  |
  f
  |
  l
 / \
o   i
|   |
w   g
|
e
|
r
```

Common path:

```text id="prefix"
f → l
```

Longest Common Prefix:

```text id="answer"
"fl"
```

---

### ✅ Key Points

* Trie efficiently captures shared prefixes.
* Traversal stops when:

  * Multiple branches appear.
  * A word ends.
* Common prefix corresponds to the shared Trie path.
* Particularly useful for prefix-based string problems.

---

### ⚠️ Edge Cases

* Empty array of strings
* Single string input
* No common prefix
* One string is a prefix of another
* All strings identical

---

### 🏁 Conclusion

The Trie-based solution efficiently identifies the longest common prefix by leveraging the hierarchical structure of shared characters. By traversing the Trie until a branch or word termination is encountered, we can directly extract the longest prefix common to all strings.


---


## 5️⃣ Longest Word in Dictionary

### 📌 Problem Statement

You are given:

* `words[]` → a list of strings

👉 Return the **longest word** in the dictionary that can be built one character at a time by other words in the dictionary.

A word is valid only if **every prefix** of that word also exists in the dictionary.

If multiple answers exist:

👉 Return the **lexicographically smallest** word.

---

### 🚀 Approach: Trie + DFS

#### 🔹 Key Idea

Insert all words into a Trie.

While traversing the Trie:

* We can move to a child node **only if that node marks the end of a valid word**.
* This guarantees that every prefix of the current word exists in the dictionary.

During DFS:

* Update the answer if:

  * A longer word is found.
  * Words have equal length but current word is lexicographically smaller.

---

### 🧠 Algorithm

1. Build a Trie from all words.
2. Mark the end of each word.
3. Start DFS from the root.
4. Traverse only through nodes where:

   * `child.end == True`
5. Construct words during traversal.
6. Update answer based on:

   * Maximum length
   * Lexicographical order
7. Return the final answer.

---

### 📊 Complexity Analysis

| Type              | Complexity |
| ----------------- | ---------- |
| Trie Construction | O(T)       |
| DFS Traversal     | O(T)       |
| Space Complexity  | O(T)       |

Where:

* `T` = total number of characters across all words.

---

### 📎 Example

```text id="example"
Input:

words =
["w","wo","wor","worl","world"]

Output:
"world"
```

---

### 🔍 Dry Run

```text id="dryrun"
Inserted Words:

w
wo
wor
worl
world

DFS Traversal:

w ✓
wo ✓
wor ✓
worl ✓
world ✓

All prefixes exist.

Answer = "world"
```

---

### 🌳 Visualization

```text id="visual"
(root)
  |
  w*
  |
  o*
  |
  r*
  |
  l*
  |
  d*

* = End of Word
```

Valid word construction:

```text id="build"
w → wo → wor → worl → world
```

---

### ✅ Key Points

* Trie naturally stores prefixes.
* DFS ensures prefix validation.
* Traverse only through valid word endings.
* Lexicographical ordering resolves ties.
* Efficient for dictionary and prefix problems.

---

### ⚠️ Edge Cases

* Empty dictionary
* Single word input
* Multiple words with same length
* Missing intermediate prefixes
* Duplicate words

---

### 🏁 Conclusion

This problem combines Trie traversal with DFS to efficiently find the longest buildable word in a dictionary. By restricting traversal to nodes representing complete words, the algorithm guarantees that every prefix exists, while lexicographical ordering ensures the correct answer when multiple candidates are possible.


