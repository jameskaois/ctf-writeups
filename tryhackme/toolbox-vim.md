# Toolbox: Vim - TryHackMe

Learn vim, a universal text editor that can be incredibly powerful when used properly. From basic text editing to editing of binary files, Vim can be an important arsenal in a security toolkit.

## Overview

- **Room URL:** [https://tryhackme.com/room/toolboxvim](https://tryhackme.com/room/toolboxvim)
- **Difficulty:** Easy
- **Time to complete:** 45

## Walkthrough

### 1. Task 1

_No answer needed!_

### 2. Task 2

- <p>How do we enter "INSERT" mode?    </p>

**=> Answer: `i`**

- <p>How do we start entering text into our new Vim document?</p>

**=> Answer: `typing`**

- <p>How do we return to command mode?            </p>

**=> Answer: `esc`**

- <p>How do we move the cursor left?</p>

**=> Answer: `h`**

- <p>How do we move the cursor right?<br /></p>

**=> Answer: `l`**

- <p>How do we move the cursor up?<br /></p>

**=> Answer: `k`**

- <p>How do we move the cursor down?<br /></p>

**=> Answer: `j`**

- <p>How do we jump to the start of a word?<br /></p>

**=> Answer: `w`**

- <p>How do we jump to the end of a word?<br /></p>

**=> Answer: `e`**

- <p>How do we insert (before the cursor)    </p>

**=> Answer: `i`**

- <p>How do we insert (at the beginning of the line?)    </p>

**=> Answer: `I`**

- <p>How do we append (after the cursor)    </p>

**=> Answer: `a`**

- <p>How do we append (at the end of the line) </p>

**=> Answer: `A`**

- <p>How do we make a new line under the current line?     </p>

**=> Answer: `o`**

### 3. Task 3

- <p>How do we <span style="">write the file, but don't exit?</span></p>

**=> Answer: `:w`**

- <p>How do we <span style="font-size:1rem;color:rgb(0, 0, 0)">write the file, but don't exit- as root?</span><br /></p>

**=> Answer: `:w !sudo tee %`**

- <p>How do we <span style="color:rgb(0, 0, 0);font-size:1rem">write and quit?</span></p>

**=> Answer: `:wq`**

- <p>How do we quit?</p>

**=> Answer: `:q`**

- <p>How do we force quit?</p>

**=> Answer: `:q!`**

- <p>How do we save and quit, for all active tabs?</p>

**=> Answer: `:wqa`**

### 4. Task 4

- How do we copy a line?

**=> Answer: `yy`**

- <p>how do we copy 2 lines?</p>

**=> Answer: `2yy`**

- <p>How do we copy to the end of the line?</p>

**=> Answer: `y$`**

- <p>How do we paste the clipboard contents after the cursor?</p>

**=> Answer: `p`**

- <p>How do we paste the clipboard contents before the cursor?<br /></p>

**=> Answer: `p`**

- <p>How do we cut a line?</p>

**=> Answer: `dd`**

- <p>How do we cut two lines?</p>

**=> Answer: `2dd`**

- <p>How do we cut to the end of the line?</p>

**=> Answer: `D`**

- <p>How do we cut a character?</p>

**=> Answer: `x`**

### 5. Task 5

- <p>How do we search forwards for a pattern (use "pattern" for your answer)</p>

**=> Answer: `/pattern`**

- <p>How do we search backwards for a pattern (use "pattern" for your answer)<br /></p>

**=> Answer: `?pattern`**

- <p>How do we repeat this search in the same direction?</p>

**=> Answer: `n`**

- <p>How do we repeat this search in the opposite direction?</p>

**=> Answer: `N`**

- <p>How do we search for "old" and replace it with "new"</p>

**=> Answer: `:%s/old/new/g`**

- <p>How do we use "grep" to search for a pattern in multiple files?</p>

**=> Answer: `:vimgrep`**
