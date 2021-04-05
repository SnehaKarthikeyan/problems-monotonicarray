Coding:
  
def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

n=int(input())
A = list(input().split())
if(isMonotonic(A)==True):
    print("YES")
else:
    print("NO")
