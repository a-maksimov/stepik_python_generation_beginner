from random import sample

word_list = ['Кант',
             'Хроника',
             'Зал',
             'Галера',
             'Балл',
             'Вес',
             'Кафель',
             'Знак',
             'Фильтр',
             'Башня',
             'Кондитер',
             'Омар',
             'Чан',
             'Пламя',
             'Банк',
             'Тетерев',
             'Муж',
             'Камбала',
             'Груз',
             'Кино',
             'Лаваш',
             'Калач',
             'Геолог',
             'Бальзам',
             'Бревно',
             'Жердь',
             'Борец',
             'Самовар',
             'Карабин',
             'Подлокотник',
             'Барак',
             'Мотор',
             'Шарж',
             'Сустав',
             'Амфитеатр',
             'Скворечник',
             'Подлодка',
             'Затычка',
             'Ресница',
             'Спичка',
             'Кабан',
             'Муфта',
             'Синоптик',
             'Характер',
             'Мафиози',
             'Фундамент',
             'Бумажник',
             'Библиофил',
             'Дрожжи',
             'Казино',
             'Конечность',
             'Пробор',
             'Дуст',
             'Комбинация',
             'Мешковина',
             'Процессор',
             'Крышка',
             'Сфинкс',
             'Пассатижи',
             'Фунт',
             'Кружево',
             'Агитатор',
             'Формуляр',
             'Прокол'
             'Абзац',
             'Караван',
             'Леденец',
             'Кашпо',
             'Баркас',
             'Кардан',
             'Вращение',
             'Заливное',
             'Метрдотель',
             'Клавиатура',
             'Радиатор',
             'Сегмент',
             'Обещание',
             'Магнитофон',
             'Кордебалет',
             'Заварушка']


def get_word(dictionary):
    random_word = sample(dictionary, 1)
    return random_word[0]


def char_spread(string):
    spread_string = ''
    for i in range(len(string)):
        spread_string += string[i] + ' '
    return spread_string


def check_letter(letter, word, string):
    for i in range(len(word)):
        if letter == word.lower()[i]:
            string = string[:i] + letter + string[i + 1:]
    return string


def check_word(guess_word, word):
    while not len(guess_word) == len(word):
        if len(guess_word) == 1:
            return
        else:
            guess_word = input(f'Слово должно быть из {len(word)} букв. Введите букву или слово.\n')
    if guess_word == word.lower():
        return True
    else:
        return False


# функция получения текущего состояния
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


def play(word):
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))

    answer = input('Показать первую и последнюю буквы? Да/Нет\n')
    while 'да' not in answer.lower() and 'нет' not in answer.lower():
        answer = input('Да или Нет?\n')
    if answer.lower() == 'да':
        word_completion = word[0] + word_completion[1:len(word_completion) - 1] + word[-1]

    print(char_spread(word_completion))

    while tries > 0:
        if word_completion == word.lower():
            guessed = True
            break

        guess = input('Введите букву или слово.\n')

        while not guess.isalpha():
            guess = input('Введите букву или слово.\n')

        guess = guess.lower()
        # Обработка слов
        if len(guess) > 1:
            while guess in guessed_words:
                guess = input('Это слово вы уже пробовали. Введите новое слово или букву.\n')
            guessed_words.append(guess)
            if check_word(guess, word):
                guessed = True
                break
            elif check_word(guess, word) is None:  # Если после слова была введена буква
                while guess in guessed_letters:
                    guess = input('Это букву вы уже пробовали. Введите новую букву.\n')
                guessed_letters.append(guess)
                word_completion = check_letter(guess, word, word_completion)
                print(char_spread(word_completion).capitalize())
        # Обработка букв
        else:
            while guess in guessed_letters:
                guess = input('Это букву вы уже пробовали. Введите новую букву.\n')
            guessed_letters.append(guess)
            word_completion = check_letter(guess, word, word_completion)
            print(char_spread(word_completion).capitalize())

        tries -= 1
        print(display_hangman(tries))

    if guessed:
        answer = input('Вы победили! Хотите сыграть еще? Да/Нет\n')
        while 'да' not in answer.lower() and 'нет' not in answer.lower():
            answer = input('Да или Нет?\n')
        if answer.lower() == 'да':
            play(get_word(word_list))
    else:
        answer = input('Вас повесили. Хотите попробовать снова? Да/Нет\n')
        while 'да' not in answer.lower() and 'нет' not in answer.lower():
            answer = input('Да или Нет?\n')
        else:
            print('Пока!')
        if answer.lower() == 'да':
            play(get_word(word_list))
        else:
            print('Пока!')


play(get_word(word_list))
