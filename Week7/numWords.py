# Во входном файле (вы можете читать данные из sys.stdin,
# подключив библиотеку sys) записан текст. Словом считается
# последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или
# символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.

if __name__ == '__main__':
    with open('input.txt', encoding='utf-8') as f:
        s = f.read().strip().split()
        res = len(set(s))
    print(res)
