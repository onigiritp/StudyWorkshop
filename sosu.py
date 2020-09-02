

def main():
    num = int(input("いくつまでの素数を足しますか・・・"))
    sosu(num)

def sosu(num):

    sum_data = 0
    for i in range(2,num):
        if i == 2:
            sum_data += i
        else:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                sum_data += i
    print(sum_data)

main()
print("Yeeee")