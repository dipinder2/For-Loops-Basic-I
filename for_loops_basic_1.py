'''
Basic - Print all integers from 0 to 150.
'''
for num in range(150+1):
    print(num)
'''
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
'''
for i in range(0,1000,5):
    print(i)
'''
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
'''
for i in range(1, 100):
    if i%10==0:
        print("Coding Dojo")
    if i%5==0:
        print("Coding")
        continue
    print(i)
'''
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
'''
final_sum = 0
for i in range(0,500000):
    if i%1==0:
        final_sum+=i
print(final_sum)
'''
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
'''
for year in range(2018,0,-4):
    print(year)
'''
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
'''

low_num=2
high_num=9
mult = 3
for i in range(low_num,high_num+1):
    if i%mult == 0:
        print(i)