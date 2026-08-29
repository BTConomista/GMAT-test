# 700+ Data Sufficiency, con le spiegazioni di Bunuel

[<- I materiali](../README.md)

Trascrizione di `quant/ds-700-plus-bunuel.doc`, raccolto e risolto da **Bunuel**
su GMAT Club nel settembre 2010. Il *700+* del titolo e' la fascia di difficolta',
non il numero di domande: le domande sono **51**, numerate da 1 a 55 con
le 16-19 assenti gia' nella fonte.

Cambia solo la resa. Le formule, che nel .doc sono immagini servite da un CGI, sono
qui in LaTeX - lo stesso LaTeX che stava scritto nell'indirizzo dell'immagine. Il
testo e' quello di Bunuel, refusi compresi.

---

## 1. Probability / Combinatorics

If 2 different representatives are to be selected at random from a group of 10 employees
and if p is the probability that both representatives selected will be women, is p > 1/2

(1) More than 1/2 of the 10 employees are women.
(2) The probability that both representatives selected will be men is less than 1/10

What is the probability of choosing 2 women out of 10 people $\frac{w}{10}*\frac{w-1}{9}$ and this should be $>1/2$. So we have $\frac{w}{10}*\frac{w-1}{9}>\frac{1}{2}$ --> $w(w-1)>45$ this is true only when $w>7$. (w # of women $<=10$)

So basically question asks is $w>7$?

(1) $w>5$ not sufficient.

(2) $\frac{10-w}{10}*\frac{10-w-1}{9}<\frac{1}{10}$ --> $(10-w)(9-w)<9$ --> $w>6$, not sufficient

(1)+(2) $w>5$, $w>6$ not sufficient

Answer E.

You can use Combinations, to solve as well:

$C^2_w$ # of selections of 2 women out of $w$ employees;

$C^2_{10}$ total # of selections of 2 representatives out of 10 employees.

Q is $\frac{C^2_w}{C^2_{10}}>\frac{1}{2}$ --> $\frac{\frac{w(w-1)}{2}}{45}>\frac{1}{2}$ --> --> $w(w-1)>45$ --> $w>7$?

(1) $w>5$, not sufficient.

(2) $C^2_{(10-w)}$ # of selections of 2 men out of $10-w=m$ employees --> $\frac{C^2_{(10-w)}}{C^2_{10}}<\frac{1}{10}$ --> $\frac{\frac{(10-w)(10-w-1)}{2}}{45}<\frac{1}{10}$ --> $(10-w)(9-w)<9$ --> $w>6$, not sufficient

(1)+(2) $w>5$, $w>6$ not sufficient

Answer E.

[Discussione su GMAT Club](http://gmatclub.com/forum/difficulty-faced-during-test-89934.html)

---

## 2. Coordinate Geometry

If vertices of a triangle have coordinates (-1,0), (4,0), and (0,A) , is the area of the triangle greater than 15?
(1) A < 3
(2) The triangle is right

First of all right triangle with hypotenuse 5, doesn't mean that we have (3, 4, 5) right triangle. If we are told that values of all sides are integers, then yes: the only integer solution for right triangle with hypotenuse 5 would be (3, 4, 5).

To check this: consider the right triangle with hypotenuse 5 inscribed in circle. We know that a right triangle inscribed in a circle must have its hypotenuse as the diameter of the circle. The reverse is also true: if the diameter of the circle is also the triangle’s hypotenuse, then that triangle is a right triangle.

So ANY point on circumference of a circle with diameter $5$ would make the right triangle with diameter. Not necessarily sides to be $3$ and $4$. For example we can have isosceles right triangle, which would be 45-45-90: and the sides would be $\frac{5}{\sqrt{2}}$. OR if we have 30-60-90 triangle and hypotenuse is $5$, sides would be $2.5$and $2.5*\sqrt{3}$. Of course there could be many other combinations.

Back to the original question:
If vertices of a triangle have coordinates (-1,0), (4,0), and (0,A) , is the area of the triangle greater than 15?
(1) A < 3 --> two vertices are on the X-axis and the third vertex is on the Y-axis, below the point (0,3). The third vertex could be at (0,1) and the area would be less than 15 OR the third vertex could be at (0,-100) and the area would be more than 15. So not sufficient.

(2) The triangle is right. --> Obviously as the third vertex is on the Y-axis, the right angle must be at the third vertex. Which means the hypotenuse is on X-axis and equals to 5. Again if we consider the circle, the radius mus be 2.5 (half of the hypotenuse/diameter) and the third vertex must be one of two intersections of the circle with Y-axis. We'll get the two specific symmetric points for the third vertex, hence the area would be fixed and defined. Which means that it's possible to answer the question whether the area is more than 15, even not calculating actual value. Sufficient.

Answer: B.

If we want to know how the area could be calculated with the help of statement 2, here you go:

One of the approaches:

The equation of a circle is $(x - a)^2 + (y-b)^2 = r^2$, where $(a,b)$ is the center and $r$ is the radius.

We know:
$r=2.5$, as the hypotenuse is 5.
$a=1.5$ and $b=0$, as the center is on the X-axis, at the point $(1.5, 0)$, half the way between the (-1, 0) and (4, 0).
We need to determine intersection of the circle with Y-axis, or the point $(0, y)$ for the circle.

So we'll have $(0-1.5)^2 + (y-0)^2 =2.5^2$

$y^2=4$ --> $y=2$ and $y=-2$. The third vertex is either at the point $(0, 2)$ OR $(0,-2)$. In any case $Area=2*\frac{5}{2}=5$.

[Discussione su GMAT Club](http://gmatclub.com/forum/urgent-help-required-87344.html?hilit=only%20integer%20solution%20triangle#p656628)

---

## 3. Geometry

Is the perimeter of triangle ABC greater than 20?
(1) BC-AC=10.
(2) The area of the triangle is 20.

This problem could be solved knowing the following properties:

For (1):
The length of any side of a triangle must be larger than the positive difference of the other two sides, but smaller than the sum of the other two sides.

Now, as BC-AC=10 then BC>10 and also according to the above property the third side AB is also more than 10, so the perimeter is more than 20. Sufficient.

For (2):
A. For a given perimeter equilateral triangle has the largest area.
B. For a given area equilateral triangle has the smallest perimeter.

Let's assume the perimeter is 20. The largest area with given perimeter will have the equilateral triangle, so side=20/3. Let's calculate the area and if the area will be less than 20 it'll mean that perimeter must be more than 20.

$Area=s^2*\frac{\sqrt{3}}{4}=(\frac{20}{3})^2*\frac{\sqrt{3}}{4}=\frac{100*\sqrt{3}}{9}=~\frac{173}{9}<20$, ($\sqrt{3}\approx{1.73}$.) ( hence area is more than 20. Sufficient.

Answer: D.

[Discussione su GMAT Club](http://gmatclub.com/forum/perimeter-of-triangle-abc-87112.html)

---

## 4. Modulus / Inequalities

If x is not equal to 0, is |x| less than 1?
(1) x/|x|< x
(2) |x| > x


$x\neq{0}$, is $|x|<1$? Which means is $-1<x<1$? ($x\neq{0}$)

(1) $\frac{x}{|x|}< x$
Two cases:
A. $x<0$ --> $\frac{x}{-x}<x$ --> $-1<x$. But remember that $x<0$, so $-1<x<0$

B. $x>0$ --> $\frac{x}{x}<x$ --> $1<x$.

Two ranges $-1<x<0$ or $x>1$. Which says that $x$ either in the first range or in the second. Not sufficient to answer whether $-1<x<1$. (For instance $x$can be $-0.5$ or $3$)

OR: $\frac{x}{|x|}< x$ multiply both sides of inequality by $|x|$ (side note: we can safely do this as absolute value is non-negative and in this case we know it's not zero too) --> $x<x|x|$ --> $x(|x|-1)>0$:
Either $x>0$ and $|x|-1>0$, so $x>1$ or $x<-1$ --> $x>1$;
Or $x<0$ and $|x|-1<0$, so $-1<x<1$ --> $-1<x<0$.

The same two ranges: $-1<x<0$ or $x>1$.

(2) $|x| > x$. Well this basically tells that $x$ is negative, as if x were positive or zero then $|x|$ would be equal to $x$. Only one range: $x<0$, but still insufficient to say whether $-1<x<1$. (For instance $x$ can be $-0.5$ or $-10$)

Or two cases again:
$x<0$--> $-x>x$--> $x<0$.
$x>0$ --> $x>x$: never correct.


(1)+(2) Intersection of the ranges from (1) and (2) is the range $-1<x<0$ ($x<0$ (from 2) and $-1<x<0$ or $x>1$ (from 1), hence $-1<x<0$). Every $x$ from this range is definitely in the range $-1<x<1$. Sufficient.

Answer: C.

To demonstrate on diagram:
Range from (1): -----(-1)----(0)----(1)---- $-1<x<0$ or $x>1$, green area;

Range from (2): -----(-1)----(0)----(1)---- $x<0$, blue area;

From (1) and (2): ----(-1)----(0)----(1)---- $-1<x<0$, common range of $x$ from (1) and (2) (intersection of ranges from (1) and (2)), red area.

[Discussione su GMAT Club](http://gmatclub.com/forum/if-x-is-not-equal-to-0-is-x-less-than-86140.html)

---

## 5. Coordinate Geometry / Modulus

On the number line shown, is zero halfway between r and s

(1) s is to the right of zero
(2) The distance between t and r is the same as the distance between t and -s

NOTE:
In GMAT we can often see such statement: $k$ is halfway between $m$ and $n$. Remember this statement can ALWAYS be expressed as: $\frac{m+n}{2}=k$.

Also in GMAT we can often see another statement: The distance between $p$ and $m$ is the same as the distance between $p$ and $n$. Remember this statement can ALWAYS be expressed as: $|p-m|=|p-n|$.


Back to original question: is 0 halfway between r and s?
OR is $\frac{r+s}{2}=0$? --> Basically the question asks is $r+s=0$?

(1) $s>0$, clearly not sufficient.

(2) The distance between $t$ and $r$ is the same as the distance between $t$ and -$s$: $|t-r|=|t+s|$.

$t-r$ is always positive as $r$ is to the left of the $t$, hence $|t-r|=t-r$;

BUT $t+s$ can be positive (when $t>-s$, meaning $t$ is to the right of -$s$) or negative (when $t<-s$, meaning $t$ is to the left of -$s$, note that even in this case $s$ would be to the left of $t$ and relative position of the points shown on the diagram still will be the same). So we get either $|t+s|=t+s$ OR $|t+s|=-t-s$.

In another words: $t+s$ is the sum of two numbers from which one $t$, is greater than $s$. Their sum clearly can be positive as well as negative. Knowing that one is greater than another doesn't help to determine the sign of their sum.

Hence:
$t-r=t+s$ --> $-r=s$;
OR
$t-r=-t-s$ --> $2t=r-s$.

So the only thing we can determine from (2) is: $t-r=|t+s|$
Not sufficient.

(1)+(2) $s>0$ and $t-r=|t+s|$. $s>0$ --> $t>0$ (as $t$ is to the right of $s$) hence $t+s>0$. Hence $|t+s|=t+s$. --> $t-r=t+s$ --> $-r=s$. Sufficient.

Answer: C.

About the relative position of the points on diagram:

"In general, you should not trust the scale of GMAT diagrams, either in Problem Solving or Data Sufficiency. It used to be true that Problem Solving diagrams were drawn to scale unless mentioned otherwise, but I've seen recent questions where that is clearly not the case. So I'd only trust a diagram I'd drawn myself. ...

Here I'm referring only to the scale of diagrams; the relative lengths of line segments in a triangle, for example. ... You can accept the relative ordering of points and their relative locations as given (if the vertices of a pentagon are labeled ABCDE clockwise around the shape, then you can take it as given that AB, BC, CD, DE and EA are the edges of the pentagon; if a line is labeled with four points in A, B, C, D in sequence, you can take it as given that AC is longer than both AB and BC; if a point C is drawn inside a circle, unless the question tells you otherwise, you can assume that C is actually within the circle; if what appears to be a straight line is labeled with three points A, B, C, you can assume the line is actually straight, and that B is a point on the line -- the GMAT would never include as a trick the possibility that ABC actually form a 179 degree angle that is imperceptible to the eye, to give a few examples).

So don't trust the lengths of lines, but do trust the sequence of points on a line, or the location of points within or outside figures in a drawing. "

[Discussione su GMAT Club](http://gmatclub.com/forum/position-on-the-number-line-89015.html)

---

## 6. Inequalities

Are x and y both positive?
(1) 2x-2y=1
(2) x/y>1

(1) 2x-2y=1. Well this one is clearly insufficient. You can do it with number plugging OR consider the following: x and y both positive means that point (x,y) is in the I quadrant. 2x-2y=1 --> y=x-1/2, we know it's an equation of a line and basically question asks whether this line (all (x,y) points of this line) is only in I quadrant. It's just not possible. Not sufficient.

(2) x/y>1 --> x and y have the same sign. But we don't know whether they are both positive or both negative. Not sufficient.

(1)+(2) Again it can be done with different approaches. You should just find the one which is the less time-consuming and comfortable for you personally.

One of the approaches:
$2x-2y=1$ --> $x=y+\frac{1}{2}$
$\frac{x}{y}>1$ --> $\frac{x-y}{y}>0$ --> substitute x --> $\frac{1}{y}>0$ --> $y$ is positive, and as $x=y+\frac{1}{2}$, $x$ is positive too. Sufficient.

Answer: C.

NOTE:

$\frac{x}{y}>1$ does not mean that $x>y$. If both x and y are positive, then $x>y$, BUT if both are negative, then $x<y$.

From (2) $\frac{x}{y}>1$, we can only deduce that x and y have the same sigh (either both positive or both negative).

[Discussione su GMAT Club](http://gmatclub.com/forum/ds1-93964.html)

---

## 7. Inequalities / Word Problem

If 20 Swiss Francs is enough to buy 9 notebooks and 3 pencils, is 40 Swiss Francs enough to buy 12 notebooks and 12 pencils?
(1) 20 Swiss Francs is enough to buy 7 notebooks and 5 pencils.
(2) 20 Swiss Francs is enough to buy 4 notebooks and 8 pencils.

Given $9n+3p\leq20$, question is $12n+12p\leq40$ true? Or is $6n+6p\leq20$ true? So basically we are asked whether we can substitute 3 notebooks with 3 pencils. Now if $p<n$ we can easily substitute notebooks with pencils (equal number of notebooks with pencils ) and the sum will be lees than 20. But if $p>n$we won't know this for sure.

But imagine the situation when we are told that we can substitute 2 notebooks with 2 pencils. In both cases ($p<n$ or $p>n$) it would mean that we can substitute 1 (less than 2) notebook with 1 pencil, but we won't be sure for 3 (more than 2).


(1) $7n+5p\leq20$. We can substitute 2 notebooks with 2 pencils, but this not enough. Not sufficient.

(2) $4n+8p\leq20$. We can substitute 5 notebooks with 5 pencils, so in any case ($p<n$ or $p>n$) we can substitute 3 notebooks with 3 pencils. Sufficient.

Answer: B.

[Discussione su GMAT Club](http://gmatclub.com/forum/tricky-inequality-89226.html?hilit=swiss#p674919)

---

## 8. Word Problem

Ten years ago, scientists predicted that the animal z would become extinct in t years. What is t?
(1) Animal z became extinct 4 years ago.
(2) If the scientists had extended their extinction prediction for animal z by 3 years, their prediction would have been incorrect by 2 years.

(1) The only thing we can get from this statement is when animal z actually extincted: 4 years ago or 6 years after the prediction. Not sufficient.

(2) Also not sufficient: t+3=actual extinction +/- 2.

(1)+(2) Animals extincted 6 years after the prediction: t+3=6-2 --> t=1 OR t+3=6+2 --> t=5. Two answers, not sufficient.

Answer: E.

[Discussione su GMAT Club](http://gmatclub.com/forum/somewhat-confusing-problem-90379.html)

---

## 9. Modulus

If x and y are non-zero integers and |x| + |y| = 32, what is xy?
(1) -4x - 12y = 0
(2) |x| - |y| = 16

(1) $x+3y=0$ --> $x=-3y$ --> $x$ and $y$ have opposite signs --> so either $|x|=x$ and $|y|=-y$ OR $|x|=-x$ and $|y|=y$ --> either $|x|+|y|=-x+y=3y+y=4y=32$: $y=8$, $x=-24$, $xy=-24*8$ OR $|x|+|y|=x-y=-3y-y=-4y=32$: $y=-8$, $x=24$, $xy=-24*8$, same answer. Sufficient.

(2) $|x| - |y| = 16$. Sum this one with the equation given in the stem --> $2|x|=48$ --> $|x|=24$, $|y|=8$. $xy=-24*8$ (x and y have opposite sign) or $xy=24*8$ (x and y have the same sign). Multiple choices. Not sufficient.

Answer: A.

[Discussione su GMAT Club](http://gmatclub.com/forum/absolute-value-90031.html)

---

## 10. Number properties

If k is an integer greater than 1, is k equal to 2^r for some positive integer r?
(1) k is divisible by 2^6
(2) k is not divisible by any odd integer greater than 1

Given: $k=integer>1$, question is $k=2^r$.

Basically we are asked to determine whether $k$ has only 2 as prime factor in its prime factorization.

(1) $2^6*p=k$, if $p$ is a power of 2 then the answer is YES and if $p$ is the integer other than 2 in any power (eg 3, 5, 12...) then the answer is NO.

(2) $k$ is not divisible by any odd integers greater then 1. Hence $k$ has only power of 2 in its prime factorization. Sufficient.

Answer: B.

[Discussione su GMAT Club](http://gmatclub.com/forum/power-of-88539.html)

---

## 11. Inequalities

What is the value of integer x?
(1) 4 < (x-1)*(x-1) < 16
(2) 4 < (x+1)*(x-1) < 16

Note: $x$ is an integer.

(1) $4<(x-1)*(x-1)<16$ --> $4<(x-1)^2<16$ --> $(x-1)^2$ is a perfect square between 4 and 16 --> there is only one perfect square: 9 --> $(x-1)^2=9$ -->$x-1=3$ or $x-1=-3$ --> $x=4$ or $x=-2$. Two answers, not sufficient.

(2) $4<(x+1)*(x-1)<16$ --> $4<x^2-x+x-1<16$ --> $4<x^2-1<16$ --> $5<x^2<17$ --> $x^2$ is a perfect square between 5 and 17 --> there are two perfect squares : 9 and 16 --> $x^2=9$ or $x^2=16$ --> $x=3$ or $x=-3$ or $x=4$ or $x=-4$. Four answers, not sufficient.

(1)+(2) Intersection of values from (1) and (2) is $x=4$. Sufficient.

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/tough-inequation-ds-what-is-the-value-of-integer-x-93008.html)

---

## 12. Inequalities / Modulus

Is x>y>z??
(1) x-y = |x-z|+|z-y|
(2) x > y

(1) $x-y=|x-z|+|z-y|$

First of all as RHS is the sum of two non-negative values LHS also must be non-negative. So $x-y\geq{0}$.

Now, we are told that the distance between two points $x$ and $y$, on the number line, equals to the sum of the distances between $x$ and $z$ AND $z$ and $y$.

The question is: can the points placed on the number line as follows ---z---y---x---. If you look at the number line you'll see that it's just not possible. Sufficient.

OR algebraic approach:

If $x>y>z$ is true, then $x-y=|x-z|+|z-y|$, will become $x-y=x-z-z+y$ --> $z=y$, which contradicts our assumption $x>y>z$. So $x>y>z$ is not possible. Sufficient.

(2) $x>y$ --> no info about $z$. Not sufficient.

Answer: A.

[Discussione su GMAT Club](http://gmatclub.com/forum/is-x-y-z-92607.html)

---

## 13. Coordinate Geometry / Algebra

In the rectangular coordinate system, are the points (a, b) and (c, d) equidistant from the origin?
(1) $\frac{a}{b}=\frac{c}{d}$
(2) $\sqrt{a^2}+ \sqrt{b^2}  = \sqrt{c^2} + \sqrt{d^2}$


Distance between the point A (x,y) and the origin can be found by the formula: $D=\sqrt{x^2+y^2}$.

So we are asked is $\sqrt{a^2+b^2}=\sqrt{c^2+d^2}$? Or is $a^2+b^2=c^2+d^2$?

(1) $\frac{a}{b}=\frac{c}{d}$. Not sufficient.
(2) $\sqrt{a^2}+\sqrt{b^2}=\sqrt{c^2} +\sqrt{d^2}$ --> $|a|+|b|=|c|+|d|$. Not sufficient.

(1)+(2) $\frac{a}{b}=\frac{c}{d}$ and $|a|+|b|=|c|+|d|$.

From (1) $a=cx$ and $b=dx$, for some non-zero $x$. Substitute in (2) $|cx|+|dx|=|c|+|d|$ --> $|x|(|c|+|d|)=|c|+|d|$ --> $|x|=1$ (another solution $|c|+|d|=0$ is not possible as $d$ in (1) given in denominator and can not be zero, so $d\neq{0}$ --> $|c|+|d|>0$) --> so as $|x|=1$ and $a=cx$ and $b=dx$, then $|a|=|c|$ and $|b|=|d|$

Now square $|a|+|b|=|c|+|d|$ --> $a^2+2|a|*|b|+b^2=c^2+2|c|*|d|+d^2$ --> $a^2+2|a|*|b|+b^2=c^2+2|a|*|b|+d^2$ --> $2|a|*|b|$ cancels out --> $a^2+b^2=c^2+d^2$. Sufficient.

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/manhttangmat-practice-cat-92533.html)

---

## 14. Remainders

If w, x, y, and z are the digits of the four-digit number N, a positive integer, what is the remainder when N is divided by 9?
(1) w + x + y + z = 13
(2) N + 5 is divisible by 9

Remainder when a number is divided by 9 is the same as remainder when the sum of its digits is divided by 9:

$Remainder \frac{N}{9}=Remainder  \frac{w + x + y + z}{9}$

Let's show this on our example:

Our 4 digit number is $1000w+100x+10y+z$. what is the remainder when it's divided by 9?

When 1000w is divided by 9 the remainder is $\frac{w}{9}$:

$\frac{3000}{9}$ remainder $3$, $\frac{3}{9}$remainder $3$.

The same with $100x$ and $10y$.

So, the remainder when $1000w+100x+10y+z$ is divided by 9 would be:

$\frac{w}{9}+\frac{x}{9}+\frac{y}{9}+\frac{z}{9}=\frac{w+x+y+z}{9}$

(1) w + x + y + z = 13 --> remainder 13/9=4, remainder N/9=4. Sufficient.

(2) N+5 is divisible by 9 --> N+5=9k --> N=9k-5=4, 13, 22, ... --> remainder upon dividing this numbers by 9 is 4. Sufficient.

Answer: D.

[Discussione su GMAT Club](http://gmatclub.com/forum/number-properties-91848.html)

---

## 15. Word Problem (800 level question)

Laura sells encyclopaedias, and her monthly income has two components, a fixed component of \$1000, and a variable component of \$C for each set of encyclopaedias that she sells in that month over a sales target of n sets, where n>0. How much did she earn in March?
(1) If Laura had sold three fewer sets in March, her income for that month would have been \$600 lower than it was.
(2) If Laura had sold 10 sets of encyclopaedias in March, her income for that month would have been over \$4000.

Laura's income $I=1000+c(s-n)$, where $s$ is number of sets she sold and $n$ is target number ($s-n\leq{0}$ --> $I=1000$).

(1) Three cases:
$s-n=1$ --> $c=600$ (surplus of 600\$ was generated by 1 set);
$s-n=2$ --> $c=300$ (surplus of 600\$ was generated by 2 set);
$s-n\geq3$ --> $c=200$ (surplus of 600\$ was generated by 3 set).

If $s-n$ equals to 1, 2, or 3, then income for March will be 1600\$, BUT if $s-n>3$, then income will be more then 1600. Or another way: if we knew that c=300 or 600, then we couldd definitely say that $I=1600$ BUT if $c=200$, then $I=1600$ (for $s-n=3$) or more (for $s-n>3$). Not sufficient.

(2) $1000+c(10-n)>4000$ --> $c>\frac{3000}{10-n}$ --> $0<n<10$ --> as the lowest value of $n=1$, then $c>333.(3)$. Not sufficient.

(1)+(2) as from (2) $c>333.(3)$, then from (1) $c=600$ --> $I=1600$. Sufficient.

Answer: C.

ADDITIONAL NOTES FOR (1) : "If Laura had sold three fewer sets in March..." --> Laura sold $s$ and had $income=I$, but if she had sold $s-3$ then her income would have been $I-600$.

Now:
If $s$ is 1 more than $n$ (or as I wrote $s-n=1$), then it would mean that 600\$ was generated by only 1 set;
If $s$ is 2 more than $n$ (or as I wrote $s-n=2$), then it would mean that 600\$ was generated by 2 sets;
If $s$ is more than 3 more than $n$ (or as I wrote $s-n\geq3$), then it would mean that 600\$ was generated by all 3 sets;

In first two cases income for March will be 1600\$, BUT for third case income can be 1600\$ or more. So this statement is not sufficient.

[Discussione su GMAT Club](http://gmatclub.com/forum/inequalities-64646.html?hilit=laura)

---

## 20. Number properties

If p is a positive integer, what is a remainder when p^2 is divided by 12?
(1) p>3.
(2) p is a prime.

(1) not sufficient
(2) not sufficient
For (1) and (2), just plug two different integers: for (1) 4 an 5 (>3) and for (2) 2 and 3 (primes) to see that you'll get two different answers for remainders.

(1)+(2) Any prime >3 when divide by 6 can only give remainder 1 or 5 (remainder can not be 2 or 4 because than p would be even, it can not be 3 because p would be divisible by 3). So any prime more than 3 can be expressed as $6n+1$ or $6n-1$ ($6n+5$)

So either: $p^2=36n^2+12n+1$ which gives remainder 1 when divided by 12,;

OR: $p^2=36n^2+60n+25$ which also gives remainder 1 when divided by 12.

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/remainder-problem-84967.html)

---

## 21. Coordinate Geometry

In the xy-plane, if line k has negative slope and passes through the point (-5,r) , is the x-intercept of line k positive?
(1) The slope of line k is -5.
(2) r> 0

Let the $x$ intercept be the point $(x,0)$. Slope $m$ is rise over run and for two points $(-5,r)$ and $(x,0)$ would be $m=\frac{r-0}{-5-x}=\frac{r}{-5-x}$ --> $x=\frac{-r-5m}{m}$.

Question: is $x>0$? --> is $x=\frac{-r-5m}{m}>0$?

(1) $m=-5$ --> $x=\frac{-r-5m}{m}=\frac{-r+25}{-5}>0$? $x=\frac{-r+25}{-5}=\frac{r}{5}-5>0$? We can not determine whether $\frac{r}{5}-5>0$ or not. Not sufficient.

(2) $r>0$ and $m<0$ --> $x=\frac{-r-5m}{m}=\frac{-r}{m}-5>0$? $\frac{-r}{m}$ is some positive value (as $m<0$) but we don't know whether it's more than $5$ or not. Not sufficient.

(1)+(2) $x=\frac{r}{5}-5$ and $r>0$ --> $r=5x+25>0$ --> $x>-5$. $x$ can be positive as well as negative. Not sufficient.

Answer: E.

This can be done by visualizing the question. Statement (2) tells us that the point $(-5,r)$, as $r>0$, is in the II quadrant. Line with negative slope through the point in the II quadrant can have $x$ intercept positive as well as negative.

Taken together: as we don't know the exact location of the point $(-5,r)$ in II quadrant we can not say even knowing the slope whether the $x$ intercept would be positive or negative.

[Discussione su GMAT Club](http://gmatclub.com/forum/og-12-ds-question-line-concept-very-good-one-key-wrong-89300.html)

---

## 22. Inequalities /Modulus

Is |x| + |x -1| = 1?
(1) x ≥ 0
(2) x ≤ 1

Q is $|x| + |x -1| = 1$. Let's check when this equation holds true. We should consider three ranges (as there are two check points $x=0$ and $x=1$):

A. $x<0$ --> $-x-x+1=1$ --> $x=0$, but this solution is not valid as we are checking the range $x<0$;

B. $0\leq{x}\leq{1}$ -->$x-x+1=1$ --> $1=1$, which is true. That means that for ANY value from the range $0\leq{x}\leq{1}$, equation $|x| + |x -1| = 1$ holds true.

C. $x>1$ --> $x+x-1=1$ --> $x=1$, but this solution is not valid as we are checking the range $x>1$.

So we get that equation $|x| + |x -1| = 1$ holds true ONLY in the range $0\leq{x}\leq{1}$.

Statements:
(1) $x\geq{0}$. Not sufficient, as $x$ must be also $\leq{1}$;
(2) $x\leq{1}$. Not sufficient, as $x$ must be also $\geq{0}$;

(1)+(2) $0\leq{x}\leq{1}$, exactly the range we needed. Sufficient.

Answer: C.

Discussion of this question at: http://gmatclub.com/forum/absolute-values-ds-questions-85666.html

---

## 23. Number properties

Is the positive integer N a perfect square?
(1) The number of distinct factors of N is even.
(2) The sum of all distinct factors of N is even.

Probably the best way of solving would be making the chart of perfect squares and its factors to check both statements, but below is the algebraic approach if needed.

Couple of things:
1. Note that if $n$ is a perfect square powers of its prime factors must be even, for instance: $36=2^2*3^2$, powers of prime factors of 2 and 3 are even.

2. There is a formula for Finding the Number of Factors of an Integer:

First make prime factorization of an integer $n=a^p*b^q*c^r$, where $a$, $b$, and $c$ are prime factors of $n$ and $p$, $q$, and $r$ are their powers.

The number of factors of $n$ will be expressed by the formula $(p+1)(q+1)(r+1)$. NOTE: this will include 1 and n itself.

Example: Finding the number of all factors of 450: $450=2^1*3^2*5^2$

Total number of factors of 450 including 1 and 450 itself is $(1+1)*(2+1)*(2+1)=2*3*3=18$ factors.

3. A perfect square ALWAYS has an ODD number of Odd-factors, and EVEN number of Even-factors. For instance odd factors of 36 are 1, 3 and 9 (3 odd factor) and even factors are 2, 4, 6, 12, 18 and 36 (6 even factors).

Back to the original question:

Is the positive integer N a perfect square?

(1) The number of distinct factors of N is even --> let's say $n=a^p*b^q*c^r$, given that the number of factors of $n$ is even --> $(p+1)(q+1)(r+1)=even$. But as we concluded if n is a perfect square then powers of its primes $p$, $q$, and $r$ must be even, and in this case number of factors would be $(p+1)(q+1)(r+1)=(even+1)(even+1)(even+1)=odd*odd*odd=odd\neq{even}$. Hence $n$ can not be a perfect square. Sufficient.

(2) The sum of all distinct factors of N is even --> if n is a perfect square then (according to 3) sum of odd factors would be odd and sum of even factors would be even, so sum of all factors of perfect square would be $odd+even=odd\neq{even}$. Hence $n$ can not be a perfect square. Sufficient.

Answer: D.

There are some tips about the perfect square:
• The number of distinct factors of a perfect square is ALWAYS ODD.
• The sum of distinct factors of a perfect square is ALWAYS ODD.
• A perfect square ALWAYS has an ODD number of Odd-factors, and EVEN number of Even-factors.
• Perfect square always has even number of powers of prime factors.

[Discussione su GMAT Club](http://gmatclub.com/forum/perfect-square-94700.html)

---

## 24. Statistic

Lists S and T consist of the same number of positive integers. Is the median of the integers in S greater than the average (arithmetic mean) of the integers in T?
(1) The integers in S are consecutive even integers, and the integers in T are consecutive odd integers.
(2) The sum of the integers in S is greater than the sum of the integers in T.

Q: is $Median\{S\}>Mean\{T\}$? Given: {# of terms in S}={# of terms in T}, let's say N.

(1) From this statement we can derive that as set S and set T are evenly spaced their medians equal to their means. So from this statement question becomes is $Mean\{S\}>Mean\{T\}$? But this statement is clearly insufficient. As we can have set S{2,4,6} and set T{21,23,25} OR S{20,22,24} and T{1,3,5}.

(2) $Sum\{S\}>Sum\{T\}$. Also insufficient. As we can have set S{1,1,10} (Median{S}=1) and set T{3,3,3} (Mean{T}=3) OR S{20,20,20} (Median{S}=20) and T{1,1,1} (Mean{T}=1).

(1)+(2) From (1) question became is $Mean\{S\}>Mean\{T\}$? --> As there are equal # of term in sets and mean(average)=(Sum of terms)/(# of terms), then we have: is $\frac{Sum\{S\}}{N}>\frac{Sum\{T\}}{N}$ true? --> Is $Sum\{S\}>Sum\{T\}$? This is exactly what is said in statement (2) that $Sum\{S\}>Sum\{T\}$. Hence sufficient.

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/mean-and-median-89305.html)

---

## 25. Number Properties

If n is an integer >1, is 3^n-2^n divisible by 35?
(1) n is divisible by 15.
(2) n is divisible by 18.

RULE: for x^n-y^n:
$x^n-y^n$ is ALWAYS divisible by $x-y$.
$x^n-y^n$ is divisible by $x+y$ when n is even.

If n is an integer >1, is $3^n-2^n$ divisible by 35?

(1) n is divisible by 15. --> $3^{15m}-2^{15m}=27^{5m}-8^{5m}$ --> 5m may or my not be even, so insufficient to answer, whether it's divisible by 27+8=35.

(2) n is divisible by 18. --> $3^{18m}-2^{18m}=27^{6m}-8^{6m}$ --> 6m is even, so 3^(18m)-2^(18m)=27^(6m)-8^(6m) is divisible by 27+8=35. Sufficient.

Answer: B.

[Discussione su GMAT Club](http://gmatclub.com/forum/divisibility-84992.html)

---

## 26. Geometry

The area of the right triangle ABC is 4 times greater than the area of the right triangle KLM. If the hypotenuse KL is 10 inches, what is the length of the hypotenuse AB?
(1) Angles ABC and KLM are each equal to 55 degrees.
(2) LM is 6 inches.

Properties of Similar Triangles:

• Corresponding angles are the same.
• Corresponding sides are all in the same proportion.
• It is only necessary to determine that two sets of angles are identical in order to conclude that two triangles are similar; the third set will be identical because all of the angles of a triangle always sum to 180º.
• In similar triangles, the sides of the triangles are in some proportion to one another. For example, a triangle with lengths 3, 4, and 5 has the same angle measures as a triangle with lengths 6, 8, and 10. The two triangles are similar, and all of the sides of the larger triangle are twice the size of the corresponding legs on the smaller triangle.
• If two similar triangles have sides in the ratio $\frac{x}{y}$, then their areas are in the ratio $\frac{x^2}{y^2}$.
OR in another way: in two similar triangles, the ratio of their areas is the square of the ratio of their sides: $\frac{AREA}{area}=\frac{SIDE^2}{side^2}$.

For more on triangles please check Triangles chapter of the Math Book (link in my signature).

Back to original question:
The area of the right triangle ABC is 4 times greater than the area of the right triangle KLM. If the hypotenuse KL is 10 inches, what is the length of the hypotenuse AB?

(1) Angles ABC and KLM are each equal to 55 degrees --> ABC and KLM are similar triangles --> $\frac{AREA_{ABC}}{area_{KLM}}=\frac{4}{1}$, so the sides are in ratio 2/1 --> hypotenuse KL=10 --> hypotenuse AB=2*10=20. Sufficient.

(2) LM is 6 inches --> KM=8 --> $area_{KLM}=24$ --> $AREA_{ABC}=96$. But just knowing the are of ABC is not enough to determine hypotenuse AB. For instance: legs of ABC can be 96 and 2 OR 48 and 4 and you'll get different values for hypotenuse. Not sufficient.

Answer: A.

[Discussione su GMAT Club](http://gmatclub.com/forum/mgmat-ds-help-94037.html?hilit=different%20values%20for%20hypotenuse%20sufficient.#p723237)

---

## 27. Number properties

If N is a positive integer, what is the last digit of 1! + 2! + ... +N!?
(1) N is divisible by 4
(2) (N^2 + 1)/5 is an odd integer.

Generally the last digit of $1! + 2! + ... +N!$ can take ONLY 3 values:
A. N=1 --> last digit 1;
B. N=3 --> last digit 9;
C. N=any other value --> last digit 3 (N=2 --> 1!+2!=3 and for N=4 --> 1!+2!+3!+4!=33, $N\geq{4}$ the terms after N=4 will end by 0 thus not affect last digit and it'll remain 3).

So basically question asks whether we can determine which of three cases we have.
(1) N is divisible by 4 --> N is not 1 or 3, thus third case. Sufficient.

(2) (N^2 + 1)/5 is an odd integer --> N is not 1 or 3, thus third case. Sufficient.

Answer: D.

[Discussione su GMAT Club](http://gmatclub.com/forum/a-question-from-the-iphone-software-94088.html)

---

## 28. Remainders

The integers m and p are such that 2<m<p, and m is not a factor of p. if r is the remainder when p is divided by m, is r>1?
(1) the greatest common factor of m and p is 2
(2) the least common multiple of m and p is 30

Given: $2<m<p$ and $\frac{p}{m}\neq{integer}$. $p=xm+r$. q: $r=?$

(1) the greatest common factor of m and p is 2 --> p and m are even (as both have 2 as a factor) --> even divided by even can give only even remainder (0, 2, 4, ...), since remainder is not zero (as $\frac{p}{m}\neq{integer}$), then remainder must be more than 1. Sufficient.

(2) the least common multiple of m and p is 30 --> if m=5 and p=6, remainder=1=1, answer to the question would be NO. BUT if m=10 and p=15 remainder=5>1answer to the question would be YES. Two different answers. Not sufficient.

Answer: A.

[Discussione su GMAT Club](http://gmatclub.com/forum/gmat-prep-ds-93770.html)

---

## 29. Inequalities

Is $\frac{x}{3} + \frac{3}{x} > 2$?
(1) $x < 3$
(2) $x > 1$

Is $\frac{x}{3}+\frac{3}{x}>2$? --> is $\frac{(x-3)^2}{x}>0$? Now, nominator is non-negative, thus the fraction to be positive nominator must not be zero (thus it'll be positive) and denominator mut be positive --> $x\neq{3}$ and $x>0$.

Statement (1) satisfies first requirement and statement (2) satisfies second requirement, so taken together they are sufficient.

Answer: C.

NOTE: Never multiply or reduce inequality by an unknown (a variable) unless you are sure of its sign since you do not know whether you must flip the sign of the inequality.

So you CAN NOT multiply $\frac{x}{3}+\frac{3}{x}>2$ by $3x$ since you don't know the sign of $x$.

What you CAN DO is: $\frac{x}{3}+\frac{3}{x}>2$ --> $\frac{x}{3}+\frac{3}{x}-2>$ --> common denominator is $3x$ --> $\frac{x^2+9-6x}{3x}>0$ --> multiply be 3 --> $\frac{x^2+9-6x}{x}>0$ --> $\frac{(x-3)^2}{x}>0$.

[Discussione su GMAT Club](http://gmatclub.com/forum/tricky-inequality-problem-97331.html)

---

## 30. Coordinate Geometry

In the xy coordinate plane, line L and line K intersect at the point (4,3). Is the product of their slopes negative?
(1) The product of the x-intersects of lines L and K is positive.
(2) The product of the y-intersects of lines L and K is negative.

We have two lines: $y_l=m_1x+b_1$ and $y_k=m_2x+b_2$. The question: is $m_1*m_2<0$?

Lines intersect at the point (4,3) --> $3=4m_1+b_1$ and $3=4m_2+b_2$

(1) The product of the x-intersects of lines L and K is positive. Now, one of the lines can intersect x-axis at 0<x<4 (positive slope) and another also at 0<x<4 (positive slope), so product of slopes also will be positive BUT it's also possible one line to intersect x-axis at 0<x<4 (positive slope) and another at x>4 (negative slope) and in this case product of slopes will be negative. Two different answers, hence not sufficient.

But from this statement we can deduce the following: x-intersect is value of $x$ for $y=0$ and equals to $x=-\frac{b}{m}$ --> so $(-\frac{b_1}{m_1})*(-\frac{b_2}{m_2})>0$ --> $\frac{b_1b_2}{m_1m_2}>0$.

(2) The product of the y-intersects of lines L and K is negative. Now, one of the lines can intersect y-axis at 0<y<3 (positive slope) and another at y<0 (positive slope), so product of slopes will also be positive BUT it's also possible one line to intersect y-axis at y<0 (positive slope) and another at y>3 (negative slope) and in this case product of slopes will be negative. Two different answers, hence not sufficient.

But from this statement we can deduce the following: y-intercept is value of $y$ for $x=0$ and equals to $x=b$ --> $b_1*b_2<0$.

(1)+(2) $\frac{b_1b_2}{m_1m_2}>0$ and $b_1*b_2<0$. As numerator in $\frac{b_1b_2}{m_1m_2}>0$ is negative, then denominator $m_1m_2$ must also be negative. So $m_1m_2<0$. Sufficient.

Answer: C.

In fact we arrived to the answer C, without using the info about the intersection point of the lines. So this info is not needed to get C.

[Discussione su GMAT Club](http://gmatclub.com/forum/gmat-prep-ds-93771.html)

---

## 31. Word Problem

The total cost of producing item X is equal to the sum of item X's fixed cost and variable cost. If the variable cost of producing X decreased by 5% in January, by what percent did the total cost of producing item X change in January?
(1) The fixed cost of producing item X increased by 13% in January.
(2) Before the changes in January, the fixed cost of producing item X was 5 times the variable cost of producing item X.

Let the total cost in January be $C_2$ and the total cost before be $C_1$.


Given: $C_2=F_2+V_2$ and $C_1=F_1+V_1$, also $V_2=0.95V_1$.
Question: $\frac{C_2}{C_1}=\frac{F_2+V_2}{F_1+V_1}=\frac{F_2+0.95V_1}{F_1+V_1}=?$

(1) The fixed cost of producing item X increased by 13% in January --> $F_2=1.13F_1$ --> $\frac{1.13F_1+0.95V_1}{F_1+V_1}=?$. Not sufficient to get the exact fraction.

(2) Before the changes in January, the fixed cost of producing item X was 5 times the variable cost of producing item X --> $F_1=5V_1$ --> $\frac{F_2+0.95V_1}{5V_1+V_1}=?$. Not sufficient.

(1)+(2) $F_2=1.13F_1$ and $F_1=5V_1$ --> $F_2=1.13F_1=5.65V_1$ --> from (2) $\frac{F_2+0.95V_1}{F_1+V_1}=?$ --> substituting $F_2$ and $F_1$--> $\frac{5.65V_1+0.95V_1}{5V_1+V_1}=\frac{6.6}{6}=1.1$ --> in January total cost increased by 10%. Sufficient. (Actually no calculations are needed: stem and statement provide us with such relationships of 4 unknowns that 3 of them can be written with help of the 4th one and when we put them in fraction, which we want to calculate, then this last unknown is reduced, leaving us with numerical value).

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/very-hard-mgmat-97488.html?hilit=changes%20in%20January#p751113)

---

## 32. Powers

If x and y are distinct positive integers, what is the value of $x^4 - y^4$?
(1) $(y^2 + x^2)(y + x)(x - y) = 240$
(2) $x^y = y^x$ and $x > y$

Important property to know: $x^2-y^2=(x+y)(x-y)$.

Given: $x$ and $y$ are distinct positive integers. Question: $x^4-y^4=?$


(1) $(y^2+x^2)(y+x)(x-y)=240$ --> $(y^2+x^2)(x^2-y^2)=240$ --> $x^4-y^4=240$. Sufficient.

(2) $x^y = y^x$ and $x>y$, also $x$ and $y$ are distinct positive integers --> only one such pair is possible $x=4>y=2$: $x^y=4^2=16=2^4=y^x$ --> $x^4-y^4=240$. Sufficient.

Answer: D.

NOTES on (2): it's worth remembering that $4^2=16=2^4$, I've seen several GMAT questions on number properties using this (another useful property $8^2=4^3=2^6=64$).

But if you don't know this property:

Given: $x^y = y^x$ and $x>y$, also $x$ and $y$ are distinct positive integers.
Couple of things:
$x$ and $y$ must be either distinct positive odd integers or distinct positive even integers (as odd in ANY positive integer power is odd and even in ANY positive integer power is even).

After testing several options you'll see that $x=4$ and $y=2$ is the only possible scenario: because, when $y\geq{2}$ and $x>{4}$, then $x^y$ (bigger value in smaller power) will be always less than $y^x$ (smaller value in bigger power): $5^3<3^5$, or $6^2<2^6$, or $8^2<2^8$, or $10^2<2^{10}$, ....

[Discussione su GMAT Club](http://gmatclub.com/forum/4-powerful-xys-97450.html)

---

## 33. Probability

For a trade show, two different cars are selected randomly from a lot of 20 cars. If all the cars on the lot are either sedans or convertibles, is the probability that both cars selected will be sedans greater than 3/4?
(1) At least three-fourths of the cars are sedans.
(2) The probability that both of the cars selected will be convertibles is less than 1/20.

Let the # of sedans be $s$ and the # of convertibles be $c$.

Given: $s+c=20$. Question: is $\frac{s}{20}*\frac{s-1}{19}>\frac{3}{4}$? --> Is $s>17$ (18, 19, 20)?

(1) $s\geq{\frac{3}{4}*20}$ --> $s\geq{15}$. Not sufficient.

(2) $\frac{c}{20}*\frac{c-1}{19}<\frac{1}{20}$ --> $c(c-1)<19$ --> $c<5$ (4, 3, 2, 1, 0) --> $s>15$. Not sufficient.

(1)+(2) Not sufficient.

Answer: E.

[Discussione su GMAT Club](http://gmatclub.com/forum/multiple-trials-conditional-probability-and-dependent-even-96038.html?hilit=sedans#p750160)

---

## 34. Inequalities

If (x/y)>2, is 3x+2y<18?
(1) x-y is less than 2
(2) y-x is less than 2

I would solve this question with graphic approach, by drawing the lines. With this approach you will "see" that the answer is A. But we can do it with algebra as well.

$\frac{x}{y}>2$ tells us that $x$ and $y$ are either both positive or both negative, which means that all points $(x,y)$ satisfying given inequality are either in I or III quadrant. When they are both negative (in III quadrant) inequality $3x+2y<18$ is always true, so we should check only for I quadrant, or when both $x$ and $y$ are positive.

In I quadrant, as $x$ and $y$ are both positive, we can rewrite $\frac{x}{y}>2$ as $x>2y>0$ (remember $x>0$ and $y>0$).

So basically question becomes: If $x>0$ and $y>0$ and $x>2y>0$, is $3x+2y<18$?

(1) $x-y<2$.

Subtract inequalities $x>2y$ and $x-y<2$ (we can do this as signs are in opposite direction) --> $x-(x-y)>2y-2$ --> $y<2$.

Now add inequalities $x-y<2$ and $y<2$ (we can do this as signs are in the same direction) --> $x-y+y<2+2$ --> $x<4$.

We got $y<2$ and $x<4$. If we take maximum values $x=4$ and $y=2$ and substitute in $3x+2y<18$, we'll get $12+4=16<18$.

Sufficient.

(2) $y-x<2$ and $x>2y$:
$x=3$ and $y=1$ --> $3x+2y=11<18$ true.
$x=11$ and $y=5$ --> $3x+2y=43<18$ false.

Not sufficient.

Answer: A.

Great post by Walker about the graphic approach: http://gmatclub.com/forum/graphic-approach-to-problems-with-inequalities-68037.html

---

## 35. Number Properties

If k is a positive integer. Is K a prime number?
(1) No integers between "2" and "square root of K" inclusive divides k evenly?
(2) No integers between 2 and k/2 divides k evenly, and k is greater than 5.

Given: $k=integer>0$. Question: $k=prime$?

A prime number is a positive integer with exactly two distinct divisors: 1 and itself.

(1) No integer between 2 and $\sqrt{k}$ inclusive divides k evenly --> let's assume $k$ is not a prime, then there must be some integers $a$ and $b$ ($1<a<k$ and $1<a<k$), a factors of $k$, for which $ab=k$. As given that $k$ has no factor between 2 and $\sqrt{k}$ inclusive, then both factors $a$ and $b$ must be more than $\sqrt{k}$. But it's not possible, as the product of two positive integers more than $\sqrt{k}$ will yield an integer more than $k$ ($ab>k$). Hence our assumption that $k$ is not a prime is not true --> $k$ is a prime. Sufficient.

(2) No integers between 2 and $\frac{k}{2}$ divides k evenly, and k is greater than 5 --> the same here : let's assume $k$ is not a prime, then there must be some integers $a$ and $b$ ($1<a<k$ and $1<a<k$), a factors of $k$, for which $ab=k$ --> $k=ab\geq{\frac{k^2}{4}}$ (as both $a$ and $b$ are more than or equal to $\frac{k}{2}$, then their product $ab$, which is $k$, must be more than or equal to $\frac{k}{2}*\frac{k}{2}$) --> $4k\geq{k^2}$ --> $k(4-k)\geq{0}$. But this inequality cannot be true as $4-k$ will be negative (as given $k>5$) and $k$ is positive so $k(4-k)$ must be negative not positive or zero. Hence our assumption that $k$ is not a prime is not true --> $k$ is a prime. Sufficient.

Answer: D.

P.S. The first statement is basically the way of checking whether some # is a prime:

Verifying the primality (checking whether the number is a prime) of a given number $n$ can be done by trial division, that is to say dividing $n$ by all integer numbers smaller than $\sqrt{n}$, thereby checking whether $n$ is a multiple of $m<\sqrt{n}$.
Example: Verifying the primality of $161$: $\sqrt{161}$ is little less than $13$, from integers from $2$ to $13$, $161$ is divisible by $7$, hence $161$ is not prime.

---

## 36. Inequalities

On the number line, the distance between x and y is greater than the distance between x and z. Does z lie between x and y on the number line?
(1) xyz<0
(2) xy< 0

The distance between x and y is greater than the distance between x and z, means that we can have one of the following four scenarios:
A. y--------z--x (YES case)
B. x--z--------y (YES case)
C. y--------x--z (NO case)
D. z--x--------y (NO case)

The question asks whether we have scenarios A or B (z lie between x and y ).

(1) xyz <0 --> either all three are negative or any two negative and the third positive. We can place zero between y and z in case A (making y negative and x, z positive), then the answer would be YES or we can place zero between y and x in case C, then the answer would be NO. Not sufficient.

(2) xy<0 --> x and y have opposite signs. The same here: We can place zero between y and x in case A, then the answer would be YES or we can place zero between y and x in case C, then the answer would be NO. Not sufficient.

(1)+(2) Cases A (answer YES) and case C (answer NO) both work even if we take both statement together, so insufficient.

A. y----0----z--x (YES case) --> xyz<0 and xy<0;
C. y----0----x--z (NO case) --> xyz<0 and xy<0

Answer: E.

---

## 37. Algebra

Is the last digit of integer x^2 - y^2 a zero?
(1) x - y is an integer divisible by 30
(2) x + y is an integer divisible by 70

Given: $x^2-y^2=(x-y)(x+y)=integer$. Question is the units digit of this integer zero, which can be translated as is $x^2-y^2$ divisible by 10.

(1) $x-y=30m$ (where $m$ is an integer) --> if $x$ and $y$ are integers, then $x+y=integer$ and $x^2-y^2=30m*(x+y)=30m*integer$, which is divisible by 10 BUT if $x=30.75$ and $y=0.75$, then $x^2-y^2=(x-y)(x+y)=30*31.5=945=integer$, which is not divisible by 10. Not sufficient.

(2) $x+y=70n$ (where $n$ is an integer) --> if $x$ and $y$ are integers, then $x-y=integer$ and $x^2-y^2=(x-y)*70n=integer*70n$, which is divisible by 10 BUT if $x=69.75$ and $y=0.25$, then $x^2-y^2=(x-y)(x+y)=69,5*70=4865=integer$, which is not divisible by 10. Not sufficient.

(1)+(2) $x^2-y^2=30m*70n=integer$, Which is divisible by 10. Sufficient.

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/gmat-club-test-95793.html)

---

## 38. Inequalities

Is (x^7)(y^2)(z^3) > 0 ?
(1) yz < 0
(2) xz > 0

Inequality $x^7*y^2*z^3>0$ to be true $x$ and $z$ must be either both positive or both negative AND $y$ must not be zero.

(1) $yz<0$ --> $y\neq{0}$. Don't know about $x$ and $z$. Not sufficient.

(2) $xz>0$ --> $x$ and $z$ are either both positive or both negative. Don't know about $y$. Not sufficient.

(1)+(2) Sufficient.

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/data-sufficiency-exponents-question-95626.html)

---

## 39. Number Properties

If K is a positive integer, how many different prime numbers are factors of the expression K^2?
(1) Three different prime numbers are factors of 4K^4.
(2) Three different prime numbers are factors of 4K.

First of all $k^x$ (where $x$ is an integer $\geq{1}$) will have as many different prime factors as integer $k$. Exponentiation doesn't "produce" primes.

Next: $p^y*k^x$ (where $p$ is a prime and $y$ is an integer $\geq{1}$) will have as many different prime factors as integer $k$ if $k$ already has $p$ as a factor OR one more factor than $k$if $k$ doesn't have $p$ as a factor .

So, the question basically is: how many different prime numbers are factors of $k$?

(1) Three different prime numbers are factors of $4k^4$ --> if $k$ itself has 2 as a factor (eg 30) than it's total # of primes is 3 but if k doesn't have 2 as a factor (eg 15) than it's total # of primes is 2. Not sufficient.

(2) Three different prime numbers are factors of $4k$ --> the same as above: if $k$ itself has 2 as a factor (eg 30) than it's total # of primes is 3 but if k doesn't have 2 as a factor (eg 15) than it's total # of primes is 2. Not sufficient.

(1)+(2) Nothing new, k can be 30 (or any other number with 3 different primes, out of which one factor is 2) than the answer is 3 or k can be 15 (or any other number with 2 different primes, out of which no factor is 2) than the answer is 2. Not sufficient.

Answer: E.

[Discussione su GMAT Club](http://gmatclub.com/forum/different-prime-factors-ds-95585.html)

---

## 40. Work Problem

Jane can paint the wall in J hours, and Bill can paint the same wall in B hours. They begin at noon together. If J and B are both even numbers is J=B?
(1) Jane and Bill finish at 4:48 p.m.
(2) (J+B)^2=400

Jane and Bill working together will paint the wall in $T=\frac{JB}{J+B}$ hours. Now suppose that $J=B$ --> $T=\frac{J^2}{2J}=\frac{J}{2}$, as $J$ and $B$ are even $J=2n$ --> $T=\frac{2n}{2}=n$, as $n$ is an integer, working together Jane and Bill will paint the wall in whole number of hours, meaning that in any case $T$ must be an integer.

(1) They finish painting in 4 hours and 48 minutes, $T$ is not an integer, --> $J$ and $B$ are not equal. Sufficient.

(2) $J+B=20$, we can even not consider this one, clearly insufficient. $J$ and $B$ can be $10$ and $10$ or $12$ and $8$.

Answer: A.

[Discussione su GMAT Club](http://gmatclub.com/forum/painting-the-wall-87131.html)

---

## 41. Word Problem

When Mrs. T's students answer the bonus question correctly, she awards a bonus. If the base score is between 10 and 99, the bonus is equal to 2 times the tens digit in the base score. The last test Mrs. T scored was between 10 and 99, and the student answered the bonus question correctly. Was the bonus given greater than 17% of the base score?
(1) The base score of the test was between 50 and 90.
(2) Mrs. T added 16 bonus points to the last test she graded.


Given:
Score is two digit number - $S=10x+y$ (as score was between 10 and 99);
Bonus - $B=2x$.
Question: is $2x>\frac{17}{100}(10x+y)$? --> is $30x>17y$?

(1) The base score of the test was between 50 and 90 --> $5\leq{x}\leq{9}$ --> the range of $30x$ is $150\leq{30x}\leq{270}$ and the range of $17y$ is $0\leq{17y}\leq{153}$ (as$y$ can be from 0 to 9). Hence $30x$ may or may not be more than $17y$. Not sufficient.

(2) Mrs. T added 16 bonus points to the last test she graded --> $B=2x=16$ --> $x=8$ --> $30x=240$. Max value of $17y=153$ (as max value of $y$ is 9), hence $30x$ is more than $17y$. Sufficient.

Answer: B.

[Discussione su GMAT Club](http://gmatclub.com/forum/700-level-question-95183.html)

---

## 42. Coordinate Geometry

If y is a negative number greater than -8, is x greater than the average (arithmetic mean) of y and -8 ?
(1) On the number line, x is closer to -8 than it is to y.
(2) x = 4y

Given: $-8<y<0$.
Q: is x greater than the average of -8 and x? Or: is $x>\frac{-8+y}{2}$? --> $2x>-8+y$?

-----{-8}-----{average}-----{y} (average of y and -8 is halfway between y and -8).

(1) On the number line, x is closer to -8 than it is to y.

Now, as $x$ is closer to $-8$ than it ($x$) is to $y$, then $x$ is either in the green area, so less than average OR in the red area, so also less than average. Answer to the question is NO.

Sufficient.

(2) $x=4y$ --> is $2x>-8+y$? --> is $8y>-8+y$? --> is $y>-\frac{8}{7}$? We don't now that. Not sufficient. (we've gotten that if $0>y>-\frac{8}{7}$ (for instance if $y=-1$), then the answer to the question is YES, but if $y\leq{-\frac{8}{7}}$ (for instance if $y=-2$), then the answer to the question is NO.)

Answer: A.

[Discussione su GMAT Club](http://gmatclub.com/forum/600-level-question-95138.html)

---

## 43. Rate Problem

Car X leaves Town A at 2 p.m. and drives toward Town B at a constant rate of m miles per hour. Fifteen minutes later, Car Y begins driving from Town B to Town A at a constant rate of n miles an hour. If both Car X and Car Y drive along the same route, will Car X be closer to Town A or Town B when it passes Car Y ?
(1) Car X arrives in Town B 90 minutes after leaving city A.
(2) Car Y arrives in Town A at the same time Car X arrived in Town B.

$A----------P----B$ (P meeting point). Question: is $PA>PB$?

(1) Car X arrives in Town B 90 minutes after leaving city A. No info about car Y. Not sufficient.

(2) Car Y arrives in Town A at the same time Car X arrived in Town B --> X needs 15 min longer than Y to cover the same distance (as Y starts 15 min after X) --> rate of X < rate of Y (m<n). Also, after they meet X and Y will need the same time to get to their respective destinations (as they arrived at the same time) --> the distance covered by Y after they meet (PA=nt) at higher speed, will obviously be more than the distance covered by X after they meet (PB=mt) at lower speed (or algebraically as m<n, mt<nt --> $PA>PB$). So $PA>PB$. Sufficient.

Answer: B.

[Discussione su GMAT Club](http://gmatclub.com/forum/kaplan-test-question-95033.html)

---

## 44. Number Properties

Is product 2*x*5*y an even integer?
(1) 2 + x + 5 + y is an even integer
(2) x - y is an odd integer

Question: $2*x*5*y=even$. As there is 2 as a multiple, then this expression will be even if $5xy=integer$. Basically we are asked is $5xy=integer$ true?

Note that $x$ and $y$ may not be integers for $2*x*5*y$ to be even (example $x=\frac{7}{9}$ and $y=\frac{9}{7}$) BUT if they are integers then $2*x*5*y$ is even.


(1) $2+x+5+y=even$ --> $7+x+y=even$ --> $x+y=odd$. Not sufficient. (x=1 and y=2 answer YES BUT x=1.3 and y=1.7 answer NO)

(2) $x-y=odd$. Not sufficient. (x=1 and y=2 answer YES BUT x=1.3 and y=0.3 answer NO)

(1)+(2) Sum (1) and (2) $(x+y)+(x-y)=odd_1+odd_2$ --> $2x=even$ --> $x=integer$ --> $y=integer$ --> Both $x$ and $y$ are integers. Hence sufficient.

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/even-ds-78950.html)

---

## 45. Number Properties

If d is a positive integer and f is the product of the first 30 positive integers, what is the value of d?
(1) 10^d is a factor of f
(2) d>6

(1) 10^d is a factor of f --> $k*10^d=30!$.

First we should find out how many zeros $30!$ has, it's called trailing zeros. It can be determined by the power of $5$ in the number $30!$ --> $\frac{30}{5}+\frac{30}{25}=6+1=7$--> $30!$ has $7$ zeros.

$k*10^d=n*10^7$, (where $n$ is the product of other multiples of 30!) --> it tells us only that max possible value of $d$ is $7$. Not sufficient.

(2) $d>6$ Not Sufficient.

(1)+(2) $d>6$, $d_{max}=7$ --> $d=7$.

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/number-properties-from-gmatprep-84770.html)
For trailing zeros: http://gmatclub.com/forum/everything-about-factorials-on-the-gmat-85592.html

---

## 46. Modulus / Inequalities

If |x|*y+ 9 > 0, and x and y are integers, is x < 6?
(1) y<0
(2) |y|<=1

(1) $y<0$. If $y=-1$, then $-|x|+9>0$ --> $|x|<9$, so $x$ can be 8, -8, 7, -7, and so on. So $x$ may or may not be less than 6. Not sufficient.

(2) $|y|\leq{1}$ --> $-1\leq{y}\leq{1}$ --> as $y$ is an integer, then $y$ is -1, 0, or 1. As we've seen above if $y=-1$, then $x$ may or may not be less than 6. Not sufficient.

(1)+(2) Again if $y=-1$ (which satisfies both stem and statements) then $x$ may or may not be less than 6. Not sufficient.

Answer: E.

[Discussione su GMAT Club](http://gmatclub.com/forum/is-x-6-mgmat-toughie-97026.html)

---

## 47. Rate Problem / Word Problem (750 level question)

Train A leaves New York for Boston at 3 PM and travels at the constant speed of 100 mph. An hour later, it passes Train B, which is making the trip from Boston to New York at a constant speed. If Train B left Boston at 3:50 PM and if the combined travel time of the two trains is 2 hours, what time did Train B arrive in New York?
(1) Train B arrived in New York before Train A arrived in Boston.
(2) The distance between New York and Boston is greater than 140 miles.

Let:
$d$ be the distance between cities;
$x$ be the rate of Train B.

"An hour later (so at 4:00PM), Train A passes Train B" --> before they pass each other A traveled 1 hour (4PM-3PM) and B traveled 1/6 hours (4PM-3:50PM).

"Combined travel time of the two trains is 2 hours" --> d/100(time to cover all distance for train A)+d/x(time to cover all distance for train B)=2 --> $\frac{d}{100}+\frac{d}{x}=2$;

As before they pass A traveled 100 miles (1 hour at 100 miles per hour), then distance to cover for B after they pass is this 100 miles and as B traveled x*1/6 miles before they pass (1/6 hour at x miles per hour), then distance to cover for A after they pass is this x*1/6 miles --> $100+\frac{x}{6}=d$;

So, we have:
$\frac{d}{100}+\frac{d}{x}=2$ and $100+\frac{x}{6}=d$.

Solving for $d$ and $x$
$d=150$ and $x=300$;
OR:
$d=\frac{800}{6}\approx{133.3}$ and $x=200$.

(1) Says that train B arrived before A.
If $x=200$ A arrives at 4:20, B at 4:30, not good;
If $x=300$ A arrives at 4:30, B at 4:20, OK.
Sufficient

(2) Says that $d>140$ --> $d=150$ --> $x=300$, arrival time for B 4:20. Sufficient

Answer D.

[Discussione su GMAT Club](http://gmatclub.com/forum/train-a-leaves-new-york-97694.html)

---

## 48. Coordinate Geometry / Geometry

If vertices of a triangle have coordinates (-2,2), (3,2) and (x,y), what is the area of the triangle?
(1) |y-2|=1
(2) angle at the vertex (x,y) equals to 90 degrees

Given two points A(-2,2) and B(3,2). Question: Area ABC=?, where C(x,y).

(1) |y-2|=1 --> $y=3$ or $y=1$ --> vertex C could be anywhere on the blue line $y=3$ or anywhere on the red line $y=1$. But in ANY case the are of ABC will be the same --> $area=\frac{1}{2}*base*height$ so $base=AB=5$ and the height would be 1 for any point C (see two possible locations of C: C1 and C2, the heights of ABC1 and ABC2 are the same and equal to 1) --> $area=\frac{1}{2}*base*height=\frac{5}{2}$. Sufficient.

(2) angle at the vertex C(x,y) equals to 90 degrees --> ABC is a right triangle with hypotenuse AB --> consider AB to be diameter of a circle and in this case C could be anywhere on the circle and it will be right angle (if the diameter of the circle is also the inscribed triangle’s side, then that triangle is a right triangle), thus height of ABC will be different for different location of point C, resulting the different areas (see two possible locations of of C: C3 and C4, heights of ABC3 and ABC4 are different). Not sufficient.

Answer: A.

[Discussione su GMAT Club](http://gmatclub.com/forum/vertices-of-a-triangle-82159.html)

---

## 49. Combinatorics / Probability

Set A consists of 25 distinct numbers. We pick n numbers from the set A one-by-one (n<=25). What is the probability that we pick numbers in ascending order?
(1) Set A consists of even consecutive integers
(2) n=5

We should understand following two things:
1. The probability of picking any n numbers from the set of 25 distinct numbers is the same. For example if we have set of numbers from 1 to 25 inclusive, then the probability we pick n=5 numbers {3,5,1,23,25} is the same as that of we pick n=5 numbers {9,10,4,6,18}. So picking any 5 numbers $\{x_1,x_2,x_3,x_4,x_5\}$ from the set is the same.

2. Now, imagine we have chosen the set $\{x_1,x_2,x_3,x_4,x_5\}$, where $x_1<x_2<x_3<x_4<x_5$. We can pick this set of numbers in $5!=120$ # of ways and only one of which, namely $\{x_1,x_2,x_3,x_4,x_5\}$ is in ascending order. So 1 out of 120. $P=\frac{1}{n!}=\frac{1}{5!}=\frac{1}{120}$.

According to the above the only thing we need to know is the size of the set (n) we are choosing from the initial set A.

Answer: B.

[Discussione su GMAT Club](http://gmatclub.com/forum/probability-of-picking-numbers-in-ascending-order-89035.html)

---

## 50. Inequalities

Is (x+y) / (x-y) > 1
(1) x + y > x -y
(2) 0 > y

If $x\neq{-y}$ is $\frac{x-y}{x+y}>1$?

Is $\frac{x-y}{x+y}>1$? --> Is $0>1-\frac{x-y}{x+y}$? --> Is $0>\frac{x+y-x+y}{x+y}$? --> Is $0>\frac{2y}{x+y}$?

(1) $x>0$ --> Not sufficient.

(2) $y<0$ --> Not sufficient.

(1)+(2) $x>0$ and $y<0$ --> numerator (y) is negative, but we can not say whether the denominator {positive (x)+negative (y)} is positive or negative. Not sufficient.

Answer: E.

NOTE: you can not rewrite given inequality as $x-y>x+y$, because you are actually multiplying both sides of inequality by $x+y$: never multiply an inequality by variable (or expression with variable) unless you know the sign of variable (or expression with variable). Because if $x+y>0$ you should write $x-y>x+y$ BUT if $x+y<0$, you should write $x-y<x+y$ (flip the sign when multiplying by negative expression).

So again: given inequality can be simplified as follows: $\frac{x-y}{x+y}>1$ --> $0>1-\frac{x-y}{x+y}<0$ --> $0>\frac{x+y-x+y}{x+y}$ --> $0>\frac{2y}{x+y}$ --> we can drop 2 and finally we'll get: $0>\frac{y}{x+y}$.

Now, numerator is negative ($y<0$), but we don't know about the denominator, as $x>0$ and $y<0$ can not help us to determine the sign of $x+y$. So the answer is E.

[Discussione su GMAT Club](http://gmatclub.com/forum/gmat-prep-ds-96090.html)

---

## 51. Statistics

The range of set A is R. A number having a value equal to R is added to set A. Will the range of set A increase?
(1) All the numbers in set A are positive.
(2) The mean of the new set is smaller than R.

Let's use the notations proposed by mainhoon:
$a$ - smallest number in the set;
$b$ - largest number in the set;
$r$ - the range, so $b-a=r$;
$n$ - # of elements in set A;
$m$ - the mean of set A.

The range of new set will NOT increase if $a\leq{r}\leq{b}$, because new range will still be $b-a$.

(1) All the numbers in set A are positive --> as all numbers are positive $r$ can note be more than $b$, the largest number in the set, so $r<b$.

But $r$ can still be less than $a$ (example $A=\{5,6\}$, $r=1$ --> $A_2=\{1,5,6\}$, $r_2=5>r=1$) and in this case answer would be YES but $a\leq{r}\leq{b}$ is also possible (example $A=\{1,6\}$, $r=5$ --> $A_2=\{1,5,6\}$, $r_2=5=r=5$) and in this case answer would be NO. Not sufficient.

(2) The mean of the new set is smaller than R --> $m_2=\frac{m*n+r}{n+1}<r$ --> $m<r$ (so R is also more than mean of set A) --> as $r$ is more than mean of A, then $r$ can note be less than $a$, the smallest number in the set, so $a<r$, (the mean is between the largest and smallest element of the set: $a\leq{m}\leq{b}$ as $r>m$, then $a<r$).

But $r$ can still be more than $b$ (example $A=\{-5,0\}$, $r=5$ --> $A_2=\{-5,0,5\}$, $r_2=10>r=5$) and in this case answer would be YES but $a\leq{r}\leq{b}$is also possible ($A=\{1,6\}$, $r=5$ --> $A_2=\{1,5,6\}$, $r_2=5=r=5$) and in this case answer would be NO. Not sufficient.

(1)+(2) From (1) $r<b$ and from (2) $a<r$ --> $a<r<b$ --> new range will still be $b-a$, so the answer to the question is NO. Sufficient.

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/hard-statistics-99657.html)

---

## 52. Number properties

Does the integer k have a factor p such that 1<p<k?
(1) k > 4!
(2) 13! + 2< k < 13!+13

Question basically asks is k a prime number. If it is, then it won't have a factor p such that 1<p<k (definition of a prime number).

(1) $k>4!$ --> k is more than some number (4!). K may or may not be a prime. Not sufficient.

(2) $13!+2\leq{k}\leq{13!+13}$ --> k can not be a prime. For instance if $k=13!+8=8*(2*4*5*6*7*9*10*11*12*13+1)$, then k is a multiple of 8, so not a prime. Same for all other numbers in this range: $k=13!+x$, where $2\leq{x}\leq{13}$ will definitely be a multiple of $x$. Sufficient.

Answer: B.

[Discussione su GMAT Club](http://gmatclub.com/forum/gmat-prep-ds-96091.html)

---

## 53. Remainders

If p and n are positive integers and p>n, what is the remainder when p^2 - n^2 is divided by 15?
(1) The remainder when p + n is divided by 5 is 1.
(2) The remainder when p - n is divided by 3 is 1.

First of all $p^2 - n^2=(p+n)(p-n)$.

(1) The remainder when p + n is divided by 5 is 1. No info about p-n. Not sufficient.

(2) The remainder when p - n is divided by 3 is 1. No info about p+n. Not sufficient.

(1)+(2) "The remainder when p + n is divided by 5 is 1" can be expressed as $p+n=5t+1$ and "The remainder when p - n is divided by 3 is 1" can be expressed as $p-n=3k+1$.

Multiply these two --> $(p+n)(p-n)=(5t+1)(3k+1)=15kt+5t+3k+1$, now first term (15kt) is clearly divisible by 15 (r=0), but we don't know about 5t+3k+1. For example t=1 and k=1, answer r=9 BUT t=7 and k=3, answer r=0. Not sufficient.

OR by number plugging: if $p+n=11$ (11 divided by 5 yields remainder of 1) and $p-n=1$ (1 divided by 3 yields remainder of 1) then $(p+n)(p-n)=11$and remainder upon division 11 by 15 is 11 BUT if $p+n=21$ (21 divided by 5 yields remainder of 1) and $p-n=1$ (1 divided by 3 yields remainder of 1) then $(p+n)(p-n)=21$ and remainder upon division 21 by 15 is 6. Not sufficient.

Answer: E.

[Discussione su GMAT Club](http://gmatclub.com/forum/ds8-93971.html)

---

## 54. Modulus / Inequality

Is $\sqrt{(x-3)^2}=3-x$?
(1) $x\neq{3}$.
(2) $-x|x| >0$

Remember: $\sqrt{x^2}=|x|$. Why?

Couple of things:

The point here is that square root function can not give negative result: wich means that $\sqrt{some \ expression}\geq{0}$.

So $\sqrt{x^2}\geq{0}$. But what does $\sqrt{x^2}$ equal to?

Let's consider following examples:
If $x=5$ --> $\sqrt{x^2}=\sqrt{25}=5=x=positive$;
If $x=-5$ --> $\sqrt{x^2}=\sqrt{25}=5=-x=positive$.

So we got that:
$\sqrt{x^2}=x$, if $x\geq{0}$;
$\sqrt{x^2}=-x$, if $x<0$.

What function does exactly the same thing? The absolute value function! That is why $\sqrt{x^2}=|x|$

Back to the original question:

So $\sqrt{(x-3)^2}=|x-3|$ and the question becomes is: $|x-3|=3-x$?

When $x>3$, then RHS (right hand side) is negative, but LHS (absolute value) is never negative, hence in this case equations doesn't hold true.

When $x\leq{3}$, then $LHS=|x-3|=-x+3=3-x=RHS$, hence in this case equation holds true.

Basically question asks is $x\leq{3}$?

(1) $x\neq{3}$. Clearly insufficient.

(2) $-x|x| >0$, basically this inequality implies that $x<0$, hence $x<3$. Sufficient.

Answer: B.

[Discussione su GMAT Club](http://gmatclub.com/forum/gmat-prep-q-92204.html)

---

## 55. Word Problem

Each employee on a certain task force is either a manager or a director. What percentage of the employees are directors
(1) Average salary for manager is \$5,000 less than average of all employees.
(2) Average salary of directors is \$15,000 greater than average salary of all employees

$S_a$ - Average salary of all employees
$S_m$ - Average salary for manager
$S_d$ - Average salary of directors
$d$ - # of directors;
$m$ - # of managers.
Question $\frac{d}{m+d}=?$

(1) $S_m=S_a-5000$ --> Not sufficient to calculate ratio.
(2) $S_d=S_a+15000$ --> Not sufficient to calculate ratio.

(1)+(2) $S_a=\frac{S_m*m+S_d*d}{d+m}$ --> substitute $S_m$ and $S_d$ --> $S_a=\frac{(S_a-5000)*m+(S_a+15000)*d}{d+m}$ --> $S_a*d+S_a*m=S_a*m-5000*m+S_a*d+15000*d$ --> $S_a*d$ and $S_a*m$ cancel out --> $m=3d$ --> $\frac{d}{m+d}=\frac{d}{3d+d}=\frac{1}{4}$. Sufficient.

Answer: C.

[Discussione su GMAT Club](http://gmatclub.com/forum/gmat-prep-test-92076.html)

---

[<- I materiali](../README.md)
