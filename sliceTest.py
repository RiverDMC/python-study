# -*- coding: utf-8 -*-
def trim(s):
	m = s
	if s == '':
		return m
	for n in s:
		if s == ' ':
			return m
		elif n == ' ':
			m = m[1:]
			continue
		elif m[-1] == ' ':
			m = m[:-2]
			continue
		else: break
	return m
 
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')