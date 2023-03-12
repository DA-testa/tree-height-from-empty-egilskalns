# python3

import sys
import threading

def compute_height(n, parents):
    check=[0]*n
    height=[0]*n

    for i in range(n):
        j=0
        m=i
        if check[i]==1:
            continue
        if check[parents[i]]==1:
            height[i]+=height[parents[i]]
            continue
        while m!=-1:
            check[m]=1
            m=parents[m]
            j+=1
        
        height[i]+=j
    
    max_height = 0

    for i in height:
        if i>max_height:
            max_height=i
    return max_height


def main():
    text1=input()
    if text1=="F":
        text3="/workspaces/tree-height-from-empty-egilskalns/test/"
        text2=input()
        if "a" not in text2:
            file=open(text3+text2,"r")
            text4=file.read()
            file.close()
            text4=text4.replace("\n"," ")
            text4=text4.strip()
            parents=[int(i) for i in text4.split(' ')]
            n=parents[0]
            parents=parents[1:]
            print(compute_height(n,parents))
            
    if text1 == "I":
        n = int(input())
        text=input()
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
