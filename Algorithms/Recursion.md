## General ideas

Recursion goes hand in hand with *loops*.
Sometimes we first figure out a solution using loops, and then convert the solution into Recursion by cases.

Recursion can be implemented starting with the **_base cases_**, followed by the **_inductive_** case. 

Each case will do some work, and then returns according to the type of the funciton.

**_base cases_** are where the function finishs.

**_inductive cases_** used to deal with the "partially correct" work.

Generally speaking, the inductive cases work by "decomposing - recomposing". 
That is, we decompose the component into the next lower level sub-components, 
pretend the sub-components are handled correctly, and then "combining" them correctly.

See 0203, 0206 for example.
