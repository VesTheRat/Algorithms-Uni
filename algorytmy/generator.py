#generator i zapis danych do plików
def generator():
    n = [10,50,100,500,1000]

    random_arrs = []
    sorted_arrs = []

    for lenght in n:
        for i in range(10):
            arr = []
            for element in range(lenght):
                x = abs(random.randint(0, 500))
                arr.append(x)
            if i%2 == 0:
                random_arrs.append(arr)
            else:
                sorted_arrs.append(sorted(arr))

    with open("listy_random.txt", "w") as f:
        for array in random_arrs:
            row = " ".join(map(str, array))
            f.write(row + "\n")

    with open("listy_sorted.txt", "w") as f:
        for array in sorted_arrs:
            row = " ".join(map(str, array))
            f.write(row + "\n")
