# Системный администратор вспомнил, что давно не делал архива
# пользовательских файлов. Однако, объем диска, куда он может
# поместить архив, может быть меньше чем суммарный объем
# архивируемых файлов.
#
# Известно, какой объем занимают файлы каждого пользователя.
#
# Напишите программу, которая по заданной информации о пользователях
# и свободному объему на архивном диске определит максимальное
# число пользователей, чьи данные можно поместить в архив.


def maxUsers(volumeList, s):
    volumeList.sort()
    leftVolume = s
    j = 0
    k = 0
    while leftVolume >= 0 and j < len(volumeList):
        leftVolume -= volumeList[j]
        if leftVolume >= 0:
            k += 1
            j += 1
    return k


s, n = list((map(int, input().split())))
volumeList = [int(input()) for i in range(n)]
print(maxUsers(volumeList, s))
