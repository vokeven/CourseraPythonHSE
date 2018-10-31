# Штаб гражданской обороны Тридесятой области решил обновить
# план спасения на случай ядерной атаки. Известно, что все n
# селений Тридесятой области находятся вдоль одной прямой
# дороги. Вдоль дороги также расположены m бомбоубежищ,
# в которых жители селений могут укрыться на случай ядерной атаки.
#
# Чтобы спасение в случае ядерной тревоги проходило
# как можно эффективнее, необходимо для каждого селения
# определить ближайшее к нему бомбоубежище.

# import unittest

def nearestTomb(n, m, distS, distM):
    distS_new = []
    distM_new = []
    for i, a in enumerate(distS):
        distS_new.append((a, i))
    for j, b in enumerate(distM):
        distM_new.append((b, j+1))
    distS_new.sort()
    distM_new.sort()
    res = [0]*n

    for x, y in distS_new:
        while k < len(distM_new):
            if k == len(distM_new) - 1:
                res[y] = distM_new[k][1]
                break
            elif (x - distM_new[k][0]) ** 2 >= (x - distM_new[k+1][0]) ** 2:
                k += 1
            else:
                res[y] = distM_new[k][1]
                break
    return res


n = int(input())
distS = list(map(int, input().split()))
m = int(input())
distM = list(map(int, input().split()))
print(*nearestTomb(n, m, distS, distM))

'''
class TestGO(unittest.TestCase):
    def test_1(self):
        self.assertEqual(nearestTomb(4, 2, [1, 2, 6, 10], [7, 3]), [2, 2, 1, 1])

    def test_2(self):
        self.assertEqual(nearestTomb(10, 10, \
        [79, 64, 13, 8, 38, 29, 58, 20, 56, 17], \
        [53, 19, 20, 85, 82, 39, 58, 46, 51, 69]),\
        [5, 10, 2, 2, 6, 3, 7, 3, 7, 2])

unittest.main()
'''