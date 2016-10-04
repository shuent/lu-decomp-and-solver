# Program that Solve Equation with LU decomposition


While studying Linear Algebra, I wanted to solve equation in programing. and I googled and found out some method. LU decomposition is faster algorithm than Gauss-Jordan elimination, which you used to it with hand computation. 

### about
If there exist the linear equation, where $A$ is $N^2$ matrix,
$$  Ax=b $$
$A$ is decomposed with $L,U$
$$A = LU$$
so equation is rewrites
$$LUx=b$$
Then let $y=Ux$, equation can separate
$$Ly=b$$
$$Ux=y$$

solve $y$ and then you acquire $x$.

There are some method since it's not uniquely determined,
we use L and U this form. (in this example 3D matrix but applied nD)

all diagonal element is 1 in L.
$$
L = \begin{bmatrix}{}
      1 & 0 & 0 \\
      * & 1 & 0 \\
      * & * & 1
    \end{bmatrix}
    $$ 
    $$
U = \begin{bmatrix}
      * & * & * \\
      0 & * & * \\
      0 & 0 & *
    \end{bmatrix}
    $$ 
### LU decomposition
Now let's consider how to decompose A with L and U.
Take 3D matrix for explanation. Note that this is applied in n-dimmention that I don't verify the validity here. 

Take a look into each elements,

$$ A = LU$$

$$ \begin{bmatrix}{}
      a_{11} & a_{12} & a_{13} \\
      a_{21} & a_{22} & a_{23} \\
      a_{31} & a_{32} & a_{33}
    \end{bmatrix}
=
  \begin{bmatrix}{}
      1 & 0 & 0 \\
      l_{21} & 1 & 0 \\
      l_{31} & l_{32} & 1
    \end{bmatrix}
   \begin{bmatrix}
      u_{11} & u_{12} & u_{13} \\
      0 & u_{22} & u_{23} \\
      0 & 0 & u_{33}
    \end{bmatrix}
    $$ 

Compute LU,
 $$A=LU=
 \begin{bmatrix}
      u_{11} & u_{12} & u_{13} \\
      l_{21}u_{11} & l_{21}u_{21}+u_{22} & l_{21}u_{13}+u_{23} \\
      l_{31}u_{11} & l_{31}u_{12}+l_{32}u_{22} & l_{31}u_{13}+l_{32}u_{23}+u_{33}
    \end{bmatrix}
$$
General solution for  $a_{ij}$ is,

if $i>j$,
$$
a_{ij} = l_{ij}u_{jj}+\sum_{k=1}^{j-1} l_{jk} u_{kj}
$$
else $ i \le j$,
$$
a_{ij} = u_{ij}+\sum_{k=1}^{i-1} l_{jk} u_{kj}
$$

Thus $l_{ij},u_{ij}$ is obtained respectively.

### L Forward, U Backward substitution	

Once you finish decomposition, it is easy and faster ( I mean, for computer ) to calculate rest of equation.

First step is to solve $Ly = b$ for $y$
In augmented matrix,
 
 \begin{bmatrix}{}
      1 & 0 & 0 & b_1\\
      l_{21} & 1 & 0 &b_2\\
      l_{31} & l_{32} & 1 & b_3
    \end{bmatrix}
Since $L$ is "lower triangle matrix", you can solve this equation by "forward substitution": What you need is just substitute $b_i$ from the top.
General solution for y is,
$$ y_n=b_n - \sum_{k=1}^{n-1} l_{nk} y_k \ \ \ (n= 1,2,3,...,N)$$

Then you can solve $ Ux = y $ for $x$

\begin{bmatrix}
      u_{11} & u_{12} & u_{13} & y_1 \\
      0 & u_{22} & u_{23} & y_2 \\
      0 & 0 & u_{33} & y_3
    \end{bmatrix}

This time you will use "backward substitution" so solution is determined from bottom to top, for $U$ is "upper triangle matrix" .

General solution for x is,
$$
x_i = \frac{y_i-( \sum_{k=i+1}^N u_{ik} x_k )}{u_{ii}} \ \ \ \ \ (i = N,N-1,N-2, ..., 1)
$$

Thus, you get solution $x$.

#### why faster?
Compared to Gauss-Jordan, which every time calculation depend on right side of equation, once A is decomposed, LU is conserved. Next time you solve equation with matrix $A$, you can just focus on forward and backward substitution which is much faster. 


### Program

Now you can use above algorithm to develop program. But there are some caution. 

First when you decompose $A$, diagonal elements in $U$ should not be $0$ in order to avoid zero division error.  So in this program, in $A$ choose most highest absolute value from the pivot column and swap row and continue decomposition. Every time row operation follows this step.

Second, LU decomposition applies only $A = N^2$  matrix. Other than this type of matrix cannot solved so program error raise. 
