if __name__ == "__main__":
    answer = []

    for i in range(1, 6):
        s = input()

        if 'FBI' in s:
            answer.append(str(i))

        if i == 5:
            if len(answer) == 0:
                print("HE GOT AWAY!")
                exit()
            else:
                print(' '.join(answer))
                exit()
