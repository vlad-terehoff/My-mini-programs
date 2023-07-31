from random import choice
word_list = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'система',
             'отношение', 'женщина', 'деньги', 'машина', 'проблема', 'решение', 'история', 'власть', 'тысяча',
             'возможность', 'результат', 'область', 'статья', 'компания', 'группа', 'развитие', 'процесс', 'условие',
             'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие', 'государство', 'любовь',
             'взгляд', 'общество', 'деятельность', 'организация', 'президент', 'комната', 'порядок', 'момент',
             'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание', 'смерть', 'программа', 'задача',
             'предприятие', 'разговор', 'правительство', 'производство', 'информация', 'положение', 'интерес',
             'федерация', 'правило', 'управление', 'мужчина', 'партия', 'сердце', 'движение', 'материал', 'неделя',
             'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
             'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка', 'очередь', 'состав',
             'количество', 'событие', 'объект', 'создание', 'значение', 'период', 'искусство', 'структура', 'пример',
             'исследование', 'гражданин', 'начальник', 'принцип', 'воздух', 'характер', 'борьба', 'использование',
             'размер', 'образование', 'мальчик', 'представитель', 'участие', 'девочка', 'политика', 'картина', 'доллар']
def get_word():
    return choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def len_ans(n):
    o = [i for i in n]
    return len(o)

def check_letters(letter):
    letter_up = letter.upper()
    
    if letter_up not in guessed_letters:
        guessed_letters.append(letter_up)
        
    else:
        return False

def check_words(word):
    word_up = word.upper()
    
    if word_up not in guessed_words:
        guessed_words.append(word_up)
        
    else:
        return False
    
def search_letter(d):
    if d in word:
        for i in range(len(word)):
            e = word[i]
            if e == d:
                a[i] = d
        return ''.join(a)
    else:
        return 'Этой буквы в слове нет'   
    
    
print('Добро пожаловать в игру - Поле чудес!','Хотите попытать удачу и сыграть?', 'Если Вы готовы скажите Да или Нет!', sep='\n' )    
ans = input()    
while ans.lower() == 'да':
    word = get_word()
    len_secret_word = len(word)
    print(f'Слово состоит из: {len_secret_word} букв!')
    print('У вас есть всего 6 попыток, чтобы отгадать слово!')
    print('_'* len_secret_word)
    c = 6
    guessed_letters = []
    guessed_words = []
    new_word = '_' * len(word)
    a = [_ for _ in new_word]
    
    while c != 0:
        guessed_ans = input('Введите вашу букву или слово целиком:').upper()
        length = len_ans(guessed_ans)

        if  not guessed_ans.isalpha():
            print('Вводите только буквы!')
            print(display_hangman(c))
            c -= 1
            print(f'У вас осталось: {c} попыток!')
            continue
        if length == 1:
            if check_letters(guessed_ans) == False:
                print('Вы вводили уже эту букву!')
                print('Попытка не засчитана!')
                c +=1
            else:
                print('Мы запомнили букву!')
                print(search_letter(guessed_ans))
        elif 1 < length < len_secret_word or (length > len_secret_word):
            if check_words(guessed_ans) == False:
                print('Вы вводили уже это слово!')
                print('Попытка не засчитана!')
                c +=1                
            else:
                print('Мы запомнили слово, но вводите слово равное длине загадоного!')
        elif length == len_secret_word:
            if guessed_ans.upper() == word or ''.join(a) == word:
                print('Поздравляем вы угодали слово!')
                break
            elif check_words(guessed_ans) == False:
                print('Вы вводили уже это слово!')
                print('Попытка не засчитана!')
                c +=1
                
            else:
                print('Хоть букв и столько но это не то слово, хотя мы его тоже запомнили!')                
#        elif guessed_ans.upper() == word or ''.join(a) == word:
            
#            print('Поздравляем вы угодали слово!')
#            break
        

#        else:
#            print('Вводите только буквы!')
        print(display_hangman(c))

        c -= 1
        print(f'У вас осталось: {c} попыток!')
 
    if c == 0:
        print(display_hangman(c))
        print('Вы проиграли!')
        print('Загадоное слово было -', word)
    ans = input('Хотите продолжить?:')
    




























