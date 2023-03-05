# python3

import sys
import threading

def compute_height(n, parents):
    check=[]
    height=[]
    for i in range(0,len(parents)):
        check.insert(i,0)
        height.insert(i,0)

    for i in range(0,len(parents)):
        while True:
            if i==-1 or check[i]==1:
                break
            check.insert(i,1)
            height[i]+=1
            i=parents[i]
    max_height = 0
    for i in height:
        if i>max_height:
            max_height=i
    return max_height


def main():
    text=input()
    for i, next in enumerate(text):
        if next in "IF":
            text = input()
    n=text[0]
    text=text[2:]
    parents=[int(i) for i in text.split(' ')]
    print(compute_height(n,parents))

    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
