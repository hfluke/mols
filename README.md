# 3 Mutually Orthogonal Latin Squares of Order 36

### Latin Squares

A _Latin square_ is an $n \times n$ grid containing $n$ district elements in which each element occurs exactly once in each row and once in each column. For example, a Sudoku puzzle is a Latin square with the extra requirement that each $3 \times 3$ subset of the $9 \times 9$ puzzle must also contain each number 1 through 9 exactly once.

### Mutually Orthogonal Latin Squares (MOLS)

Two Latin squares are _mutually orthogonal_ if they are the same size and the corresponding gird cell of each Latin square do not contain the same element. Think of this as extending the Sudoku puzzle into three dimentions, (without the requirement that the third dimension must also contain 9 elements). You can learn more about mutually orthogonal Latin squares [here](https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Combinatorics_(Morris)/04%3A_Design_Theory/16%3A_Latin_Squares/16.02%3A_Mutually_Orthogonal_Latin_Squares_(MOLS)).

### Fun Fact

No mutually orthogonal Latin squares exist for a $6 \times 6$ grid. This problem is famously known as "Euler's Officers," and is attributed to Leonhard Euler, a mathematician born in 1707.

### Constructing my $36 \times 36$ MOLS 

I constructed my Latin squares using several abstract algebra theorems. I constructed a finite fields of order 9 and order 4. Additionally, I derived opperation tables for both finite fields. I was then able to create $n-1$ Latin squares for each finite field using the opperation tables. Each $36 \times 36$ MOLS was created by taking the Kronecker product of an order 9 Latin square with an order 4 Latin square. I want to thank Dr. David E. Brown for teaching me all the math I needed to know in order to create these Latin squares.
