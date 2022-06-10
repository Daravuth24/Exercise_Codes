def selection_sort(names):
    for i in range(0, len(names)):
        min = i
        for j in range(i, len(names)):
            if len(names[j]) < len(names[min]):
                min = j
        names[i], names[min] = names[min], names[i]
        print(names)


selection_sort(["Thearin", "Sara Pich", "Daravuth", "Sen", "Panha"])