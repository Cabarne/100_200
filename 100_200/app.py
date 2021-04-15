
app = open("in.txt", "r")
info = app.read()

a = []
b = []

for i in info: 
    if i != " ":      
        a.append(i)             # создаем новый список a[] до "пробела"
    else:
        break

for i in info: 
    b.append(i)                 # создаем новый список b[]
    if i == " ":
        b.remove(" ")           # удаляем из списка b[] "пробел"

for i in range(len(a)):
    b.remove(a[i])              # удаляем из списка b[] все что содержится в a[]
    
a = "".join(a)                  # соединяем в одну строку все что в a[]
b = "".join(b)                  # соединяем в одну строку все что в b[]
b = int(b)
a = int(a)
r = a + b
print(r, type(r))   

