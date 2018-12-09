import itertools

with open('deutsch.txt', 'r') as file:
    german_words = [line.strip().upper() for line in file]


def calc(a, b, c, d, e='', f='', g='', h='', i='', j='', k='', l=''):
    word = [a, b, c, d]
    if e != '':
        word.append(e)
    if f != '':
        word.append(f)
    if g != '':
        word.append(g)
    if h != '':
        word.append(h)
    if i != '':
        word.append(i)
    if j != '':
        word.append(j)
    if k != '':
        word.append(k)
    if l != '':
        word.append(l)

    words = []
    for letter in word:
        words.append(word)

    combinations = list(itertools.product(*words))

    letter_count = {}
    for letter in word:
        letter_count[letter] = word.count(letter)

    solutions = []
    found_flag = False
    for solved_word in combinations:
        flag = True
        for letter in solved_word:
            if not solved_word.count(letter) == letter_count[letter]:
                flag = False
        solved_word = ''.join(solved_word)
        if flag:
            if solved_word in german_words:
                if solved_word not in solutions:
                    solutions.append(solved_word)
                found_flag = True

    print(solutions)
    if found_flag == True:
        print("\n" + "Finished Search successfully")
    else:
        print("\n" + "no matching words found.")

##-------------------------------------------------------

def calc_fast(a, b, c, d, e='', f='', g='', h='', i='', j='', k='', l=''):
    word = [a, b, c, d]
    if e != '':
        word.append(e)
    if f != '':
        word.append(f)
    if g != '':
        word.append(g)
    if h != '':
        word.append(h)
    if i != '':
        word.append(i)
    if j != '':
        word.append(j)
    if k != '':
        word.append(k)
    if l != '':
        word.append(l)

    solutions = []
    for solved_word in itertools.permutations(word):
        solutions.append(''.join(solved_word))

    solutions_set = set(solutions)
    solutions = list(solutions_set)

    final_solutions = []
    found_flag = False
    for i, solution in enumerate(solutions):
        if solution in german_words:
            found_flag = True
            final_solutions.append(solution)
        if i%100 == 0:
            print("Check word "+str(i)+" of "+str(len(solutions))+"\r")

    if found_flag == True:
        print("\n" + "Finished Search successfully")
        print(final_solutions)
    else:
        print("\n" + "no matching words found.")


##-------------------------------------------------------
##=======================================================
##-------------------------------------------------------

calc_fast("A", "D", "D", "I", "K", "A", "N", "T")