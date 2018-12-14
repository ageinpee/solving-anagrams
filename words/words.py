import itertools
import numpy as np
import time

with open('deutsch.txt', 'r') as file:
    german_words = [line.strip().upper() for line in file]

    german_words_np = np.asarray(german_words)
    german_words_set = set(german_words)

with open('top10000de.txt', 'r') as file:
    german_words2= [line.strip().upper() for line in file]

    german_words_np2 = np.asarray(german_words2)
    german_words_set2 = set(german_words2)

with open('wortliste.txt', 'r') as file:
    german_words3= [line.strip().upper() for line in file]

    german_words_np3 = np.asarray(german_words3)
    german_words_set3 = set(german_words3)

print("deutsch.txt // evaluates " + str(len(german_words_set)) + " words")
print("top10000.txt // evaluates " + str(len(german_words_set2)) + " words")
print("wortliste.txt // evaluates " + str(len(german_words_set3)) + " words")

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

##----------------------------------------------------------------

def calc_np(a, b, c, d, e='', f='', g='', h='', i='', j='', k='', l=''):
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
        if solution in german_words_np:
            found_flag = True
            final_solutions.append(solution)
        if i%100 == 0:
            print("Check word "+str(i)+" of "+str(len(solutions))+"\r")

    if found_flag == True:
        print("\n" + "Finished Search successfully")
        print(final_solutions)
    else:
        print("\n" + "no matching words found.")

##----------------------------------------------------------------

def calc_set(a, b, c, d, e='', f='', g='', h='', i='', j='', k='', l=''):
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

    solutions = set()
    for solved_word in itertools.permutations(word):
        solutions.add(''.join(solved_word))

    solutions = set(solutions)

    print(len(solutions))
    final_solutions = set()
    found_flag = False
    for i, solution in enumerate(solutions):
        if solution in german_words_set:
            found_flag = True
            final_solutions.add(solution)
        if solution in german_words_set2:
            found_flag = True
            final_solutions.add(solution)
        if solution in german_words_set3:
            found_flag = True
            final_solutions.add(solution)
        #if i%100 == 0:
            #print("Check word "+str(i)+" of "+str(len(solutions))+"\r")

    if found_flag == True:
        print("\n" + "Finished Search successfully")
        print(final_solutions)
        print("----------------------------")
    else:
        print("\n" + "no matching words found")
        print("----------------------------")

def input(word):
    word = list(word.upper())
    dif = 12-len(word)
    for i in range(dif):
        word.append('')
    return word[0], word[1], word[2], word[3], word[4], word[5], word[6], word[7], word[8], word[9], word[10], word[11]

##-------------------------------------------------------
##=======================================================
##-------------------------------------------------------

start = time.time()
print("word 1")
calc_set(*input("freenst"))
print("word 2")
calc_set(*input("treiten"))
print("word 3")
calc_set(*input("adinost"))
print("word 4")
calc_set(*input("addikant"))
print("word 5")
calc_set(*input("prionator"))
print("word 6")
calc_set(*input("teotelti"))
print("word 7")
calc_set(*input("grereist"))
print("word 8")
calc_set(*input("halzgnu"))
print("word 9")
calc_set(*input("keidroma"))
print("word 10")
calc_set(*input("wandkreh"))
print("word 11")
calc_set(*input("rindteig"))
print("word 12")
calc_set(*input("pechobrot"))
print("word 13")
calc_set(*input("strinkdich"))
print("word 14")
calc_set(*input("nachemtritt"))
print("word 15")
calc_set(*input("daergenle"))
print("word 16")
calc_set(*input("fundheutert"))
print("word 17")
print("toohard")
print("-------------------------")
#calc_set(*input("krechsaftweg"))
print("word 18")
calc_set(*input("knechges"))
print("word 19")
#calc_set(*input("sunnebohbton"))
print("toohard")
print("-------------------------")
print("word 20")
calc_set(*input("helgusteil"))
print("word 21")
calc_set(*input("sachpinsem"))
print("word 22")
calc_set(*input("amorkeid"))
print("word 23")
calc_set(*input("freinzieger"))
print("word 24")
calc_set(*input("bananenmut"))
print(time.time() - start)