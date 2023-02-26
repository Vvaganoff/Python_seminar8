# Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста.
# У нас труб будет больше.
#
# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего
# бассейна только одной данной работающей трубой (в часах). Затем после пустой строки перечислены трубы,
# которые будут заполнять бассейн. Сколько минут на это потребуется?
#
# Номер трубы соответствует номеру строки, в которой записана ее производительность.
#
# Результат запишите в файл time.txt
#
# Пример
# Ввод
#
# 1
# 2
# 3
# (пустая строка)
# 1 2 3
#
# Вывод
# 32.72727272727273

list_of_pipes = []
with open('pipes.txt', 'r', encoding='utf-8') as pipes:
    for lines in pipes:
        if lines.strip() != "":
            list_of_pipes.append(int(lines.strip()))
        else:
            break

speed_hour = 0
for i in list_of_pipes:
    speed_hour = speed_hour + 1/i
speed_minute = speed_hour/60
time_fill = 1/speed_minute

with open('time.txt', 'w', encoding='utf-8') as time_file:
    time_file.write(str(time_fill))