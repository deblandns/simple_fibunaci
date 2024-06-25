while True:
    entered_number = int(input('enter domain number you want to get from number'))
    num : int = 1
    count: int = 0
    second_num: int = 0

    while num <= entered_number:
        a = num + second_num
        count += 1
        second_num, num = num, a
        print(num)
