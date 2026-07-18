# -*- coding: utf-8 -*-
"""
Offline Intelligence Helper for AI Learning Buddy.
Provides predefined high-quality educational templates and rule-based evaluation.
"""

# Extensive educational database for 11 key topics
OFFLINE_DATA = {
    "binary search": {
        "explanation": """### 🔍 What is Binary Search?

**Binary Search** is an extremely efficient algorithm used to find the position of a target value within a **sorted array**. 

Instead of checking every element one by one (Linear Search), Binary Search uses a **divide-and-conquer** strategy:
1. **Find the Middle**: It starts by looking at the element in the middle of the sorted array.
2. **Compare**: If the middle element is equal to the target, the search is complete!
3. **Halve the Search Space**: If the target is smaller than the middle element, you discard the right half. If it's larger, you discard the left half.
4. **Repeat**: Repeat the process on the remaining half until the element is found or the search space becomes empty.

#### 📈 Key Characteristics:
* **Prerequisite**: The list/array **MUST** be sorted.
* **Time Complexity**: $O(\\log N)$ — which is incredibly fast! For example, searching through 1,000,000 items takes at most **20 comparisons**.
* **Space Complexity**: $O(1)$ for iterative implementation.
""",
        "real_life_example": """### 📖 Real-Life Analogy: The physical dictionary search

Imagine you are looking for the word **"Photosynthesis"** in a thick, physical dictionary.

1. **The Sorted Setup**: A dictionary is naturally sorted alphabetically (A to Z).
2. **The Binary Search Approach**: 
   - You don't start from page 1 and read every word (that's **Linear Search**).
   - Instead, you open the dictionary **exactly in the middle** (say, you land on the letter **"M"**).
   - Since **"P"** comes after **"M"**, you know the word cannot be in the first half of the book. You completely ignore pages A through M!
   - Now, you open the remaining second half (M to Z) right in the middle (say, you land on **"T"**).
   - Since **"P"** comes before **"T"**, you throw away the second half of this section.
   - You repeat this splitting process and find "Photosynthesis" in just 4 or 5 flips, rather than reading 20,000 words!
""",
        "quiz": [
            {
                "question": "What is the primary prerequisite for applying Binary Search to an array?",
                "options": {
                    "A": "The array must be empty.",
                    "B": "The array must be sorted.",
                    "C": "The array must contain only positive integers.",
                    "D": "The array size must be a power of two."
                },
                "correct_answer": "B",
                "explanation": "Binary Search relies on the sorted order of elements to determine whether to discard the left or right half of the search space."
            },
            {
                "question": "What is the worst-case time complexity of Binary Search?",
                "options": {
                    "A": "O(1)",
                    "B": "O(N)",
                    "C": "O(N log N)",
                    "D": "O(log N)"
                },
                "correct_answer": "D",
                "explanation": "In each step, Binary Search halves the size of the search interval, leading to a logarithmic time complexity."
            },
            {
                "question": "If you are searching an array of 1,024 sorted elements, what is the maximum number of comparisons Binary Search will make?",
                "options": {
                    "A": "1,024",
                    "B": "512",
                    "C": "10",
                    "D": "20"
                },
                "correct_answer": "C",
                "explanation": "Since 2^10 = 1024, searching through 1024 items takes at most 10 divisions."
            },
            {
                "question": "Which algorithmic design strategy does Binary Search utilize?",
                "options": {
                    "A": "Dynamic Programming",
                    "B": "Greedy Choice",
                    "C": "Divide and Conquer",
                    "D": "Backtracking"
                },
                "correct_answer": "C",
                "explanation": "It divides the problem into halves, discarding the irrelevant half and solving the smaller subproblem."
            },
            {
                "question": "What happens if the target element is NOT present in the sorted array?",
                "options": {
                    "A": "The algorithm loops indefinitely.",
                    "B": "An error is thrown.",
                    "C": "The low pointer exceeds the high pointer, and the search terminates returning -1 or None.",
                    "D": "The array is automatically resorted."
                },
                "correct_answer": "C",
                "explanation": "When the search pointers cross (low > high), it signifies the target is not present, and the algorithm exits safely."
            }
        ],
        "keywords": ["sort", "divide", "conquer", "middle", "half", "pointers", "log", "complexity"],
        "guide": "Binary Search requires a sorted list. It finds the middle element, compares it with the target, and discards the half that cannot contain the target, repeating until found."
    },
    "binary tree": {
        "explanation": """### 🌳 What is a Binary Tree?

A **Binary Tree** is a hierarchical, non-linear data structure in which each node has at most **two children**, referred to as the **left child** and the **right child**.

#### 📐 Core Concepts:
1. **Root**: The top-most node of the tree, which has no parent.
2. **Parent and Child**: Nodes connected by an edge where the upper node is the parent.
3. **Leaf Node**: Nodes at the bottom of the tree that have no children.
4. **Subtree**: A tree formed by a node and its descendants.
5. **Height**: The number of edges on the longest path from the root to a leaf.

#### 🗂️ Common Types of Binary Trees:
* **Full Binary Tree**: Every node has either 0 or 2 children.
* **Complete Binary Tree**: All levels are completely filled except possibly the last level, which is filled from left to right.
* **Binary Search Tree (BST)**: A special binary tree where the left child's value is less than the parent's, and the right child's value is greater.
""",
        "real_life_example": """### 📖 Real-Life Analogy: A Family Tree or Corporate Hierarchy

Think of a **Binary Tree** like a strict corporate hierarchy in a highly structured start-up:

1. **The Root (CEO)**: The CEO represents the root node at the top.
2. **Two Managers (Children)**: The CEO has exactly two direct reports (e.g., VP of Engineering and VP of Sales).
3. **Team Leads**: Each VP manages at most two team leads (their left and right children).
4. **Individual Contributors (Leaf Nodes)**: At the bottom are the individual software engineers and salespeople who have no direct reports (leaf nodes).
5. **The Structure**: Information flows downwards from parents to children, and each person only reports to one immediate boss (parent node).
""",
        "quiz": [
            {
                "question": "What is the maximum number of children any node in a binary tree can have?",
                "options": {
                    "A": "1",
                    "B": "2",
                    "C": "3",
                    "D": "Unlimited"
                },
                "correct_answer": "B",
                "explanation": "By definition, a binary tree node can have at most 2 children (left and right)."
            },
            {
                "question": "What is a node with no children called?",
                "options": {
                    "A": "Root Node",
                    "B": "Internal Node",
                    "C": "Leaf Node",
                    "D": "Ancestor Node"
                },
                "correct_answer": "C",
                "explanation": "Nodes at the bottom-most boundary of a tree that have no children are called leaf nodes."
            },
            {
                "question": "In a Binary Search Tree (BST), where is a value smaller than the root node stored?",
                "options": {
                    "A": "In the right subtree.",
                    "B": "In the root node.",
                    "C": "In the left subtree.",
                    "D": "As a sibling to the root."
                },
                "correct_answer": "C",
                "explanation": "In a BST, the left subtree contains values strictly smaller than the node, and the right subtree contains values strictly larger."
            },
            {
                "question": "What is the height of a empty binary tree (no nodes)?",
                "options": {
                    "A": "-1 (or sometimes defined as 0 depending on convention)",
                    "B": "1",
                    "C": "Infinity",
                    "D": "Undefined"
                },
                "correct_answer": "A",
                "explanation": "Conventionally, a tree with no nodes has a height of -1 (or 0), while a tree with only a root node has a height of 0 (or 1)."
            },
            {
                "question": "Which tree traversal visits the root node LAST?",
                "options": {
                    "A": "Pre-order",
                    "B": "In-order",
                    "C": "Post-order",
                    "D": "Level-order"
                },
                "correct_answer": "C",
                "explanation": "Post-order traversal visits the left subtree, then the right subtree, and finally the root node (Left, Right, Root)."
            }
        ],
        "keywords": ["node", "child", "children", "root", "leaf", "left", "right", "bst", "subtree"],
        "guide": "A Binary Tree is a hierarchical structure where each node has at most two child nodes (left and right). Key nodes include the root and leaves."
    },
    "dbms": {
        "explanation": """### 🗄️ What is a DBMS?

A **Database Management System (DBMS)** is system software for creating, managing, retrieving, and updating data in databases. It serves as an interface between databases and end-users or application programs.

#### 🌟 Key Responsibilities of a DBMS:
1. **Data Definition**: Creating, modifying, and removing database structures (tables, schemas).
2. **Data Manipulation**: Inserting, updating, deleting, and querying data (usually via SQL).
3. **Transaction Management**: Ensuring data integrity via **ACID properties**:
   * **A**tomicity: All or nothing.
   * **C**onsistency: Moves from one valid state to another.
   * **I**solation: Transactions run concurrently without interfering.
   * **D**urability: Once saved, data is permanent even during crashes.
4. **Concurrency Control**: Managing simultaneous data access.
5. **Data Security**: Controlling user permissions and data access.
""",
        "real_life_example": """### 📖 Real-Life Analogy: The University Registrar's Office

Imagine a massive university with 50,000 students. 

* **The Database**: The actual files containing student grades, courses, and fees.
* **The DBMS**: The **Registrar's Office staff and their computer system**.
  - If a professor wants to enter a grade, they don't scribble it on the hard drive. They request the Registrar (DBMS) to update it.
  - The Registrar ensures that a student cannot enroll in two classes scheduled at the same time (**Consistency/Rules**).
  - The Registrar ensures that two advisors updating a student's address at the same moment don't corrupt the record (**Concurrency Control**).
  - Only authorized faculty can view student financial files (**Security**).
""",
        "quiz": [
            {
                "question": "What does the acronym ACID stand for in DBMS?",
                "options": {
                    "A": "Action, Control, Isolation, Database",
                    "B": "Atomicity, Consistency, Isolation, Durability",
                    "C": "Access, Creation, Integrity, Distribution",
                    "D": "Algorithm, Core, Index, Document"
                },
                "correct_answer": "B",
                "explanation": "ACID represents the fundamental properties (Atomicity, Consistency, Isolation, Durability) that guarantee database transactions are processed reliably."
            },
            {
                "question": "Which SQL statement is used to retrieve data from a database?",
                "options": {
                    "A": "GET",
                    "B": "EXTRACT",
                    "C": "SELECT",
                    "D": "FETCH"
                },
                "correct_answer": "C",
                "explanation": "The SELECT statement in SQL is used to query and fetch records from one or more tables."
            },
            {
                "question": "What is a Primary Key in a database table?",
                "options": {
                    "A": "A key that can unlock the database server.",
                    "B": "A unique identifier for each record in a table, which cannot contain NULL values.",
                    "C": "An optional description field.",
                    "D": "A key used to encrypt the table data."
                },
                "correct_answer": "B",
                "explanation": "A primary key uniquely identifies each row in a table. It must contain unique values and cannot contain NULL values."
            },
            {
                "question": "Which of the following database models uses tables (relations) to store data?",
                "options": {
                    "A": "Hierarchical Model",
                    "B": "Network Model",
                    "C": "Relational Model",
                    "D": "NoSQL Key-Value Model"
                },
                "correct_answer": "C",
                "explanation": "The Relational Database Model organizes data into tables consisting of rows (tuples) and columns (attributes)."
            },
            {
                "question": "What is the purpose of a Foreign Key?",
                "options": {
                    "A": "To translate database queries into foreign languages.",
                    "B": "To establish a link or relationship between data in two different tables.",
                    "C": "To bypass database security protocols.",
                    "D": "To speed up data deletion."
                },
                "correct_answer": "B",
                "explanation": "A foreign key is a field (or collection of fields) in one table that refers to the primary key in another table, enforcing referential integrity."
            }
        ],
        "keywords": ["database", "acid", "sql", "transaction", "primary", "foreign", "key", "relation", "table"],
        "guide": "A DBMS manages databases. It enforces ACID properties to ensure transaction reliability, manages schemas, queries data via languages like SQL, and handles security and concurrency."
    },
    "python": {
        "explanation": """### 🐍 What is Python?

**Python** is a high-level, interpreted, general-purpose programming language. It is widely known for its clean syntax, readability, and extreme versatility.

#### 💡 Key Features of Python:
1. **Readable Syntax**: Python's syntax resembles natural English, making it incredibly beginner-friendly. It uses indentation to define code blocks instead of curly braces `{}`.
2. **Interpreted Language**: Python code is executed line-by-line, which speeds up testing and debugging.
3. **Dynamically Typed**: You don't need to declare variable types (like `int x = 5` in C++). Python figures it out automatically: `x = 5`.
4. **Batteries Included**: Python comes with a massive standard library and third-party package ecosystem (like NumPy, Pandas, Django, and Streamlit!) for almost any task.
""",
        "real_life_example": """### 📖 Real-Life Analogy: The Swiss Army Knife

Imagine a toolkit. Some tools are highly specialized and hard to use (like a jackhammer — equivalent to assembly or low-level C).

* **Python is a Swiss Army Knife**:
  - It is compact, comfortable to hold, and has a tool for almost everything: a scissors, a bottle opener, a blade, a corkscrew, and a toothpick.
  - While a Swiss Army Knife isn't the fastest tool to chop down a huge tree (analogous to Python being slower than C++ for heavy game engines), it is the **most convenient and versatile tool** to carry around for everyday problem-solving, data analysis, script building, and rapid prototyping.
""",
        "quiz": [
            {
                "question": "How are blocks of code (like loops or functions) defined in Python?",
                "options": {
                    "A": "Using curly braces { }",
                    "B": "Using parentheses ( )",
                    "C": "Using indentation (spaces or tabs)",
                    "D": "Using semicolon labels"
                },
                "correct_answer": "C",
                "explanation": "Python does not use braces to define code blocks. Instead, it relies on consistent indentation (usually 4 spaces) to define code scope."
            },
            {
                "question": "Which of the following data types in Python is MUTABLE?",
                "options": {
                    "A": "Tuple",
                    "B": "List",
                    "C": "String",
                    "D": "Integer"
                },
                "correct_answer": "B",
                "explanation": "Lists in Python are mutable, meaning their elements can be modified after creation. Tuples, strings, and integers are immutable."
            },
            {
                "question": "What is the correct syntax to define a function in Python?",
                "options": {
                    "A": "function my_func():",
                    "B": "def my_func():",
                    "C": "void my_func()",
                    "D": "define my_func:"
                },
                "correct_answer": "B",
                "explanation": "In Python, the 'def' keyword is used to define functions, followed by the function name, parentheses, and a colon."
            },
            {
                "question": "What does the expression 3 ** 2 evaluate to in Python?",
                "options": {
                    "A": "6",
                    "B": "9",
                    "C": "5",
                    "D": "8"
                },
                "correct_answer": "B",
                "explanation": "The '**' operator in Python is used for exponentiation (raising a number to a power). 3 ** 2 is 3 squared, which is 9."
            },
            {
                "question": "Which Python keyword is used to handle exceptions/errors in a try block?",
                "options": {
                    "A": "catch",
                    "B": "except",
                    "C": "error",
                    "D": "finally"
                },
                "correct_answer": "B",
                "explanation": "Python uses 'try' and 'except' blocks for exception handling, unlike Java or C++ which use 'try' and 'catch'."
            }
        ],
        "keywords": ["interpret", "dynamic", "indent", "variable", "mutable", "list", "tuple", "syntax", "def"],
        "guide": "Python is an interpreted, readable, general-purpose language that relies on indentation for block structure. It is dynamically typed and supports multiple programming paradigms."
    },
    "photosynthesis": {
        "explanation": """### 🍃 What is Photosynthesis?

**Photosynthesis** is the chemical process by which green plants, algae, and some bacteria convert light energy (from the sun) into chemical energy (glucose/sugar), using water and carbon dioxide.

#### 🧪 The Chemical Equation:
$$6CO_2 + 6H_2O + \\text{Light Energy} \\rightarrow C_6H_{12}O_6 + 6O_2$$
*(Carbon Dioxide + Water + Light $\\rightarrow$ Glucose + Oxygen)*

#### 🔬 Key Steps in Photosynthesis:
1. **Light-Dependent Reactions**: 
   * Happens in the **thylakoid membranes** of chloroplasts.
   * Absorbs sunlight using **chlorophyll**.
   * Splits water ($H_2O$) molecules, releasing oxygen ($O_2$) as a byproduct, and creating energy-carrier molecules (ATP and NADPH).
2. **Light-Independent Reactions (The Calvin Cycle)**:
   * Happens in the **stroma** of chloroplasts.
   * Uses ATP, NADPH, and Carbon Dioxide ($CO_2$) to synthesize sugar (**Glucose**).
""",
        "real_life_example": """### 📖 Real-Life Analogy: A Solar-Powered Bakery

Think of a leaf as a highly sophisticated **Solar-Powered Bakery**:

1. **The Bakery (The Chloroplast)**: This is where all the baking takes place.
2. **The Solar Panels (Chlorophyll)**: These green pigments sit on the roof, trapping the energy from the sun.
3. **The Raw Materials**: The baker collects **Water** ($H_2O$) from the pipes (roots) and **Flour/Air** ($CO_2$) from the windows (stomata).
4. **The Oven (Light Reactions)**: Sunlight is converted into electric power (ATP/NADPH).
5. **The Mixing & Baking (Calvin Cycle)**: The baker uses the raw materials and electric power to bake delicious **Cakes (Glucose)**.
6. **The Exhaust (Oxygen)**: During the baking process, a fresh exhaust gas (**Oxygen**) is puffed out of the bakery chimneys into the air.
""",
        "quiz": [
            {
                "question": "What pigment absorbs sunlight to initiate photosynthesis?",
                "options": {
                    "A": "Melanin",
                    "B": "Chlorophyll",
                    "C": "Hemoglobin",
                    "D": "Carotenoid"
                },
                "correct_answer": "B",
                "explanation": "Chlorophyll is the green pigment in chloroplasts that absorbs light energy, primarily blue and red wavelengths, for photosynthesis."
            },
            {
                "question": "What is the primary gas released as a byproduct during photosynthesis?",
                "options": {
                    "A": "Carbon Dioxide (CO2)",
                    "B": "Nitrogen (N2)",
                    "C": "Oxygen (O2)",
                    "D": "Water Vapor (H2O)"
                },
                "correct_answer": "C",
                "explanation": "When water molecules are split during the light-dependent reactions, oxygen is released as a waste byproduct."
            },
            {
                "question": "Where do the light-independent reactions (Calvin Cycle) take place?",
                "options": {
                    "A": "Thylakoid Membrane",
                    "B": "Mitochondria",
                    "C": "Stroma of the chloroplast",
                    "D": "Cell Wall"
                },
                "correct_answer": "C",
                "explanation": "While light reactions occur in the thylakoid membrane, the carbon-fixing Calvin Cycle occurs in the fluid-filled stroma of the chloroplast."
            },
            {
                "question": "What is the correct chemical formula for the glucose produced in photosynthesis?",
                "options": {
                    "A": "H2O",
                    "B": "CO2",
                    "C": "C6H12O6",
                    "D": "NaCl"
                },
                "correct_answer": "C",
                "explanation": "C6H12O6 is the chemical formula for glucose, which is the simple carbohydrate produced as energy food for plants."
            },
            {
                "question": "Which of the following is NOT required for photosynthesis to occur?",
                "options": {
                    "A": "Sunlight",
                    "B": "Oxygen",
                    "C": "Water",
                    "D": "Carbon Dioxide"
                },
                "correct_answer": "B",
                "explanation": "Oxygen is a *product* of photosynthesis, not a starting reactant. Plants require sunlight, water, and carbon dioxide."
            }
        ],
        "keywords": ["chloroplast", "chlorophyll", "sunlight", "glucose", "oxygen", "carbon dioxide", "water", "calvin", "thylakoid"],
        "guide": "Photosynthesis is the process where plants use chlorophyll to capture light energy, combining carbon dioxide and water to produce glucose and release oxygen."
    },
    "machine learning": {
        "explanation": """### 🤖 What is Machine Learning?

**Machine Learning (ML)** is a subset of Artificial Intelligence (AI) that focuses on building systems that can learn from data, identify patterns, and make decisions with minimal human intervention.

Instead of writing explicit rules (traditional programming), you feed the computer data and let it figure out the rules on its own.

#### 🗃️ Three Main Types of Machine Learning:
1. **Supervised Learning**: The model is trained on **labeled data** (input-output pairs). Example: Training an email spam filter with thousands of emails labeled "spam" or "not spam".
2. **Unsupervised Learning**: The model works with **unlabeled data** and tries to find hidden structures or groups. Example: Customer segmentation based on buying behavior.
3. **Reinforcement Learning**: The model learns by trial and error in an environment, receiving **rewards or penalties**. Example: An AI learning to play chess or drive a self-driving car.
""",
        "real_life_example": """### 📖 Real-Life Analogy: Learning to Shoot a Basketball

Imagine you are teaching a child to shoot a basketball.

* **Traditional Programming (Explicit Rules)**: You write a massive manual with precise angles, wind vectors, knee angles, and release velocities. The child attempts to calculate and execute this, but crashes because real-world variables change.
* **Machine Learning Approach (Supervised / Reinforcement)**:
  - You let the child throw the ball.
  - Throw 1: Too hard $\rightarrow$ misses (**Negative Feedback / Data point**).
  - Throw 2: Too soft $\rightarrow$ falls short (**Negative Feedback**).
  - Throw 3: Perfect angle $\rightarrow$ swish! (**Positive Reward**).
  - After 500 attempts (training epochs), the child's brain automatically adjusts muscle memory based on what worked. The brain **learned the optimal mapping from target distance (input) to throw power (output) from historical data**.
""",
        "quiz": [
            {
                "question": "What is the difference between Supervised and Unsupervised Learning?",
                "options": {
                    "A": "Supervised uses computers; Unsupervised uses humans.",
                    "B": "Supervised requires labeled training data; Unsupervised uses unlabeled data to find hidden structures.",
                    "C": "Supervised is fast; Unsupervised is slow.",
                    "D": "Supervised is only for robot control."
                },
                "correct_answer": "B",
                "explanation": "Supervised learning relies on explicit input-output labels to map connections, whereas unsupervised learning identifies patterns in data without pre-existing labels."
            },
            {
                "question": "Which type of ML uses rewards and penalties to guide an agent in an environment?",
                "options": {
                    "A": "Supervised Learning",
                    "B": "Unsupervised Learning",
                    "C": "Reinforcement Learning",
                    "D": "Semi-supervised Learning"
                },
                "correct_answer": "C",
                "explanation": "Reinforcement learning is based on an agent interacting with an environment to maximize cumulative rewards, mimicking trial-and-error learning."
            },
            {
                "question": "What is 'Overfitting' in Machine Learning?",
                "options": {
                    "A": "When the model is too big to fit in memory.",
                    "B": "When a model learns the training data too well, including its noise, making it perform poorly on new, unseen data.",
                    "C": "When the model finishes training too quickly.",
                    "D": "When data contains too many features."
                },
                "correct_answer": "B",
                "explanation": "Overfitting occurs when a model memorizes training details and noise instead of generalizing the underlying trend, failing on fresh testing data."
            },
            {
                "question": "What is a common algorithm used for Classification tasks in ML?",
                "options": {
                    "A": "K-Means Clustering",
                    "B": "Linear Regression",
                    "C": "Logistic Regression",
                    "D": "Apriori Algorithm"
                },
                "correct_answer": "C",
                "explanation": "Despite its name containing 'regression', Logistic Regression is a classic algorithm used to classify data into discrete categories (e.g., Yes/No)."
            },
            {
                "question": "What is the 'training set' used for in ML?",
                "options": {
                    "A": "To evaluate the final accuracy of the model.",
                    "B": "To teach the model and fit its parameters.",
                    "C": "To write the application code.",
                    "D": "To encrypt the database."
                },
                "correct_answer": "B",
                "explanation": "The training set is the dataset fed directly into the learning algorithm to calibrate its internal mathematical coefficients."
            }
        ],
        "keywords": ["data", "supervised", "unsupervised", "reinforcement", "learn", "overfit", "train", "pattern", "label"],
        "guide": "Machine Learning is training algorithms on data to learn patterns and make predictions without explicit rules. It is split into supervised, unsupervised, and reinforcement categories."
    },
    "sorting": {
        "explanation": """### 📊 What is Sorting?

**Sorting** is the process of arranging elements in a specific order (typically ascending or descending alphabetical or numerical order).

Sorting is a fundamental problem in Computer Science because sorted data makes searching, merging, and parsing operations extremely fast.

#### ⚡ Common Sorting Algorithms:
1. **Bubble Sort**: Repeatedly swaps adjacent elements if they are in the wrong order. Very slow ($O(N^2)$) but simple.
2. **Insertion Sort**: Builds the final sorted array one item at a time by inserting elements into their correct spots (like sorting a hand of playing cards). Average: $O(N^2)$.
3. **Merge Sort**: A **divide-and-conquer** algorithm. It splits the array in half, recursively sorts each half, and merges them. Fast ($O(N \\log N)$).
4. **Quick Sort**: Selects a 'pivot' element and partitions the other elements into those smaller and larger than the pivot. Fast on average ($O(N \\log N)$).
""",
        "real_life_example": """### 📖 Real-Life Analogy: Sorting a Hand of Playing Cards

Imagine you are dealt 5 playing cards, and you want to arrange them from lowest to highest value:

* **Bubble Sort Approach**: You compare card 1 and 2, swap if wrong. Compare card 2 and 3, swap if wrong. You keep scanning across your hand, swapping adjacent cards until no swaps are needed.
* **Insertion Sort Approach**: You hold your cards in a pile. You pick card 2 and insert it before or after card 1. You take card 3 and slide it into its perfect position relative to cards 1 and 2. You repeat this until your hand is completely sorted.
* **Merge Sort Approach**: You split your 5 cards into small piles of 1 or 2 cards. You sort those micro-piles, then merge two sorted pairs back together into a final sorted hand.
""",
        "quiz": [
            {
                "question": "What is the average time complexity of Merge Sort?",
                "options": {
                    "A": "O(N^2)",
                    "B": "O(N)",
                    "C": "O(N log N)",
                    "D": "O(log N)"
                },
                "correct_answer": "C",
                "explanation": "Merge Sort repeatedly divides the array in half (log N splits) and merges them (O(N) operations), giving O(N log N) in all cases."
            },
            {
                "question": "Which of the following sorting algorithms has a worst-case time complexity of O(N^2)?",
                "options": {
                    "A": "Merge Sort",
                    "B": "Bubble Sort",
                    "C": "Heap Sort",
                    "D": "Radix Sort"
                },
                "correct_answer": "B",
                "explanation": "Bubble Sort uses nested loops to compare adjacent elements, resulting in a worst-case complexity of O(N^2)."
            },
            {
                "question": "What is a 'Stable' sorting algorithm?",
                "options": {
                    "A": "An algorithm that never crashes.",
                    "B": "An algorithm that maintains the relative order of identical elements.",
                    "C": "An algorithm that runs in O(1) space.",
                    "D": "An algorithm designed only for static arrays."
                },
                "correct_answer": "B",
                "explanation": "Stability means if two elements have the same value, their original sequence order remains unchanged in the final sorted list."
            },
            {
                "question": "Which sorting algorithm is based on choosing a 'Pivot' element?",
                "options": {
                    "A": "Merge Sort",
                    "B": "Quick Sort",
                    "C": "Selection Sort",
                    "D": "Insertion Sort"
                },
                "correct_answer": "B",
                "explanation": "Quick Sort selects a pivot element and partitions the array into segments smaller and larger than the pivot."
            },
            {
                "question": "Which algorithm is highly efficient for sorting a hand of playing cards manually?",
                "options": {
                    "A": "Bubble Sort",
                    "B": "Insertion Sort",
                    "C": "Heap Sort",
                    "D": "Quick Sort"
                },
                "correct_answer": "B",
                "explanation": "Insertion Sort matches how humans intuitively sort items in their hand — by inserting one new item at a time into a sorted subset."
            }
        ],
        "keywords": ["sort", "bubble", "merge", "quick", "insertion", "pivot", "complexity", "swap", "order"],
        "guide": "Sorting arranges items in numerical/alphabetical sequence. Algorithms vary in efficiency (O(N log N) like Merge Sort vs O(N^2) like Bubble Sort) and style."
    },
    "stack": {
        "explanation": """### 📚 What is a Stack?

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

This means that the last element added to the stack is the very first one to be removed. Think of it as a vertical container.

#### ⚙️ Core Operations:
1. **Push**: Add an element to the top of the stack.
2. **Pop**: Remove and return the top element of the stack.
3. **Peek/Top**: View the top element without removing it.
4. **IsEmpty**: Check if the stack is empty.

#### 📈 Time Complexity:
* **Push/Pop/Peek**: $O(1)$ — highly efficient constant time operations since actions only happen at one end!
""",
        "real_life_example": """### 📖 Real-Life Analogy: A Stack of Dinner Plates

Imagine you are washing dishes and stacking clean plates in a kitchen cabinet:

1. **Stacking Plates (Push)**: You place plate 1 on the shelf. You wash plate 2 and place it **on top** of plate 1. You wash plate 3 and place it on top of plate 2.
2. **Taking Plates to Eat (Pop)**: When it's dinner time, you cannot pull plate 1 from the bottom (unless you want all the plates to crash!).
3. **LIFO Rule**: You take **plate 3 (the top-most plate)** first. This is LIFO — the plate you washed *last* is the one you retrieve *first*.
""",
        "quiz": [
            {
                "question": "What access principle does a Stack follow?",
                "options": {
                    "A": "FIFO (First In, First Out)",
                    "B": "LIFO (Last In, First Out)",
                    "C": "Random Access",
                    "D": "Priority-Based Access"
                },
                "correct_answer": "B",
                "explanation": "A stack is strictly Last In, First Out (LIFO), where elements are added and removed from the same top boundary."
            },
            {
                "question": "What is the name of the operation that adds an element to the stack?",
                "options": {
                    "A": "Pop",
                    "B": "Enqueue",
                    "C": "Push",
                    "D": "Insert"
                },
                "correct_answer": "C",
                "explanation": "The 'Push' operation inserts a new item onto the top of the stack."
            },
            {
                "question": "What error occurs if you try to POP an element from an empty stack?",
                "options": {
                    "A": "Stack Overflow",
                    "B": "Stack Underflow",
                    "C": "NullPointer Exception",
                    "D": "Out of Bounds"
                },
                "correct_answer": "B",
                "explanation": "Popping from an empty stack results in a 'Stack Underflow' error. Pushing onto a completely full, fixed-size stack results in 'Stack Overflow'."
            },
            {
                "question": "Which of the following is a classic practical application of a Stack?",
                "options": {
                    "A": "Printer task queue.",
                    "B": "Undo / Redo history mechanism in text editors.",
                    "C": "Ticket booking lines.",
                    "D": "Broadcasting network packets."
                },
                "correct_answer": "B",
                "explanation": "An Undo button requires retrieving your absolute last change first, making it a perfect match for LIFO/Stack structures."
            },
            {
                "question": "What is the time complexity to PUSH or POP from a standard stack?",
                "options": {
                    "A": "O(N)",
                    "B": "O(log N)",
                    "C": "O(1)",
                    "D": "O(N log N)"
                },
                "correct_answer": "C",
                "explanation": "Since insertions and deletions only happen at the pre-tracked top pointer, stack operations are constant time O(1)."
            }
        ],
        "keywords": ["stack", "lifo", "push", "pop", "peek", "top", "underflow", "overflow", "undo"],
        "guide": "A Stack is a LIFO (Last In, First Out) structure where push and pop occur at the top. Stack overflow and underflow represent limit errors."
    },
    "queue": {
        "explanation": """### 🚶‍♂️ What is a Queue?

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.

This means that the first element added to the queue is the first one to be removed. Think of it as a horizontal line.

#### ⚙️ Core Operations:
1. **Enqueue**: Add an element to the back (rear) of the queue.
2. **Dequeue**: Remove and return the front element of the queue.
3. **Front/Peek**: View the front element without removing it.
4. **Rear**: View the last element in the queue.

#### 📈 Time Complexity:
* **Enqueue/Dequeue**: $O(1)$ constant time operations if implemented correctly using pre-tracked head and tail pointers.
""",
        "real_life_example": """### 📖 Real-Life Analogy: Waiting in Line at a Movie Theater

Imagine you want to buy tickets for a blockbuster movie:

1. **Getting in Line (Enqueue)**: Person A arrives and stands at the counter. Person B arrives and stands *behind* Person A. Person C stands behind Person B.
2. **Buying Tickets (Dequeue)**: The ticket salesperson serves the person at the **front of the line** first. 
3. **FIFO Rule**: Person A gets served first, buys their ticket, and leaves the line. Only when A is done does Person B get served. The person who joined the queue first gets served first!
""",
        "quiz": [
            {
                "question": "What access principle does a standard Queue follow?",
                "options": {
                    "A": "LIFO (Last In, First Out)",
                    "B": "FIFO (First In, First Out)",
                    "C": "Random Access",
                    "D": "Last In, Last Out (LILO) - wait, this is the same as FIFO"
                },
                "correct_answer": "B",
                "explanation": "A queue is strictly First In, First Out (FIFO), meaning items leave the queue in the exact order they entered."
            },
            {
                "question": "What is the operation to add an element to the back of a queue?",
                "options": {
                    "A": "Push",
                    "B": "Dequeue",
                    "C": "Enqueue",
                    "D": "Pop"
                },
                "correct_answer": "C",
                "explanation": "Enqueue adds a new element to the tail/rear boundary of a queue."
            },
            {
                "question": "From which boundary of the queue are elements removed?",
                "options": {
                    "A": "Rear/Back",
                    "B": "Front/Head",
                    "C": "Middle",
                    "D": "Random locations"
                },
                "correct_answer": "B",
                "explanation": "Elements are always dequeued (removed) from the 'Front' or 'Head' of the queue."
            },
            {
                "question": "Which of the following is a classic application of a Queue data structure?",
                "options": {
                    "A": "Recursive function calls.",
                    "B": "Print spooler (managing printer print jobs).",
                    "C": "Web browser back button history.",
                    "D": "Arithmetic expression parsing."
                },
                "correct_answer": "B",
                "explanation": "A printer handles document requests in the exact sequence they are submitted, which is a classic FIFO queue application."
            },
            {
                "question": "What is a 'Circular Queue' designed to solve?",
                "options": {
                    "A": "Memory wastage in array-based linear queue implementations.",
                    "B": "Infinite loops in code.",
                    "C": "Slow searching speeds.",
                    "D": "The sorting of random data elements."
                },
                "correct_answer": "A",
                "explanation": "In a linear array queue, dequeuing leaves empty spaces at the front that can't be reused easily. A circular queue wraps pointers around to reuse this wasted memory."
            }
        ],
        "keywords": ["queue", "fifo", "enqueue", "dequeue", "front", "rear", "circular", "line", "buffer"],
        "guide": "A Queue is a FIFO (First In, First Out) linear structure. Enqueue adds to the rear, and dequeue removes from the front."
    },
    "operating system": {
        "explanation": """### 💻 What is an Operating System?

An **Operating System (OS)** is system software that acts as an intermediary between computer hardware and the user/applications. It controls and coordinates the use of hardware among various system programs and user apps.

#### ⚙️ Primary Core Functions of an OS:
1. **Processor Management (CPU Scheduling)**: Decides which process gets the CPU, when, and for how long (Algorithms like Round Robin, FIFO, Shortest Job First).
2. **Memory Management**: Coordinates RAM, tracking what parts of memory are currently in use, and allocating/deallocating space for running programs.
3. **File System Management**: Organizes, manages, and stores files on hard drives, managing directory trees and read/write permissions.
4. **Device Management**: Communicates with hardware components (keyboard, mouse, monitor, printer) using **device drivers**.
5. **Security & Protection**: Keeps user data isolated and prevents malware from tampering with physical memory.
""",
        "real_life_example": """### 📖 Real-Life Analogy: The Hotel Manager

Think of a computer's physical hardware as a **Hotel Building** (rooms, beds, kitchen, laundry).

* **The OS is the Hotel General Manager**:
  - The guests are the **running applications** (Chrome, Spotify, games).
  - The rooms are **system memory (RAM)**. The Manager decides which guest gets which room (Memory Management).
  - The hotel has only one shared kitchen **(The CPU)**. The Manager coordinates who gets to use the kitchen stoves and in what order so guests don't fight (CPU Scheduling).
  - If a guest wants to print a receipt (use hardware), they ask the front desk. The Manager coordinates the printing machine so papers don't jam (Device Management).
  - The Manager locks individual room doors to ensure Guest A cannot wake up and steal bags from Guest B's closet (Security/Isolation).
""",
        "quiz": [
            {
                "question": "What is the core heart of an operating system that has complete control over everything in the system?",
                "options": {
                    "A": "The Shell",
                    "B": "The Kernel",
                    "C": "The Bootloader",
                    "D": "The Registry"
                },
                "correct_answer": "B",
                "explanation": "The Kernel is the central, foundational component of an OS that manages hardware-level system operations directly."
            },
            {
                "question": "What is virtual memory?",
                "options": {
                    "A": "RAM purchased online.",
                    "B": "A storage allocation technique where secondary hard-drive space is used to trick the CPU into thinking it has more RAM.",
                    "C": "Memory designed only for gaming.",
                    "D": "The cloud-based storage system."
                },
                "correct_answer": "B",
                "explanation": "Virtual memory uses hardware and software to map virtual addresses to physical storage, allowing programs to run even if they exceed active RAM capacities."
            },
            {
                "question": "What is a 'Deadlock' in an operating system?",
                "options": {
                    "A": "When the computer's power is unplugged.",
                    "B": "A situation where a set of processes are blocked because each process is holding a resource and waiting for another resource held by some other process.",
                    "C": "When a file is permanently locked and deleted.",
                    "D": "A network connection crash."
                },
                "correct_answer": "B",
                "explanation": "Deadlock is a circular waiting state where Process A holds resource X and waits for Y, while Process B holds Y and waits for X. Neither can proceed."
            },
            {
                "question": "Which CPU scheduling algorithm gives equal, timed turns (time slices) to every process?",
                "options": {
                    "A": "Shortest Job First (SJF)",
                    "B": "Round Robin (RR)",
                    "C": "First Come, First Served (FCFS)",
                    "D": "Priority Scheduling"
                },
                "correct_answer": "B",
                "explanation": "Round Robin assigns a small, fixed unit of time (time quantum) to each active process in circular rotation."
            },
            {
                "question": "What is the main purpose of device drivers?",
                "options": {
                    "A": "To drive hardware delivery trucks.",
                    "B": "To translate generic OS system commands into specialized instructions that a specific hardware device understands.",
                    "C": "To backup user files.",
                    "D": "To scan the computer for viruses."
                },
                "correct_answer": "B",
                "explanation": "Device drivers are translator programs that let the OS control physical hardware units (like printers or graphics cards) easily."
            }
        ],
        "keywords": ["kernel", "scheduling", "memory", "deadlock", "process", "thread", "virtual", "cpu", "ram"],
        "guide": "An OS is an intermediary between hardware and applications. Key duties include processor scheduling, memory allocation, and device and file coordination."
    },
    "computer networks": {
        "explanation": """### 🌐 What are Computer Networks?

A **Computer Network** is a set of connected computers and devices that can share resources and exchange digital data.

Networks operate using standard protocol rules (such as TCP/IP) to package, address, and deliver data packets across physical or wireless connections.

#### 🏢 The OSI Model (7 layers of networking standard):
1. **Physical Layer**: Physical transmission medium (cables, radio waves).
2. **Data Link Layer**: Node-to-node data transfer (MAC addresses, Ethernet).
3. **Network Layer**: Packet routing and forwarding (**IP addresses**).
4. **Transport Layer**: End-to-end reliability and connection control (**TCP / UDP**).
5. **Session Layer**: Managing communication sessions.
6. **Presentation Layer**: Data formatting, encryption, and compression.
7. **Application Layer**: User interaction interfaces (**HTTP, FTP, SMTP**).
""",
        "real_life_example": """### 📖 Real-Life Analogy: Sending a Physical Postal Letter

Imagine you want to send a physical letter to a friend in another country:

1. **The Letter (Data payload)**: You write your message on paper.
2. **The Envelope (Packaging)**: You put the letter in an envelope. This is like adding headers (Transport layer TCP).
3. **The Address (IP Routing)**: You write your friend's home address and your return address. This represents the Network Layer (IP addressing).
4. **The Mail Carrier (Data Link/Physical)**: The local post truck picks up the mail (Ethernet/cables) and ships it.
5. **Intermediate Sorting Offices (Routers)**: The letter goes through airport postal hubs. The hubs don't read your letter — they only look at the city and zip code to decide which truck or plane it boards next (IP Routing).
6. **Delivery & Unboxing (Reassembly)**: Your friend gets the letter, slides it out of the envelope, and reads it.
""",
        "quiz": [
            {
                "question": "What does the IP in IP Address stand for?",
                "options": {
                    "A": "Intranet Protocol",
                    "B": "Internet Protocol",
                    "C": "Internal Pathway",
                    "D": "Instant Packet"
                },
                "correct_answer": "B",
                "explanation": "IP stands for Internet Protocol, which is the network-layer protocol responsible for addressing and routing data packets."
            },
            {
                "question": "Which of the following layers of the OSI model is responsible for routing packets based on IP addresses?",
                "options": {
                    "A": "Physical Layer",
                    "B": "Transport Layer",
                    "C": "Network Layer",
                    "D": "Application Layer"
                },
                "correct_answer": "C",
                "explanation": "The Network Layer (Layer 3) handles routing, IP addressing, and packet forwarding across different networks."
            },
            {
                "question": "What is the primary difference between TCP and UDP protocols?",
                "options": {
                    "A": "TCP is wireless; UDP requires fiber optic cables.",
                    "B": "TCP is connection-oriented and guarantees reliable packet delivery; UDP is connectionless and fast but does not guarantee delivery.",
                    "C": "TCP is only for websites; UDP is only for databases.",
                    "D": "TCP is an older protocol that is no longer used."
                },
                "correct_answer": "B",
                "explanation": "TCP ensures error correction and order-guaranteed delivery (used for emails, web browsing), while UDP shoots packets rapidly without overhead (used for video streaming, live gaming)."
            },
            {
                "question": "What is the purpose of a DNS (Domain Name System)?",
                "options": {
                    "A": "To encrypt website passwords.",
                    "B": "To translate human-friendly domain names (like google.com) into machine-readable IP addresses (like 142.250.190.46).",
                    "C": "To block virus downloads.",
                    "D": "To speed up local printer connections."
                },
                "correct_answer": "B",
                "explanation": "DNS is often referred to as the phonebook of the internet, converting domain names into physical IP routing destinations."
            },
            {
                "question": "Which port is conventionally reserved for secure encrypted web traffic (HTTPS)?",
                "options": {
                    "A": "80",
                    "B": "21",
                    "C": "443",
                    "D": "22"
                },
                "correct_answer": "C",
                "explanation": "Port 443 is the standard port for Secure HTTP (HTTPS), while Port 80 is used for unencrypted standard HTTP traffic."
            }
        ],
        "keywords": ["protocol", "packet", "ip", "tcp", "udp", "router", "dns", "osi", "layer", "http"],
        "guide": "Computer Networks share digital resources using standard protocols. The OSI model outlines 7 communication layers, spanning physical links to user interfaces."
    }
}


def explain_topic(topic: str) -> str:
    """Returns a simplified educational explanation for the given topic."""
    normalized = topic.strip().lower()
    
    # Check if we have exact or substring matches
    for key, data in OFFLINE_DATA.items():
        if key in normalized or normalized in key:
            return data["explanation"]
            
    # Generic intelligent fallback
    return f"""### 📘 Exploring the Topic: **{topic.title()}**

Welcome to your offline learning session! Although we are offline, we can break down **{topic}** into fundamental components.

#### 🗝️ Core Foundations of {topic.title()}
1. **Primary Purpose**: Every concept exists to solve a specific problem or explain a phenomenon. For **{topic}**, the core focus is organizing rules, managing elements, or structuring interactions to achieve a specific outcome.
2. **How it Works**: It divides processes into discrete steps or modules. By establishing clear rules and relationships, {topic} eliminates chaos and provides predictable results.
3. **Why it Matters**: Understanding this topic is critical because it forms the building block for more advanced systems, algorithms, or natural processes in this domain.

#### ⚙️ Standard Framework:
* **The Inputs**: What elements, data, or energy go into the system of {topic}?
* **The Processes**: How are these elements structured, manipulated, or transformed?
* **The Outputs**: What is the final result or state after {topic} has been applied?
"""


def real_life_example(topic: str) -> str:
    """Returns a real-life analogy/example for the topic."""
    normalized = topic.strip().lower()
    
    for key, data in OFFLINE_DATA.items():
        if key in normalized or normalized in key:
            return data["real_life_example"]
            
    # Generic intelligent fallback
    return f"""### 📖 Real-Life Analogy: The Orchestrated Project

To understand **{topic.title()}** without complex jargon, let's look at a relatable real-life scenario:

#### 🏢 The Scenario: Organizing a Massive Community Library
Imagine you are asked to organize a community hall filled with **10,000 random books** thrown in piles on the floor.

* **The Problem**: If someone wants to find a book about "Cooking", they would have to search every pile, taking hours (**Inefficient State**).
* **The {topic.title()} Solution**:
  - You implement **{topic.title()}** rules. You set up labeled bookshelves, split the books into genres (Categories), sort them alphabetically, and create a physical ledger index near the entrance.
  - Now, anyone can walk in, read the signs, and walk directly to their book in less than 30 seconds!
* **The Lesson**: In the same way, **{topic.title()}** provides the structure, categorization, and flow-control rules that prevent clutter and make interactions orderly, fast, and scalable in its environment.
"""


def generate_quiz(topic: str) -> list:
    """Generates exactly 5 multiple choice questions for the given topic."""
    normalized = topic.strip().lower()
    
    for key, data in OFFLINE_DATA.items():
        if key in normalized or normalized in key:
            return data["quiz"]
            
    # Generic intelligent fallback
    return [
        {
            "question": f"What is the ultimate primary goal of applying {topic.title()} in a system?",
            "options": {
                "A": "To maximize entropy, complexity, and random errors.",
                "B": "To organize elements, optimize processes, and solve problems systematically.",
                "C": "To replace all human programmers and users immediately.",
                "D": "To permanently delete historical data."
            },
            "correct_answer": "B",
            "explanation": f"At its core, {topic.title()} is utilized to bring organization, efficiency, and structural integrity to its domain."
        },
        {
            "question": f"Which of the following is a fundamental characteristic of {topic.title()}?",
            "options": {
                "A": "It relies on defined rules, modules, inputs, or relationships.",
                "B": "It operates entirely without any energy, resource, or logic constraint.",
                "C": "It is purely theoretical and has absolutely no practical application.",
                "D": "It must only be written on paper and never implemented on computers."
            },
            "correct_answer": "A",
            "explanation": f"All organized processes like {topic.title()} operate under specific governing guidelines, parameters, or logical states."
        },
        {
            "question": f"Why is scaling a challenge when dealing with {topic.title()}?",
            "options": {
                "A": "Because smaller elements are heavier.",
                "B": "Because as size increases, managing complexity and resource constraints becomes exponentially harder.",
                "C": "Because the concept becomes completely invalid in different cities.",
                "D": "Because computers refuse to process larger numbers."
            },
            "correct_answer": "B",
            "explanation": "Scale-complexity is a universal engineering challenge. Larger loads demand robust, well-designed architectures."
        },
        {
            "question": f"Which of the following represents the best practice when mastering {topic.title()}?",
            "options": {
                "A": "Memorizing superficial structures without understanding underlying mechanics.",
                "B": "Breaking down the concept to basic fundamentals, analyzing analogies, and doing practical exercises.",
                "C": "Assuming the concept is perfect and never has any edge cases.",
                "D": "Using it on every single project, even when simple alternatives are far better."
            },
            "correct_answer": "B",
            "explanation": "Mastery of any educational topic comes from deep conceptual understanding, analogy-mapping, and targeted problem practice."
        },
        {
            "question": f"What is the benefit of using modular, structured patterns in {topic.title()}?",
            "options": {
                "A": "It makes debugging, maintenance, and logical updates much easier.",
                "B": "It increases file sizes and slows down the CPU.",
                "C": "It prevents users from reading the content.",
                "D": "It requires dual-monitor setups to run."
            },
            "correct_answer": "A",
            "explanation": "Modular separation divides complex architectures into small, independent pieces, making updates and debugging straightforward."
        }
    ]


def evaluate_answer(topic: str, answer: str) -> dict:
    """
    Evaluates the user's answer for a given topic using keyword matching
    and heuristic rule-based logic.
    """
    normalized = topic.strip().lower()
    answer_clean = answer.strip().lower()
    
    # 1. Base Checks
    if len(answer_clean) < 10:
        return {
            "score": 20,
            "feedback": "Your answer is extremely brief.",
            "mistakes": "The response lacks detail, descriptions, or core terminology.",
            "suggestions": "Try to write at least 2-3 full sentences. Explain the 'how' and 'why' of the topic.",
            "encouragement": "Don't worry! Deep learning is iterative. Try expanding your response by explaining what the topic does and how it is structured!"
        }
        
    # Find matching data to extract keywords
    target_keywords = []
    target_guide = ""
    matched = False
    
    for key, data in OFFLINE_DATA.items():
        if key in normalized or normalized in key:
            target_keywords = data["keywords"]
            target_guide = data["guide"]
            matched = True
            break
            
    if not matched:
        # Generate dynamic keywords from the topic string
        words = [w for w in normalized.split() if len(w) > 3]
        target_keywords = words + ["system", "process", "rule", "structure", "data", "efficient", "solve"]
        target_guide = f"A valid explanation of {topic} detailing its core goals, components, and practical applications."

    # 2. Key Term Matching Heuristics
    matched_keywords = [kw for kw in target_keywords if kw in answer_clean]
    keyword_ratio = len(matched_keywords) / max(len(target_keywords), 1)
    
    # 3. Structural Analysis Heuristics
    has_example = any(ex in answer_clean for ex in ["example", "analogy", "like", "such as", "imagine", "scenario"])
    has_complexity_or_structure = any(comp in answer_clean for comp in ["time", "space", "complexity", "structure", "step", "rule", "element", "node"])
    
    # Compute score (out of 100)
    score = 30  # Baseline for trying
    score += int(keyword_ratio * 40)  # Keyword presence (up to 40 pts)
    if has_example:
        score += 15  # Gives a nice bonus for illustrating with examples
    if has_complexity_or_structure:
        score += 15  # Gives a nice bonus for structural or performance details
        
    score = min(score, 100)
    
    # Build Feedback
    feedback = f"Great effort! You successfully included key concepts in your description." if score >= 70 else "You have a basic start, but your explanation could benefit from more precise terminology."
    
    mistakes = []
    if len(matched_keywords) < 2:
        mistakes.append("Missing core technical vocabulary that defines this specific topic.")
    if not has_example:
        mistakes.append("Your response lacks concrete real-life examples or analogies to ground the theory.")
    if not has_complexity_or_structure:
        mistakes.append("No discussion on structural mechanics, rules, or performance characteristics (like speed or limits).")
        
    mistakes_str = " | ".join(mistakes) if mistakes else "None! Your structural outline is solid."
    
    # Suggestions
    suggestions = []
    if len(matched_keywords) < 3:
        missing_kw = [k for k in target_keywords if k not in matched_keywords][:3]
        suggestions.append(f"Incorporate important terms such as: {', '.join(missing_kw)}.")
    if not has_example:
        suggestions.append("Add a simple real-life analogy (e.g., 'This is like...') to demonstrate conceptual clarity.")
    if not has_complexity_or_structure:
        suggestions.append("Discuss how this topic operates step-by-step or mention its limitations/constraints.")
    suggestions.append(f"Compare your thoughts with the reference guide: \"{target_guide}\"")
    
    # Encouragement
    if score >= 85:
        encouragement = "Outstanding! You have a very clear, professional grasp of this topic. Keep up the brilliant work!"
    elif score >= 65:
        encouragement = "Good job! You understand the key foundations. A little more technical precision will make your answers perfect!"
    else:
        encouragement = "Learning is a step-by-step journey. Review the 'Explain Topic' and 'Real-Life Example' tabs above, then rewrite your answer. You can do this!"
        
    return {
        "score": score,
        "feedback": feedback,
        "mistakes": mistakes_str,
        "suggestions": suggestions,
        "encouragement": encouragement
    }


def full_learning_session(topic: str) -> dict:
    """Compiles a complete structured learning curriculum for the topic."""
    explanation = explain_topic(topic)
    example = real_life_example(topic)
    quiz = generate_quiz(topic)
    
    summary = f"""* **Topic Focus**: {topic.title()}
* **Core Takeaway**: Structured processes are the key to managing complexity.
* **Analogy Recalled**: Physical catalogs, registrar structures, or street networks.
* **Efficiency Focus**: Selecting optimal paths to minimize waste and errors.
"""

    motivational_message = f"""🌟 **Your AI Tutor says**: 
Learning is about building neural connections. By reading the explanation of **{topic.title()}**, mapping it to a real-life analogy, and testing your mind with quizzes, you have stimulated active recall! Keep exploring, stay curious, and remember: every expert was once a beginner who refused to quit! 🚀"""

    return {
        "introduction": f"### 🎓 Welcome to the Full Learning Session for **{topic.title()}**\n\nWe have organized a complete, offline-compatible curriculum to take you from a complete beginner to a confident practitioner. Follow the steps sequentially!",
        "explanation": explanation,
        "real_life_example": example,
        "quiz": quiz,
        "summary": summary,
        "motivational_message": motivational_message
    }
