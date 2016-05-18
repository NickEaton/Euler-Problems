def digitSum(x):
    sum = 0
    while(x/10 >= 1):
        sum += x % 10
        x /= 10
    return sum

def div23(x):
    return x % 23 == 0

def check(x):
    if(digitSum(x) == 23 and div23(x)):
        return 1
    else:
        return 0

def main():
    sum = 0
    y = eval(input('Enter the max value to check '))
    for i in range(0, y, 23):
        print(str(i))
        sum += check(i)
    print('The number of acceptable values is: ' + str(sum))

if(__name__ == '__main__'): main()
