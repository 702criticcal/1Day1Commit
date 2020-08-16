word_list = []
result_list = []

for _ in range(0, int(input())):
    word_list.append(input())
word_list = list(set(word_list))

for i in range(0, 51):
    for j in sorted(word_list):
        if len(j) == i:
            result_list.append(j)

for result in result_list:
    print(result)
