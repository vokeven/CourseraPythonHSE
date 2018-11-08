# Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой
# набор и в каждом наборе все кубики различны по цвету. Однажды дети
# заинтересовались, сколько существуют цветов таких, что кубики каждого
# цвета присутствуют в обоих наборах. Для этого они занумеровали все цвета
# случайными числами. На этом их энтузиазм иссяк, поэтому вам предлагается
# помочь им в оставшейся части. Номер любого цвета — это целое число в
# пределах от 0 до 10⁹.

if __name__ == '__main__':
    with open('input.txt', encoding='utf-8') as f:
        n, m = tuple(map(int, f.readline().strip().split()))
        setA = set()
        setB = set()
        for i in range(n):
            setA.add(int(f.readline().strip()))
        for j in range(m):
            setB.add(int(f.readline().strip()))
        ins = setA & setB
        insList = list(ins)
        insList.sort()
        setA1 = list(setA - ins)
        setA1.sort()
        setB1 = list(setB - ins)
        setB1.sort()
    print(len(ins))
    print(*insList)
    print(len(setA1))
    print(*setA1)
    print(len(setB1))
    print(*setB1)
