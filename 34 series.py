def find(n):
	a = [''] * (n + 1)
	s = 1
	m = 1
	while (s <= n):
		i = 0
		while(i < m and (s + i) <= n):
			a[s + i] = "3" + a[s - m + i]
			i += 1
		i = 0
		while(i < m and (s + m + i) <= n):
			a[s + m + i] = "4" + a[s - m + i]
			i += 1
		m = m << 1
		s = s + m
	print(a[n])


i = int(input())
for i in range(1, i):
	find(i+1)
