cs325
=====
Aaron Egger 
John Cargil 
Scott Malizio

Run-time analysis: Give pseudocode for each algorithm and an analysis of the asymptotic running-times of the algorithmes 

Algorithm 1: Enumeration Initially, mark each line as visible. Loop over each triple of indices j < i < k and compute the point of intersection (xj,k, yj (xj,k)) of the lines yj and yk. If yj (xj,k) > yi(xj,k), then mark yi as not visible.

Pseudo code: 

Algorithm 2: Better Enumeration Notice that in the previous algorithm, the same line may be tested for visibility multiple times after it has been marked as not visible. Write a new version of the first algorithm that stops testing a line for visibility after it has been marked as not visible.

Pseudo code:


Correctness: Prove that Claim 2 is correct and, given their claim, prove that your design for Algorithm 3 is correct. 

Claim 2: If {yj1, yj2, . . . , yjt} is the visible subset of {y1, y2, . . . , yi−1} (t ≤ i − 1) then
{yj1, yj2, . . . , yjk, yi} is the visible subset of {y1, y2, . . . , yi} where yjk is the last line such that yjk(x∗) > yi(x∗) where (x∗, yjk(x∗)) is the point of intersection of the lines yjk and yjk−1.


Claim 2 Proof: 
Let {Yj1, Yj2 …, YJt } be the visible subset of {Y1, Y2…, Yi-1} such that (t <= i-1) 
