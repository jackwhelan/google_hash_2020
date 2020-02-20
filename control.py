datasets = [
    "b_read_on",
    "c_incunabula",
    "d_tough_choices",
    "e_so_many_books",
    "f_libraries_of_the_world"
]

total_books = dict()
amt_libraries = dict()
days_to_scan = dict()
book_scores = dict()
books_scanned = list()
days_left = 1000

for dataset in datasets:
    current_dataset = open("data\\" + dataset + ".txt", "r", encoding="ascii")

    info = current_dataset.readlines()

    total_books[dataset] = info[0].split()[0]
    amt_libraries[dataset] = info[0].split()[1]
    days_to_scan[dataset] = info[0].split()[2]
    book_scores[dataset] = info[1].split()

    # for count, line in enumerate(current_dataset.readlines(), start=3):
    #     if count % 2 == 0:
    #         print(line)

    library = list()
    lib_count = 0

    for count, line in enumerate(info):
        if count > 1 and count % 2 == 0:
            lib_info = line.split()
            current_library = list()
            if len(lib_info) > 0:
                current_library.append(lib_info[0])
                current_library.append(lib_info[1])
                current_library.append(lib_info[2])
                current_library.append(count+1)
                library.append(current_library)
        lib_count += 1
    break
