"""
The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move 
the entire stack to another rod. You are given the number of discs N. Initially, these discs are in the rod 1. You 
need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.

Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. Also, all 
the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc. Refer the provided link
to get a better clarity about the puzzle.
EXAMPLE: 
For Input (N = 2) 
Output:
move disk 1 from rod 1 to rod 2
move disk 2 from rod 1 to rod 3
move disk 1 from rod 2 to rod 3
3
"""
# TC-O((2^n)-1) SC-O(n)
def toh(N, fromm, to, aux):
    count=0

    def helper(N, fromm, to, aux):
        nonlocal count
        if N==1:
            count+=1
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            return

        helper(N-1, fromm, aux, to)
        count+=1
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        helper(N-1, aux, to, fromm)

        return count
        
    return helper(N, fromm, to, aux)

print(toh(3, 1,3,2))