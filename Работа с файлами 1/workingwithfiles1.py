# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
# что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
def Read_lines(lines, file="article.txt"):
    list_1 = []
    with open(file, "r", encoding='utf-8') as data:
        for line in data:
            list_1.append(line.strip())
    for i in range(len(list_1) - lines, len(list_1)):
        print(f'{i}. {list_1[i]}')


# Требуется реализовать функцию longest_words(file), которая выводит
# слово, имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file="article.txt"):
    list_1 = []
    list_2 = []
    maxword = ""
    with open(file, "r", encoding='utf-8') as data:
        for line in data:
           list_1.append(line.strip())
    for line in list_1:
        for word in line.split():
            if len(word) > len(maxword):
                 maxword = word
    for line in list_1:
        for word in line.split():
            if len(word) == len(maxword) and word != maxword:
                list_2.append(word)

    if len(list_2) == 0:
        print(f'Самое длинное слово: {maxword}')
    else:
        s = ", "
        print(f'Самые длинные слова: {maxword}, {s.join(list_2)}')




while True:
    lines_number = int(input("Введите количество строк: "))
    if lines_number <= 0:
        print("Надо ввести число больше ноля: ")
    else:
        Read_lines(lines_number)
        longest_words()
        break
