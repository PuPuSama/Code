while True:
    try:
        per_person, num_students = map(int, input("请输入每人分到的数量和同学的人数，用空格分隔：").split())
        if 1 <= per_person <= 9999 and 1 <= num_students <= 9999:
            break  # 如果输入的都是符合要求的正整数，结束循环
        else:
            print("输入有误，请确保输入的是1到9999之间的正整数")
    except ValueError:
        print("输入有误，请确保输入的是1到9999之间的正整数")

total_apples = per_person * num_students
print(total_apples)