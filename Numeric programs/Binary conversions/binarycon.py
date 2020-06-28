d = float(input("entre a decimal num less that zero "))
b_w = ''

x = 1
while((d*(2**x))%1 != 0):
	x = x + 1


w = d*(2**x)
w = int(w)

while (w != 0):
	b_w = str(w%2) + b_w
	w= w//2

for i in range(x-len(b_w)):
	b_w = '0' + b_w

result  = b_w[ :-x] + "." + b_w[-x:]

print(result)