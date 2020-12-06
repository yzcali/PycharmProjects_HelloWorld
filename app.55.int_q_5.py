# question :Write a function that prints
# all the prime numbers between 0 and limit
# where limit is a parameter.

def prime_number(limit):
    if limit < 2:
        print("not prime")
        return
    elif limit == 2:
        print(2)
        return
    else:
        print(2)
        for i in range(3, limit):
            divided = False
            for j in range(2, i):
                if i % j == 0:
                    divided = True
                    break
            if not divided:
                print(i)


prime_number(10)
