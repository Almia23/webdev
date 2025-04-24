def DivExp(a,b):
    assert a>0, "a must be > 0"
    if b==0: raise ZeroDivisionError("b can't be 0")
    return a/b

a,b = map(int, input("Enter a b: ").split())
try: print("Result:", DivExp(a,b))
except Exception as e: print(e)