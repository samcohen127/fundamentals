#Basic - Print all integers from 0 to 150
print("Basic")
for i in range(151):
    print(i)
    
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print("Multiples of Five")
for i in range(5,1001,5):
    print(i)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
print("Counting, the Dojo Way")
for i in range(1,101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)
    
#Woah, Thats Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
print("Woah, That Suckers Huge")
big_sum = 0
for i in range(500000):
    big_sum = big_sum+i
print(big_sum)
 
#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
print("Countdown by Fours")
for i in range(2018,-1,-4):
    print(i)

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
print("Flexible Counter")
lowNum = 2
highNum = 69
multi = 4
for i in range(lowNum,highNum):
    if i%multi==0:
        print(i)
