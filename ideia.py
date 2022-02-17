number = int(input("Digite um valor:"))
digits = [int(_) for _ in str(number)]

number_of_digits = len(str(number))

digits_ele = list([])
i_ele = 0
for i in digits:
  i_ele = i**number_of_digits
  digits_ele.append(i_ele)
digits = digits_ele

total = sum(digits)

if total == number:
  print("Numero de Armstrong")
else: 
  print("Nao e um numero de Armstrong")