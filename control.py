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

# print(library, "\n\n\n")

# library_sorted = list()
# for lib in library:
#     library_sorted.append(lib.sort())

# print(library, "\n\n\n")

def calcVal(library):
    books, days_to_reg, books_per_day, books_index = library
    books = int(books)
    days_to_reg = int(days_to_reg)
    books_per_day = int(books_per_day)

    days_taken = days_to_reg
    while books > 0:
        books -= books_per_day
        days_taken += 1
    return days_taken

def addable(days_left, library):
    books, days_to_reg, books_per_day, books_index = library
    books = int(books)
    days_to_reg = int(days_to_reg)
    books_per_day = int(books_per_day)
    days_left = days_left - days_to_reg
    readable = days_left * books_per_day
    return readable, days_left

new_library = list()
for item in library:
    value = calcVal(item)
    new_library.append([calcVal(item), item])

sorted_library = sorted(new_library, key=lambda x: x[0])

addable_library = list()
for score, library in sorted_library:
    add_score, new_days_left = addable(days_left, library)
    days_left = new_days_left
    library.append(add_score)
    addable_library.append(library)
