# LeetCode-NoteBook-Python3


## Goal
Although the book will contain a bunch of problem solutions, we demand more. 
The notebook aims at helping us become skilled at solving problems using *Data structures*, *Algorithms* and tricks.
Instead of through hard working on problems again and again,
our motivation is to develop problem-solving skills wisely 
by applying and deveoping meta-skills such as abstracting, grouping, finding properties, connecting, comparing, evaluating, etc..
(Sounds like working with *Category Theory*, doesn't it?)
Parallelly, there will be a collection of common procedures and steps, guidelines and tips available.

Furthermore, through this project, 
we hope to collect and develop (usually by abstracting) strategy 
for developing meta-skills 
useful in developing problem-solving skills.
They can be viewed layer by layer vertically.
And horizontally, we need to supply common procedures and steps, guidelines and tips by abstracting.
These abilities and the strategy are common in other domains of materials.
The higher demand will motivate us through the journey.


## How to use LeetCode
Therefore,
*LeetCode* problems are no more isolated individual problems,
but a repository of problems with hidden connections of similarity and variance.
We need to manage time wisely instead of hacking on everyone starting from problem #1 which is frustrating.
Note *LeetCode* is not the place for learning fundamental concepts, we should do that before starting *LeetCode*.
The repository are trainings for developing individual skills
and also for applying them flexibly and logically.
Moreover, the problems are putting together for abstracting the common procedures and steps for solving problems.

Although it will be slower at the beginning,
but it will become much faster at the end with additional gain of higher level abilities.


## Map
The knowledges are organized in groups of "Analysis-Solutions", "Algorithms" and "Data-structures".
More than a structure, 
with time passing, we should have a virtual map in our brain for contents as nodes and connections as pathes.
That is, *LeetCode* problems are no more in a linearly ordered sequence,
but a graph of nodes and connections.


## Schedule 
One month on "Easy" questions:
They provide us the chance for understanding and getting familiar with concepts and properties.
They are for developing individual basic skills and tricks for the future.
They are the start point of the journey for expanding our power. 
But we do not have to go through all of them, 
since many of them are not worth spending much efforts (See [Tips](#tips)).
Therefore we start with questions for fundamental concepts and skills.
And then make sure to cover all "Top 100 Liked Questions" and "Top 100 Interview Questions".
We focus on coding skills.

Then one "Medium-Hard" problem per day:
They are essential problems closer to real daily problems.
They are more complexed problems composed of lower level problems with new restrictions,
which require us to play with a bunch of basic building blocks flexibly and logically.
Make sure to cover all "Top 100 Liked Questions" and "Top 100 Interview Questions".
We focus on solutions.


## Time Management
Only spend less than 20-30 minutes for generating a solution without implementation.
See "How to come up with own solutions".

On one hand, 
it trains us to get used to the real interview scene.

On the other hand, 
remember our goal is to get the problem-solving ability through the training.
Our time is valuable, we have to spend our time wisely.
We do not have to beat every question by our own during the training. 
No one knows everything when he is growing.
The failure guides us to the next success by showing what knowledge do we need to make up, 
and what skills do we need to spend our time for.
See "How to check with other solutions".


## How to come up with own solutions
* Grab a piece of white paper.
* 90-10 stratege: 90% time for thinking, 10% time for coding.
* Read the description carefully.
* Find and write down *input-output-functionality*.
* Find and write down restrictions.
* Abstract tasks and information to higher level as a conceptuality.
* Determine which group it belongs to.
* Connect to *Data Structures*, *Algorithms* and tricks commonly used for the group and estimate if they help to make the tasks easier.
* Manipulate this optional solution with a general example to make sure it works.
* Find other solutions and repeat above steps, and then estimate their *time / space complexity*.
* Pick one solution and decompose the tasks into sub-tasks according to your chosen tools and mark them down.
* Move on to "How to implement your own solutions".


## How to implement your own solutions
* Never start before coming up with own solutions.
* Open a notebook to write it down. It is where we make our hands dirty dealing with details.
* Bottom-up refinement with an example.
* Start with output or return, place them at different locations.
* Around return output to add code blocks for it and comment briefly for how to come up with the return.
* Structure the blocks by cases or loops and comment briefly for each one.
* Add initializations.
* Add *guards*.
* Double check with the *margin cases*.
* Verify by drawing test cases and manipulating them with our code. Modify the code to handle the error.
* Use compiler knowledge on codes for possible optimization. 
* Optimize (make concise) our codes by combining redundant, but sometimes it reduces readibility.
* Move on to "After implementation".


## After implementation
- #### Copy it to *LeetCode* and submit.
- #### Record bugs you couldn't find and do reasoning.
- #### Check with otherones answers for improvements.
- #### Move on to "How to check with other solutions".


## How to check with other solutions
- #### Benefit to check with standard solutions and also those in "Discuss" (click "Most Votes" and only for <=2 pages).
- #### Use "Debugger" to understand the solution step by step if necessary.
- #### Abstract their tricks and find out how to come up with the tricks from the questions, then also extend our tricks set for this topic.
- #### Evaluate and compare *time / space complexity* of all solutions.
- #### Mark the problem number down and review it in the near future.


## Tips
* Use filters. E.g., pick "Top 100 Liked Questions".
* Do not work on the problems with :-1: >> :+1:. It doesn't mean the problem is "bad", but it is too easy for doing, if you have worked out "T-I".
* Only view discussion with :+1: >> :-1:.
* Do not connect the problem to a particular problem, but to a general category, because we have limited memory.
* Optimization and conciseness are different.
* Understand the relationship of *Data Structures*, i.e., *Hash Table* with don't care values, then use *Set*.
* Keep in mind the operations can be arranged in different structures, by trade off between readibility and conciseness.
* Conciseness might not always help optimization (which is by estimating complexity and mind-compiling), but sacrifice the readability.
* We will be skilled at conciseness automatically with the time going, but focus on correctness and *time / space complexity*.
* Do not RUSH! The faster is the slower; The slower is the faster.
* Instead of hacking on solving problems, it benefits from reviewing sloved problems as well as otherones solutions and evaluating them. 


## Content Table

*Note we supply solutions as much as possible for inspiration, 
but please estimate if it satisfies the question restrictions.*

### Abbreviations:
- "I" stands for Implementations are supplied, which take the training for coding skills
- "A" stands for Analysis are supplied, which take the training for coming up solutions, and also the overview of all solutions
- "N" stands no work, either because the analysis is straight forward, or the problem is a slightly alternate to a problem already seen. Also skip coding training
- "T-I" stands "Top 100 Interview Questions"
- "T-100" stands "Top 100 Liked Questions"
- "E" stands for "Building blocks", because they are from LeetCode category "Easy"
- "E+" stands for "Requiring changes on Building blocks", also from LeetCode category "Easy"
- "BFS" stands for "Breadth-First Search"
- "BM" stands for "Bit Manipulation"
- "BS" stands for "Binary Search"
- "DC" stands for "Divide and Conquer"
- "DP" stands for "Dynamic Programming"
- "DFS" stands for "Depth-First Search"
- "GR" stands for "Greedy"
- "HT" stands for "Hash Tables"
- "LI" stands for "List"
- "REC" stands for "Recursion"
- "SO" stands for "Sorting"
- "TP" stands for "Two Pointers"
- "* " stands for "Incomplete"
- ":star:" stands for fundamental tasks from LeetCode category "Easy"
- ":star::star:" stands for fundamental tasks from LeetCode category "Easy", but with a little bit change on ":star:"


### Array
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0001 | Two Sum                                | Easy   | :star:       | HT             |         | >> | N  | T-I |
| 0026 | Remove Duplicates from Sorted Array    | Easy   | :star::star: | TP             | 27      | << | AI | T-I |
| 0053 | Maximum Subarray                       | Easy   | :star:       | DC, DP, GR     | 121     | >> | N  | T-I |
| 0088 | Merge Sorted Array                     | Easy   | :star:       | TP             | 21      | <  | A  | T-I |
| 0121 | Best Time to Buy and Sell Stock        | Easy   | :star::star: | DC, DP, GR     | 53      | >> | N  | T-I |
| 0122 | Best Time to Buy and Sell Stock II     | Easy   | :star:       | GR             |         | >> | N  | T-I |
| 0136 | Single Number                          | Easy   | :star:       | HT, SO, BM, MA | 242     | >> | A  | T-I |
| 0169 | Majority Element                       | Easy   | :star:       | HT, SO, DC, REC|         | >> | N  | T-I |
| 0217 | Contains Duplicate                     | Easy   | :star:       | SO, Set, HT    |         | >> | AI | T-I |
| 0283 | Move Zeroes                            | Easy   | :star::star: | TP             | 27      | >> | A  | T-I |
| 0350 | Intersection of Two Arrays II          | Easy   | :star:       | TP, BS, HT, SO |         | >> | N  | T-I |


### String
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0014*| Longest Common Prefix                    | Easy   | :star:       | DC, BS  |         | >> | A  | T-I |
| 0020 | Valid Parentheses                        | Easy   | :star:       | STK     |         | >> | N  | T-I |
| 0028 | Implement strStr()                       | Easy   | :star:       | TP      |         | =  | A  | T-I |
| 0038 | Count and Say                            | Easy   |              |         |         | <  | N  | T-I |
| 0125 | Valid Palindrome                         | Easy   | :star::star: | TP      | 304,709 | << | N  | T-I |
| 0242 | Valid Anagram                            | Easy   | :star::star: | SO      | 217     | >> | AI | T-I |
| 0344 | Reverse String                           | Easy   | :star:       | TP, REC | 27      | >> | AI | T-I |
| 0387 | First Unique Character in a String       | Easy   | :star:       | HT, Set |         | >> | N  | T-I |


### LinkedList
| # | Title | Difficulty |  Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0021 | Merge Two Sorted Lists                 | Easy   | :star:       | TP, REC | 88       | >> | I  | T-I |
| 0141 | Linked List Cycle                      | Easy   | :star:       | TP, Set |          | >> | AI | T-I |
| 0160 | Intersection of Two Linked Lists       | Easy   | :star:       | TP, Set |          | >> | A  | T-I |
| 0206 | Reverse Linked List                    | Easy   | :star:       | REC     |          | >> | AI | T-I |
| 0234*| Palindrome Linked List                 | Easy   | :star::star: | TP, REC | 206, 876 | >> | A  | T-I |
| 0237 | Delete Node in a Linked List           | Easy   | :star:       |         |          | << | N  | T-I |


### Math & Stack
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0007 | Reverse Integer                        | Easy   | :star:       |           | 326      | <  | N  | T-I |
| 0013 | Roman to Integer                       | Easy   |              |           |          | <  | N  | T-I |
| 0069 | Sqrt(x)                                | Easy   | :star:       | BS, BM    | 367      | <  | N  | T-I |
| 0070 | Climbing Stairs                        | Easy   | :star:       | DC, REC   | 509      | >> | AI | T-I |
| 0171 | Excel Sheet Column Number              | Easy   | :star:       |           |          | >> | N  | T-I |
| 0172 | Factorial Trailing Zeroes              | Easy   | :star:       |           |          | =  | N  | T-I |
| 0202 | Happy Number                           | Easy   | :star:       | HT, Set   |          | >> | I  | T-I |
| 0204 | Count Primes                           | Easy   | :star:       | HT        |          | >> | N  | T-I |
| 0268 | Missing Number                         | Easy   | :star:       | BM, SO, HT|          | =  | N  | T-I |
| 0326 | Power of Three                         | Easy   | :star:       |           |          | << | N  | T-I |


### Tree
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0101 | Symmetric Tree                             | Easy   | :star:       | BFS, DFS      |        | >> |    | T-I |
| 0104 | Maximum Depth of Binary Tree               | Easy   | :star:       | BFS, DFS, REC |        | >> |    | T-I |
| 0108 | Convert Sorted Array to Binary Search Tree | Easy   | :star:       | BFS, DFS      |        | >> |    | T-I |



### Non Top 100 Interview Questions

### Array
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0027 | Remove Element                           | Easy   | :star:       | TP             |         | << | A  |     |
| 0035 | Search Insert Position                   | Easy   | :star:       | BS, REC        | 704     | >> | N  |     |
| 0080 | Remove Duplicates from Sorted Array II   | Medium | :star::star: | TP             | 26      | >> | AI |     |
| 0167 | Two Sum II - Input array is sorted       | Easy   | :star::star: | TP, BS, HT     | 1       | >> | I  |     |
| 0349 | Intersection of Two Arrays               | Easy   |              | TO, BS, SO, Set| 350     | << | N  |     |
| 0448 | Find All Numbers Disappeared in an Array | Easy   |              |                |         | >> |    |     |
| 0704 | Binary Search                            | Easy   | :star:       | BS, REC        | 35      | >> | N  |     |
| 0724 | Find Pivot Index                         | Easy   |              |                |         | >> |    |     |
| 0905 | Sort Array By Parity                     | Easy   |              |                |         | >> |    |     |

### String
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0205 | Isomorphic Strings                       | Easy   |              |         |         | >> |    |     |
| 0290 | Word Pattern                             | Easy   |              |         |         | >> |    |     |
| 0557 | Reverse Words in a String III            | Easy   | :star:       |         |         | >> | N  |     |
| 0771 | Jewels and Stones                        | Easy   |              |         |         | >> |    |     |
| 0844 | Backspace String Compare                 | Easy   | :star:       | TP, STK |         | >> | N  |     |
| 1002 | Find Common Characters                   | Easy   |              | HT      |         | >> | N  |     |
| 1047 | Remove All Adjacent Duplicates In String | Easy   | :star:       | STK     |         | >> |    |     |

### LinkedList
| # | Title | Difficulty |  Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0083 | Remove Duplicates from Sorted List     | Easy   | :star::star: | REC     | 203, 26  | >> | I  |     |
| 0203 | Remove Linked List Elements            | Easy   | :star:       | REC     |          | >> | AI |     |
| 0876 | Middle of the Linked List              | Easy   | :star:       | TP, LI  |          | >> | AI |     |


### Math & Stack
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0118 | Pascal's Triangle                      | Easy   |              |          |          | >> |    |     |
| 0119 | Pascal's Triangle II                   | Easy   |              |          |          | >> |    |     |
| 0155 | Min Stack                              | Easy   | :star:       | STK      |          | >> |    |     |
| 0190 | Reverse Bits                           | Easy   | :star:       | TP, BM   |          | >> | N  |     |
| 0191 | Number of 1 Bits                       | Easy   |              | BM       |          | >  |    |     |
| 0232 | Implement Queue using Stacks           | Easy   | :star:       | STK, QU  |          | >> |    |     |
| 0367 | Valid Perfect Square                   | Easy   | :star:       | BS       | 69       | >> | N  |     |
| 0374 | Guess Number Higher or Lower           | Easy   | :star:       | BS       | 704      | <  | N  |     |
| 0389 | Find the Difference                    | Easy   | :star:       | BM, HT   |          | >> | N  |     |
| 0509 | Fibonacci Number                       | Easy   | :star:       | REC, DP  | 70       | >  | N  |     |
| 0566 | Reshape the Matrix                     | Easy   |              |          |          | >  |    |     |
| 0674 | Longest Continuous Increasing Subsequence| Easy | :star:       | TP, DP   |          | >> | N  |     |
| 0746 | Min Cost Climbing Stairs               | Easy   | :star:       | DP       |          | >> | N  |     |
| 0766 | Toeplitz Matrix                        | Easy   |              |          |          | >> |    |     |
| 0832 | Flipping an Image                      | Easy   |              |          |          | >> |    |     |
| 0867 | Transpose Matrix                       | Easy   |              |          |          | =  |    |     |

### Tree
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0100 | Same Tree                                  | Easy   |              |               |        | >> |    |     |
| 0107 | Binary Tree Level Order Traversal II       | Easy   |              |               |        | >> |    |     |
| 0112 | Path Sum                                   | Easy   |              |               |        | >> |    |     |
| 0226 | Invert Binary Treee                        | Easy   |              |               |        | >> |    |     |
| 0404 | Sum of Left Leaves                         | Easy   |              |               |        | >> |    |     |
| 0559 | Maximum Depth of N-ary Tree                | Easy   |              |               |        | >> |    |     |
| 0572 | Subtree of Another Tree                    | Easy   |              |               |        | >> |    |     |
| 0700 | Search in a Binary Search Tree             | Easy   |              |               |        | >> |    |     |
| 0872 | Leaf-Similar Trees                         | Easy   |              |               |        | >> |    |     |
| 0938 | Range Sum of BST                           | Easy   |              | REC           |        | >> |    |     |
| 0993 | Cousins in Binary Tree                     | Easy   |              |               |        | >> |    |     |


### Done before (NOT :+1: >> :-1:. Easy for doing, if you have worked out "T-I".)
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0058 | Length of Last Word                        | Easy   | :star:       |          |          | << | N  |     |
| 0066 | Plus One                                   | Easy   | :star:       |          |          | <  | N  |     |
| 0219 | Contains Duplicate II                      | Easy   |              |          |          | =  |    |     |
| 0345 | Reverse Vowels of a String                 | Easy   |              |          |          | << |    |     |
| 0383 | Ransom Note                                | Easy   |              |          |          | >  |    |     |
| 0412 | Fizz Buzz                                  | Easy   |              |          |          | <  |    |     |
| 0414 | Third Maximum Number                       | Easy   |              |          |          | << |    |     |
| 0434 | Number of Segments in a String             | Easy   |              |          |          | << |    |     |
| 0485 | Max Consecutive Ones                       | Easy   |              |          |          | >  |    |     |
| 0520 | Detect Capital                             | Easy   |              |          |          | >  |    |     |
| 0521 | Longest Uncommon Subsequence I             | Easy   |              |          |          | << |    |     |
| 0541 | Reverse String II                          | Easy   |              |          |          | << |    |     |
| 0551 | Student Attendance Record I                | Easy   |              |          |          | <  |    |     |
| 0561 | Array Partition I                          | Easy   |              |          |          | =  |    |     |
| 0589 | N-ary Tree Preorder Traversal              | Easy   |              |          |          | >  |    |     |
| 0605 | Can Place Flowers                          | Easy   |              |          |          | >  |    |     |
| 0657 | Robot Return to Origin                     | Easy   |              |          |          | >  |    |     |
| 0697 | Degree of an Array                         | Easy   |              |          |          | =  |    |     |
| 0705 | Design HashSet                             | Easy   |              |          |          | >  |    |     |
| 0706 | Design HashMap                             | Easy   |              |          |          | >> |    |     |
| 0709 | To Lower Case                              | Easy   | :star:       |          |          | << | N  |     |
| 0717 | 1-bit and 2-bit Characters                 | Easy   |              |          |          | << |    |     |
| 0804 | Unique Morse Code Words                    | Easy   |              |          |          | =  |    |     |
| 0819 | Most Common Word                           | Easy   |              |          |          | << |    |     |
| 0824 | Goat Latin                                 | Easy   |              |          |          | << |    |     |
| 0830 | Positions of Large Groups                  | Easy   |              |          |          | >  |    |     |
| 0859 | Buddy Strings                              | Easy   |              |          |          | >  |    |     |
| 0888 | Fair Candy Swap                            | Easy   |              |          |          | >  |    |     |
| 0893 | Groups of Special-Equivalent Strings       | Easy   |              |          |          | << |    |     |
| 0896 | Monotonic Array                            | Easy   |              |          |          | >  |    |     |
| 0965 | Univalued Binary Tree                      | Easy   |              |          |          | >  |    |     |
| 1160 | Find Words That Can Be Formed by Characters| Easy   |              |          |          | >  |    |     |
| 1189 | Maximum Number of Balloons                 | Easy   |              |          |          | >  |    |     |
| 1207 | Unique Number of Occurrences               | Easy   |              |          |          | >  |    |     |


### Todo (for up >> down and up > 1000) For practicing topics if needed
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0009 | Palindrome Number                          | Easy   |              |               |        | >> |    |     |
| 0067 | Add Binary                                 | Easy   |              |               |        | >> |    |     |
| 0168 | Excel Sheet Column Title                   | Easy   |              |               |        | >> |    |     |
| 0175 | Combine Two Tables                         | Easy   |              |               |        | >> |    |     |
| 0231 | Power of Two                               | Easy   |              |               |        | >> |    |     |
| 0235 | Lowest Common Ancestor of a BST            | Easy   |              |               |        | >> |    |     |
| 0278 | First Bad Version                          | Easy   |              |               |        | >> |    |     |
| 0392 | Is Subsequence                             | Easy   |              |               |        | >> |    |     |
| 0409 | Longest Palindrome                         | Easy   |              |               |        | >> |    |     |
| 0415 | Add Strings                                | Easy   |              |               |        | >> |    |     |
| 0459 | Repeated Substring Pattern                 | Easy   |              |               |        | >> |    |     |
| 0461 | Hamming Distance                           | Easy   |              |               |        | >> |    |     |
| 0463 | Island Perimeter                           | Easy   |              |               |        | >> |    |     |
| 0476 | Number Complement                          | Easy   |              |               |        | >> |    |     |
| 0501 | Find Mode in Binary Search Tree            | Easy   |              |               |        | >> |    |     |
| 0530 | Minimum Absolute Difference in BST         | Easy   |              |               |        | >> |    |     |
| 0543 | Diameter of Binary Tree                    | Easy   |              |               |        | >> |    |     |
| 0617 | Merge Two Binary Trees                     | Easy   |              |               |        | >> |    |     |
| 0628 | Maximum Product of Three Numbers           | Easy   |              |               |        | >> |    |     |
| 0637 | Average of Levels in Binary Tree           | Easy   |              |               |        | >> |    |     |
| 0665 | Non-decreasing Array                       | Easy   |              |               |        | >> |    |     |
| 0653 | Two Sum IV - Input is a BST                | Easy   |              |               |        | >> |    |     |
| 0669 | Trim a Binary Search Tree                  | Easy   |              |               |        | >> |    |     |
| 0680 | Valid Palindrome II                        | Easy   |              |               |        | >> |    |     |
| 0696 | Count Binary Substrings                    | Easy   |              |               |        | >> |    |     |
| 0703 | Kth Largest Element in a Stream            | Easy   |              |               |        | >> |    |     |
| 0733 | Flood Fill                                 | Easy   |              |               |        | >> |    |     |
| 0796 | Rotate String                              | Easy   |              |               |        | >> |    |     |
| 0821 | Shortest Distance to a Character           | Easy   |              |               |        | >> |    |     |
| 0929 | Unique Email Addresses                     | Easy   |              |               |        | >> |    |     |
| 0942 | DI String Match                            | Easy   |              |               |        | >> |    |     |
| 0953 | Verifying an Alien Dictionary              | Easy   |              |               |        | >> |    |     |
| 0977 | Squares of a Sorted Array                  | Easy   |              |               |        | >> |    |     |
| 0997 | Find the Town Judge                        | Easy   |              |               |        | >> |    |     |
| 1046 | Last Stone Weight                          | Easy   |              |               |        | >> |    |     |
| 1154 | Day of the Year                            | Easy   |              |               |        | >> |    |     |
| 1365 | How Many Numbers Are Smaller Than the Current Number| Easy |       |               |        | >> |    |     |
























