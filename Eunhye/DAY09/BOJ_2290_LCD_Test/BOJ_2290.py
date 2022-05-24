# (0) 맨 위 가로 줄,
# (1) 첫 번째 왼쪽 세로 줄, (2) 오른쪽 세로 줄, 
# (3) 중간 가로 줄,
# (4) 두 번째 왼쪽 세로 줄, (5) 오른쪽 세로 줄,
# (6) 맨 아래 가로 줄
numbers = {
    "1": [" ", " ", "|", " ", " ", "|", " "],
    "2": ["-", " ", "|", "-", "|", " ", "-"],
    "3": ["-", " ", "|", "-", " ", "|", "-"],
    "4": [" ", "|", "|", "-", " ", "|", " "],
    "5": ["-", "|", " ", "-", " ", "|", "-"],
    "6": ["-", "|", " ", "-", "|", "|", "-"],
    "7": ["-", " ", "|", " ", " ", "|", " "],
    "8": ["-", "|", "|", "-", "|", "|", "-"],
    "9": ["-", "|", "|", "-", " ", "|", "-"],
    "0": ["-", "|", "|", " ", "|", "|", "-"],
}

s, n = input().split()
s = int(s)
i = 0
while i < 7:
    row = ""
    if i % 3:
        for num in n:
            row += numbers[num][i] + " "*s + numbers[num][i+1]
            row += " "
        for _ in range(s):
            print(row)
        i += 2
    else:
        for num in n:
            row += " " + numbers[num][i]*s + " "
            row += " "
        print(row)
        i += 1
        