A,B,C = input().split()

A = int(A)
B = int(B)
C = int(C)

if (A > B) and (B > C):
    print(f"{A}\n{B}\n{C}")
elif (B > A) and (A > C):
    print(f"{B}\n{A}\n{C}")
elif (C > A) and (B > A):
    print(f"{C}\n{B}\n{A}")
elif (A > C) and (C > B):
    print(f"{A}\n{C}\n{B}")
elif (B > C) and (C > A):
    print(f"{B}\n{C}\n{A}")
elif (C > B) and (B > A):
    print(f"{C}\n{A}\n{B}")