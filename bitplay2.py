def setOrNot (number, n):
    mask = 1
    if(n & mask) == 1 or (n & mask) == 0:
         mask2 = 1<<(n-1)
         if number & mask2:
            print("It is a set")
         else:
            print("It is not set")
number = int(input("Enter the number :"))
n = int(input("Enter the place position of bit :"))
setOrNot(number, n)
   