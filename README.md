# LeetCode-NoteBook-Python3


## Goal
Although the book will contain a bunch of problem solutions, we demand more. 
The notebook aims at helping us become skilled at solving problems using Data structures and Algorithms.
Instead of through hard working on problems again and again,
our motivation is to develop problem-solving skills wisely 
by applying and deveoping meta-skills such as abstracting, gouping, finding properties, connecting, comparing, evaluating, etc..
(Sounds like working with Category Theory, doesn't it?)
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
LeetCode problems are no more isolated individual problems,
but a repository of problems with hidden connections of similarity and variance.
We need to manage time wisely instead of work on everyone starting from problem #1 which is frustrating.
The repository are trainings for developing individual skills
and also for applying them flexibly and logically.
Moreover, the problems are putting together for abstracting the common procedures and steps for solving problems.

Although it will be slower at the beginning,
but it will become much faster at the end with additional gain of higher level abilities.


## Map
The knowledges are organized in groups "Analysis-Solutions", "Algorithms" and "Data-structures".
More than a structure, 
with time passing, we should have a virtual map in our brain for contents as nodes and connections as pathes.
That is, LeetCode problems are no more in a linearly ordered sequence,
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

Then one "Medium-Hard" problem per day:
They are essential problems closer to real daily problems.
They are more complexed problems composed of lower level problems with new restrictions,
which require us to play with a bunch of basic building blocks flexibly and logically.
Make sure to cover all "Top 100 Liked Questions" and "Top 100 Interview Questions".


## Time Management
Only spend less than 20-30 minutes for generating a solution without implementation.
See "How to come up with own solutions".

On one hand, 
it trains us to get used to the real interview scene.

On the other hand, 
remember our goal is to get the problem-solving ability throught the training.
Our time is valuable, we have to spend our time wisely.
We do not have to beat every question during the training by ourselves. 
No one knows everything when he is new.
The failure guides us to the next success by showing what knowledge do we need to make up, 
and what skills do we need to spend your time for.
See "How to check with other solutions".


## How to come up with own solutions
* Grab a piece of white paper.
* 90-10 stratege: 90% time for thinking, 10% time for coding.
* Read the description carefully.
* Find and write down input-output-functionality.
* Find and write down restrictions.
* Abstract tasks and information to higher level as a conceptuality.
* Determine what groups it belongs to.
* Connect to tricks commonly used for these groups and estimate if they help to make the tasks easier.
* Decompose the tasks into sub-tasks according to tricks and mark them down.
* Manipulate this optional solution with a general example to make sure it works.
* Find other solutions and repeat above steps, and then estimate their time-space complexity.
* Pick one solution and move on to implement.


## How to implement your own solutions
* Never start before coming up with own solutions.
* Open a notebook to write it down. It is where we make our hands dirty dealing with details.
* Bottom-up refinement with an example.
* Start with output or return, place them at different locations.
* Around return output to add functional blocks and comment briefly for how to come up with the return.
* Structure the blocks by cases or loops and comment briefly for each part.
* Add initializations.
* Add guards.
* Double check with the margin cases.
* Verify by drawing test cases and manipulating them with our code. Modify the code to handle the error.
* Use compiler knowledge on codes for possible optimization. 
* Optimize our codes by combining redundant, but sometimes it reduces readibility.


## After implementation
- #### Copy it to LeetCode and submit.
- #### Record bugs and do analysis.
- #### Check with other solutions for improvements.


## How to check with other solutions
- #### Benefit to check with standard solutions and those in "Discuss" (click "Most Votes" and only for 2 pages).
- #### Use "Debugger" to understand the solution step by step if necessary.
- #### Abstract their tricks to extend our tricks set for this topic.
- #### Evaluate and compare time-space complexity of all solutions.
- #### Mark the problem number down and review it in the near future.


## Tips
* Use filters. E.g., pick "Top 100 Liked Questions".
* Do not work on the problems with :-1: >> :+1:. 
* Only view discussion with :+1: >> :-1:.
* Do not connect the problem to a particular problem, but to a general category, because we have limited memory.
* Do not chase for conciseness intensively, they might not always optimize (estimate and mind-compile), but sacrifices the readability.
* We will be skilled at concise coding with the time going, but focus on solving with correctness and time-space complexity.
* Do not RUSH! The faster is the slower; The slower is the faster.
* Optimization and conciseness are different.
* Keep in mind the operations can be arranged in different structures, by trade off between readibility and conciseness.
* Instead of hacking on solving problems, it benefits by reviewing sloved problems as well as different solutions and evaluating them. 
* Understand the relationship of Data Structures, i.e., *Hash Table* with don't care values, then use *Set*.


## Content Table
- "Y" means both analysis and solutions are supplied
- "N" means only analysis is supplied
- "T-I" abbreviates "Top 100 Interview Questions"
- "T-100" abbreviates "Top 100 Liked Questions"
- "B" stands for "Building block"

### Array
| # | Title | Difficulty | Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0026 | Remove Duplicates from Sorted Array    | Easy   | B  | Two Pointers    | 27, 217 | << | Y | T-I |
| 0027 | Remove Element                         | Easy   | B  | Two Pointers    | 26      | << | N |     |
| 0080 | Remove Duplicates from Sorted Array II | Medium |    | Two Pointers    |         | >> | Y |     |
| 0217 | Contains Duplicate                     | Easy   | B  | Set, Hash Table | 26      | >> | Y | T-I |
| 0283 | Move Zeroes                            | Easy   | B  | Two Pointers    | 27      | >> | N | T-I |

### LinkedList
| # | Title | Difficulty |  Level | Algorithms | Related | :+1: :-1: | Solutions | Lists |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0019 | Remove Nth Node From End of List       | Medium |    |                 |         | >> |   | T-I |
| 0083 | Remove Duplicates from Sorted List     | Easy   |    |                 | 203, 26 | >> |   |     |
| 0141 | Linked List Cycle                      | Easy   | B  | Two Pointers    |         | >> | Y | T-I |
| 0143 | Reorder List                           | Medium |    |                 |         | >> |   |     |
| 0160 | Intersection of Two Linked Lists       | Easy   |    |                 | 206     | >> |   | T-I |
| 0203 | Remove Linked List Elements            | Easy   | B  | Reccursion      |         | >> | Y |     |
| 0206 | Reverse Linked List                    | Easy   | B  | Reccursion      |         | >> | Y | T-I |
| 0234 | Palindrome Linked List                 | Easy   |    | Two Pointers    | 143?    | >> |   | T-I |
| 0237 | Delete Node in a Linked List           | Easy   | B  |                 |         | << |   | T-I |
| 0876 | Middle of the Linked List              | Easy   | B  | Two Pointers    |         | >> | Y |     |



