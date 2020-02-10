## Exercise 1
import math
arr = []
def recursion(x):
    arr.append(x)
    if x !=0:
        recursion(x-1)
    return

def main():
    print("Please enter in the number: ")
    x = int(input())
    for i in range(x+1):
        recursion(x-i)
        print(*arr)        
        arr.clear()

main()

# Exercise 2

#import math

#def calculation(x):
#    number = []
#    a = 1
#    temp = 0
#    for z in range(x):
#        temp+=a
#        number.append(temp)
#        a=1+a
#    print(str(number)[1:-1])
#    return number


#def main():
#    print("please enter in the number: ")
#    x = int(input())
#    calculation(x)
       

#main()

## Exercise 3
#import math

#def USFTime(s):
#    x = (s.split(":"))
#    hours = 0
#    minutes = 0
#    seconds = 0
#    f_sec = 0
#    s_min = 0
#    u_hr = 0
#    if x[2][2] == 'P':
#            x[2] = x[2][:-2]
#            if x[0] == 12:
#                hours = 13
#            else:
#                hours = int(x[0]) + 12
#            minutes = int(x[1])
#            seconds = int(x[2])
#            seconds = seconds + (hours * 60 * 60) + (minutes * 60)
#            f_sec = seconds%45
            
#            seconds = seconds - f_sec
#            s_min = int((seconds/45)%60)
            
#            seconds = seconds - (s_min*45)
            
#            u_hr = int(((seconds/45)/60))
            
#    else:
#        x[2] = x[2][:-2]
#        if x[0] == 12:
#            hours = 1
#        else:
#            hours = int(x[0])
#        minutes = int(x[1])
#        seconds = int(x[2])
#        seconds = seconds + (hours * 60 * 60) + (minutes * 60)
#        f_sec = seconds%45
#        seconds = seconds - f_sec
#        s_min = int((seconds/45)%60)
        
#        seconds = seconds - (s_min*45)
            
#        u_hr = int(((seconds/45)/60))
#    if f_sec < 10:
#        finalsec = "0" + str(f_sec)
#    else:
#        finalsec = str(f_sec)
#    r = ":"
#    print("%s%s%s%s%s" % (u_hr, r, s_min, r, finalsec))
#    return


#def main():
#    print("Please enter the earth time")
#    s = str(input())
#    USFTime(s)

#main()

## Exercise 4
#def main():
#    print("Please enter in the number of itegers you wish to print(110 is the max)")
#    n = int(input())
#    while n > 110:
#        print("invalid number please try again")
#        n = int(input())
#    print("Please enter in the number per line:")
#    k = int(input())
#    while k > n:    
#        print("invalid number please try again")
#        k = int(input())
#    UsfNumbers(n,k)

#def UsfNumbers(n,k):
#    point = 1
#    out = ""
#    for x in range(n):
#        U = False
#        F = False
#        S = False
#        if (x+1)%3 == 0:
#            U = True
#        if (x+1)%5 == 0:
#            S = True
#        if (x+1)%7 == 0:
#            F = True
#        if point != 1:
#            out = out + ", "
#        #print(out)
#        if U and (not S) and (not F):
#            out = out + "U"
#        elif (not U) and S and (not F):
#            out = out +"S"
#        elif (not U) and (not S) and F:
#            out = out + "F"
#        elif U and S and (not F):
#            out = out + "US"
#        elif U and (not S) and F:
#            out = out + "UF"
#        elif (not U) and S and F:
#            out = out + "SF"
#        elif U and S and F:
#            out = out +"USF"
#        elif (not U) and (not S) and (not F):
#            out = out +  (str(x+1))

#        if point ==  k:
#            point = 1
#            print(out)
#            out = ""
#        else:
#            point = point + 1

     
#main()

## Exercise 5

#import re
#def reverse(s): 
#    return s[::-1] 
  
#def isPalindrome(s): 
#    # Calling reverse function 
#    rev = reverse(s) 
  
#    # Checking if both string are equal or not 
#    if (s == rev): 
#        return True
#    return False
  
  
#def main():
#    wordlist = []
#    finallist = ""
#    flag = 0
#    given = str(input())
#    given = re.sub('[!@#$",]', ' ', given)
#    given = given[1:-1]
#    wordlist = given.split()   
    
#    pointy = 0
#    pointz = 0
#    for y in wordlist:
       
#        for z in (wordlist):
           
#            if pointy == pointz:
#                empty = ""
#                pointz = pointz+1
#            else:
#                ans = isPalindrome(y + z)
    
#                if ans == 1:
#                    if flag == 0: 
#                        finallist = finallist + ("[["+str(pointy) + ", " + str(pointz) + "]") 
#                        flag = 1
#                        pointz = pointz + 1
#                    else:
#                        finallist = finallist + (", ["+str(pointy) + ", " + str(pointz) + "]") 
#                        pointz = pointz + 1
#                else: 
#                    empty = ""
#                    pointz = pointz+1
#        pointz = 0
#        pointy = pointy + 1
#    finallist = finallist + "]"
#    print (finallist)

#main()

## Exercise 6
# global list for the winning conditions
#winlist = []
#isWon = []


#def main():
#    print("please enter in the number of stones in the bag:")
#    stones = int(input())
#    hi = "["
#    turn = 1
#    isWon.append(False)
#    findWin(stones, hi, turn)
#    if isWon[0] == False:
#        print("FALSE")

#def findWin(stones, hi, turn):
#    if(stones - 1 == 0) and (turn%2 !=0):
#        isWon[0] = True
#        print (hi + "1]")
#        return
#    elif (stones - 2 == 0)and (turn%2 !=0):
#        isWon[0] = True
#        print (hi + "2] ")
#        return
#    elif (stones - 3 == 0)and (turn%2 !=0):
#        isWon[0] = True
#        print (hi + "3]")
#        return
#    elif (stones -1 != 0) and (stones - 2 != 0) and (stones - 3!=0):
#        if(stones-1) >=1:
#            findWin((stones - 1), hi + "1,", (turn + 1))
#        if (stones-2) >=1:
#            findWin((stones - 2), hi + "2,", (turn + 1))
#        if (stones - 3) >= 1:
#            findWin((stones - 3), hi + "3,", (turn + 1))
#    return

#main()