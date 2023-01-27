a=0
b=0
count=0
do=0
a=input( "Введите первое число:")
while (count<1):
count=input( "Введите кол-во действий:")
count=int(count)
if count<1:print("Больше нуля, плиз")
for i in range(0,count):
do=input("Выберете действие: +,-,/,*\nИли любое другое, для выхода из программы:")
match do.split():
case["+"]:
b=input(f"Введите второе число, {a}+")
a=float(a)+float(b)
case["-"]:
b=input(f"Введите второе число, {a}-")
a=float(a)-float(b)
case["/"]:
b=input(f"Введите второе число, {a}/")
a=float(a)/float(b)
case["*"]:
b=input(f"Введите второе число, {a}*")
a=float(a)* float(b)
case _:
break
print(f"Ответ={a}")