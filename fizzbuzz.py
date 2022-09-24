#This is my solution to the most famous interview question 

class Solution:

    def fizzbuzz(x):
        for i in range(x+1):
            if i == 0:
                pass
            else:
                if i % 3 == 0:
                    if i % 5 == 0:
                        print('FizzBuzz')
                    else:
                        print('Fizz')
                elif i % 5 == 0:
                    print('Buzz')
                
                else:
                    print(i)

    fizzbuzz(15)
