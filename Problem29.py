#distinct powers

if __name__ == '__main__':
    s = []
    for i in range(2, 101):
        for j in range(2, 101):
            s.append(i ** j)
    print(len(set(s)))