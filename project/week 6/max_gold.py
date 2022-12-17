# Uses python3
import sys

def optimal_weight(W, w):
    OPTIMAL_VALUE=[[0 for i in range(W+1)] for i in range(len(w)+1)]
    for i in range(1,len(w)+1):
        for j in range(1,W+1):
            if w[i-1]<=j:
                OPTIMAL_VALUE[i][j] = OPTIMAL_VALUE[i-1][j-w[i-1]] + w[i-1]
            value=OPTIMAL_VALUE[i-1][j]
            if value>OPTIMAL_VALUE[i][j]:
                OPTIMAL_VALUE[i][j]=value
    return OPTIMAL_VALUE[len(w)][W]
        

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
    