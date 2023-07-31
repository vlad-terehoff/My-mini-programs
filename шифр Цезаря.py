def cesar(ch,sdvig):
    ordch = ord(ch)
    if 65 <= ordch <= 90:
        lg = 65
        pg = 90
        dm = 26
    elif 97 <= ordch <= 122:
        lg = 97
        pg = 122
        dm = 26
    elif 1040 <= ordch <= 1071:
        lg = 1040
        pg = 1071
        dm = 32
    elif 1072 <= ordch <= 1103:
        lg = 1072
        pg = 1103
        dm = 32
    else:
        return(ch)
    return(chr(lg + (ord(ch)-lg + sdvig)%dm))

print('Введите текст для шифрования')
text = input()
print('На какую величину будем делать сдвиг? Ввод значения с МИНУСОМ - дешифрует текст!')
sdvig = int(input())
b = [i for i in text if i.isalnum() or i.isspace()]
c = ''.join(b)
c = c.split()
for _ in range(len(c)):
    t = len(c[_])
for i in range(len(text)):
    print(cesar(text[i],sdvig),end ='')