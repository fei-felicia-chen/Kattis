sequence = input()
zero, one, two, ans = 0, 0, 0, 0
for c in sequence:
	if c == '0':
		zero += 1
		ans += one + two
	elif c == '1':
		one += 1
		ans += two
	else:
		two += 1
print(ans)