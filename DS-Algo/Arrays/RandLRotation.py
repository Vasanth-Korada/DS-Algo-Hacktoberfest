
"""

Given a String and Interger to Roatate Left or Right

EXAMPLE :

    Enter the Rotation value: 5
    Enter the string to Rotate L & R: HacktoberFest
    After Left Rotating: oberFestHackt
    After Right Rotating: rFestHacktobe

"""

def rotLeft(a, d):
    a = a[d%len(a) : ] + a[ : d%len(a)]
    return a
def rotRight(a, d):
    a = a[-d%len(a) : ] + a[ : -d%len(a)]
    return a
    
d = int(input("Enter the Rotation value: "))
a = input("Enter the string to Rotate L & R: ").strip()
LeftResult = rotLeft(a, d)
print("After Left Rotating:",LeftResult)
RightResult = rotRight(a,d)
print("After Right Rotating:",RightResult)