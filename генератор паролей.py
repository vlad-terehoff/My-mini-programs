from random import *
digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
similar_symbols = 'il1Lo0O'

def len_pass_world():
    lenpass = 0
    if pw_digits.lower() == 'да':
        lenpass += 8
    if pw_up.lower() == 'да':
        lenpass += 24
    if pw_low.lower() == 'да':
        lenpass += 23        
    if pw_symbols.lower() == 'да':
        lenpass += 13       
    if pw_similar_symbols.lower() == 'нет':
        lenpass += 7
    return lenpass
    
def cheking_len(n):
    while True:
        if 1 <= n <= b:
            break
        else:
            print('Введите корректное колличество символов')
            n = int(input())

def filling_chars():
    chars = ''
    if pw_digits.lower() == 'да':
        chars += digits
    if pw_up.lower() == 'да':
        chars += uppercase_letters
    if pw_low.lower() == 'да':
        chars += lowercase_letters        
    if pw_symbols.lower() == 'да':
        chars += punctuation       
    if pw_similar_symbols.lower() == 'нет':
        chars += similar_symbols
    return chars    

def generate_pass(c, e):
    for i in range(1, e +1):
        m = ('').join(sample(c, lenPw))
        print(f'По вашему запросу это {i} пароль: {m}')
#        print(*sample(c, lenPw), sep='')
ans = input('Хотите сгенерировать пароли? Ответьте Да или Нет:')
while True:
    
    if ans.lower() == 'да':
        
        pw_digits = input('Включать ли цифры 23456789?; д = да, н = нет :')
        pw_up = input('Включать ли прописные буквы ABCDEFGHIJKMNPQRSTUVWXYZ?; д = да, н = нет :')
        pw_low = input('Включать ли строчные буквы abcdefghjkmnpqrstuvwxyz?; д = да, н = нет :')
        pw_symbols = input('Включать ли символы !#$%&*+-=?@^_ ?; д = да, н = нет :')
        pw_similar_symbols = input('Исключать ли неоднозначные символы il1Lo0O ?; д = да, н = нет :')
        b = len_pass_world()
        cntPw = int(input('Укажите количество паролей для генерации:'))
        lenPw = int(input(f'Укажите длину одного пароля, обратите внимание, что длина пароля не может привышать {b} символов:'))
        cheking_len(lenPw)
        char_list = filling_chars()
        generate_pass(char_list, cntPw)
        ans = input('Хотите ли сгенерировать еще пароли? Ответьте Да или Нет: ')
    else:
        break
   
    
    