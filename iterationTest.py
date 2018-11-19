# -*- coding: utf-8 -*-
def findMinAndMax(L):
	t = ()
	if L == []:
		return (None,None)
	else:
		for n in L:
			t.add(n)

	if t[1]:
		for m in t:
			a = 0
			b = 0
			for n in L:
				if n > m:
					a + 1
				elif n < m:
					b + 1
				else:
					continue
			if a > 0 and b > 0:
				t.pop(m)
			else:
				break
		return t	
	else:
		return t
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')



				
