import pyttsx3
import speech_recognition
import time
import os

recogniser = speech_recognition.Recognizer()
microfon = speech_recognition.Microphone()


def init_engin():
    engin = pyttsx3.init('sapi5')
    voices = engin.getProperty('voices')
    #for i in voices:
        #print(i)
    engin.setProperty('voice', voices[2].id)
    engin.setProperty('volume', 0.5)
    rate = engin.getProperty('rate')
    #print(rate)
    engin.setProperty('rate', 185)
    return engin

def sound(engin, text):
    # вызываем функцию синтеза тектста в речь
    engin.say(text)
    # воспроизводим полученное аудио
    engin.runAndWait()


def recognizer_search():

    audio = ''
    with microfon:
        #global textnum
        textnum = ''
        recogniser.adjust_for_ambient_noise(microfon, duration=2)
        try:
            ask = 'Уважаемый пользователь, задайте команду начиная со слово: выключи компьютер'
            engin = init_engin()
            sound(engin, ask)
            print('скажите команду')
            audio = recogniser.listen(microfon, 5,5)
        except Exception as ex:
            print('ошибка: ', ex )
            return ''

        data = recogniser.recognize_google(audio, language='ru')
        return data.lower()

# функция выключения ПК. На вход принимает время, сранивает с текущим и выключает по достижении указанного
def off_computer(text):
    while True:

        time.sleep(10)

        time_1 = time.strftime("%H:%M")
        time_sum = []
        for tttt in time_1:
            time_sum.append(tttt)

        time_1 = ''.join(time_sum)
        time_1 = time_1.split()

        b = text

        if time_1 == b:
            print('время выклбчения ПКЖ', b)
            print('Текущее время ', time_1)
            os.system('shutdown -s')
            break

#off_computer('22:03') # проверка работоспособности функции

# ф-ция перобразования времени в случае задания времени четрыхначной цифрой
def clock_and_min(textnum = str):


    global rez_clok_and_min

    textnum_check = textnum.split()
    check_off = ['сейчас']
    rez_check_off = list(set(textnum_check) & set(check_off))
    # выполняем проверку на наличие в выражении о времни выключения.
    # Если нет данных, значит выклчение будет через 30 секунд.

    if textnum == '' or rez_check_off != []:
        rez_clok_and_min = '00:00' #прописать время на выключение через 30 секунд
        print("выключение через 30 сек: ", rez_clok_and_min)
        return rez_clok_and_min
    else:
        lst_unit = []
        for unut in range(0,2360):
            lst_unit.append(str(unut))

        textnum = ''.join(textnum)
        check_clock_min = []
        for i_check in textnum:
            check_clock_min.append(i_check)
        print(check_clock_min)
        checking_correctness = list(set(lst_unit) & set(check_clock_min))
        if checking_correctness == []:
            return print('неверные данные')
        else:
            if len(check_clock_min) < 4:
                textnum_lst1 =[]
                for tex_lst in textnum:
                    textnum_lst1.append(tex_lst)
                textnum = textnum_lst1
                textnum_clock = ''.join(textnum[0:1])
                textnum_minut = ''.join(textnum[1:len(textnum)])
                textnum_clock = "0" + textnum_clock
                print('час выключения', textnum_clock)
                print('минуты выключения', textnum_minut)
            else:
                textnum_lst =[]
                for i_text in textnum:
                    textnum_lst.append(i_text)
                textnum = textnum_lst

                textnum_clock = ''.join(textnum[0:2])

                textnum_minut = ''.join(textnum[2:len(textnum)])
                print('час выключения', textnum_clock)
                print('минуты выключения', textnum_minut)
            rez_clok_and_min = textnum_clock +':'+ textnum_minut
            rez_clok_and_min =rez_clok_and_min.split()
            print('время в которое выключиться ПК', rez_clok_and_min)
            return rez_clok_and_min


#clock_and_min( '201') # проверка работоспособности функции

# ф-ция определения ЧАСА [в] который необходимо выключить ПК
def clock_in(textnum = str, numwords={}):

    #print("textnum : ", textnum)
    global rez_clok_in
    #textnum = textnum.split()
    # выполняем проверку на наличие в выражении о времни выключения.
    # Если нет данных, значит выключение будет только в минутах

    if textnum == '':
        rez_clok_in = '00'
        print("выключение ПК в: ", rez_clok_in)
        return rez_clok_in
    #print(textnum[-1])
    textnum = textnum.split()
    #print("textnum[-1] = ",textnum[-1])

    if textnum[-1] == "часов" or textnum[-1] == 'часов' or textnum[-1] == 'час':
        if len(textnum)> 1:

            # отсекаем словов "часа"
            textnum = ' '.join(textnum[0:len(textnum)-1])
            textnum=textnum.split()
        #print(textnum)
        else:
            textnum = ' '.join(textnum[0:len(textnum)])
            textnum = textnum.split()


    if not numwords:
        units = [
            "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шеснадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать"        ]

        units_n = []
        for i in range(0, 16):
            units_n.append(str(i))

        units_1 = ["ноль", "одиу", "две"]

        hour_1 = ['ноль', 'час' ]

        #hour_05 = ['ноль', 'пол' ]

        #hour_1_5 = ["ноль", "полтора" ]



        #tens = ["", "", "двадцать"]

        numwords["and"] = (1, 0)
        #print(numwords)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(units_n):
            numwords[word] = (1, idx)
        for idx, word in enumerate(units_1):
            numwords[word] = (1, idx)
        for idx, word in enumerate(hour_1):
            numwords[word] = (1, idx)
        #for idx, word in enumerate(hour_05):
            #numwords[word] = (1, idx*0.5)
        #for idx, word in enumerate(hour_1_5):
            #numwords[word] = (1, idx*1.5)

        #for idx, word in enumerate(tens):
            #numwords[word] = (1, idx * 10)

            #numwords[hour[i]] = (10 ** (i * 3 or 2), 0)
    current = result = 0
    textnum = ' '.join(textnum)
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Незаконное слово: " + word)

        scale, increment = numwords[word]

        print('scale :',scale, 'increment : ',increment )
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    rez_clok_in = (result + current)
    if int(rez_clok_in) < 10:
        rez_clok_in = str(rez_clok_in)
        rez_clok_in = "0" +rez_clok_in
        print('выключение через в ', rez_clok_in, ' часов (от фнкции определения часа)')
        return rez_clok_in
    else:
        rez_clok_in = str(rez_clok_in)
        print('выключение через в ',rez_clok_in, ' часов (от фнкции определения часа)')
        return rez_clok_in

#clock_in('15 часов', numwords={}) # проверка работоспособности функции

# ф-ция определения МИНУТ [в] который необходимо выключить ПК
def minutes_in(textnum=str, numwords={}):
    global rez_minuts_in
    if textnum == '':
        rez_minuts_in = '00'
        return rez_minuts_in
    if not numwords:
        units = [
            "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шеснадцать", "семнадцать", "восемнадцать", "девятнадцать", ]
        units_1 = [
            "ноль", "одну", "две",  ]

        minut_05 = ['ноль', 'пол']

        minut_1_5 = ["ноль", "полтора"]

        units_n = []
        for i in range(0, 40):
            units_n.append(str(i))

        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                "девяносто"]

        numwords["and"] = (1, 0)
        # print(numwords)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)

        for idx, word in enumerate(units_n):
            numwords[word] = (1, idx)

        for idx, word in enumerate(units_1):
            numwords[word] = (1, idx)

        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(minut_05):
            numwords[word] = (1, idx * 0.5)
        for idx, word in enumerate(minut_1_5):
            numwords[word] = (1, idx * 1.5)

            # numwords[hour[i]] = (10 ** (i * 3 or 2), 0)
    current = result = rez = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Незаконное слово: " + word)

        scale, increment = numwords[word]
        # print('scale :',scale, 'increment : ',increment )
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

        rez_minuts_in = result + current

    if rez_minuts_in < 10:
        rez_minuts_in = str(rez_minuts_in)
        rez_minuts_in = '0' + rez_minuts_in
        print('выключение в', rez_minuts_in, ' минуту(ы)(от фнкции определения минут)')
        return rez_minuts_in
    else:
        print('выключение в', rez_minuts_in, ' минуту(ы)(от фнкции определения минут)')
        return str(rez_minuts_in)

#minutes_in('5', numwords={}) # проверка работоспособности функции

# ф-ция определения ЧАСА И МИНУТ [в] который необходимо выключить ПК по типу- 22:10
def sum_time_in(rez_minuts_in, rez_clok_in):
    global time_offsetting_in
    time_offsetting_in = str(rez_clok_in)+":" + str(rez_minuts_in)
    time_offsetting_in = time_offsetting_in.split()
    print('Итогое время до выключения компьтера: ', time_offsetting_in, ' в секундах ')

#ф-ция определения ЧАСОВ [ЧЕРГЕЗ] который необходимо выключить ПК
def text2int_clock(textnum = str, numwords={}):

    #print("textnum : ", textnum)
    global rez_clok
    #textnum = textnum.split()
    # выполняем проверку на наличие в выражении о времни выключения.
    # Если нет данных, значит выключение будет только в минутах

    if textnum == []:
        rez_clok = 0
        return rez_clok
    #print(textnum[-1])
    textnum = textnum.split()
    #print("textnum[-1] = ",textnum[-1])

    if textnum[-1] == "часа":

        # отсекаем словов "часа"
        textnum = ' '.join(textnum[0:len(textnum)-1])
        #print(textnum)


    if not numwords:
        units = [
            "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шеснадцать", "семнадцать", "восемнадцать", "девятнадцать"         ]

        units_n = []
        for i in range(0, 1000):
            units_n.append(str(i))

        units_1 = ["ноль", "одиу", "две"]

        hour_1 = ['ноль', 'час' ]

        hour_05 = ['ноль', 'пол' ]

        hour_1_5 = ["ноль", "полтора" ]



        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

        numwords["and"] = (1, 0)
        #print(numwords)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(units_n):
            numwords[word] = (1, idx)
        for idx, word in enumerate(units_1):
            numwords[word] = (1, idx)
        for idx, word in enumerate(hour_1):
            numwords[word] = (1, idx)
        for idx, word in enumerate(hour_05):
            numwords[word] = (1, idx*0.5)
        for idx, word in enumerate(hour_1_5):
            numwords[word] = (1, idx*1.5)



        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)

            #numwords[hour[i]] = (10 ** (i * 3 or 2), 0)
    current = result =  rez= 0
    textnum = ' '.join(textnum)
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Незаконное слово: " + word)

        scale, increment = numwords[word]
        #print('scale :',scale, 'increment : ',increment )
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0


    #global rez_clok
    rez_clok = (result + current)*60

    print('выключение через',rez_clok, ' минут(от фнкции определения часа)')
    return int(rez_clok)

#ф-ция определения МИНУТ [ЧЕРГЕЗ] который необходимо выключить ПК
def text2int_minutes(textnum=str, numwords={}):
    global rez_minuts
    if textnum == '':
        rez_minuts = 0
        return rez_minuts
    if not numwords:
        units = [
            "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шеснадцать", "семнадцать", "восемнадцать", "девятнадцать", ]
        units_1 = [
            "ноль", "одну", "две",  ]

        minut_05 = ['ноль', 'пол']

        minut_1_5 = ["ноль", "полтора"]

        units_n = []
        for i in range(0, 1000):
            units_n.append(str(i))

        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                "девяносто"]

        numwords["and"] = (1, 0)
        # print(numwords)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)

        for idx, word in enumerate(units_n):
            numwords[word] = (1, idx)

        for idx, word in enumerate(units_1):
            numwords[word] = (1, idx)

        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(minut_05):
            numwords[word] = (1, idx * 0.5)
        for idx, word in enumerate(minut_1_5):
            numwords[word] = (1, idx * 1.5)

            # numwords[hour[i]] = (10 ** (i * 3 or 2), 0)
    current = result = rez = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Незаконное слово: " + word)

        scale, increment = numwords[word]
        # print('scale :',scale, 'increment : ',increment )
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

        rez_minuts = result + current
    #print('выключение через', rez_minuts, ' минут(от фнкции определения минут)')
    return int(rez_minuts)
#ф-ция определения СУММАРНОГО количества минут от ф-ции ЧАСОВ ф-йии МИНУТ [ЧЕРГЕЗ] который необходимо выключить ПК
def sum_time(rez_minuts, rez_clok):

    time_offsetting = (rez_clok + rez_minuts)*60
    print('Итогое время до выключения компьтера: ', time_offsetting)
    time.sleep(time_offsetting)
    os.system('shutdown -s')
# Функция общей логи программы
def clock_1(textnum = str):

    textnum = textnum.split()
    textnum_1 = [] # список , покоторому будет проверяться условие
    # по какой ветке пойти опредления времени либо "в" либо "через"
    through = ['через'] #клчевое слово выбора поределения сколько времени осталось до выключения
    in_v = ['в']

    for idx, text_3 in enumerate(textnum):
        textnum_1.append(str(text_3))
    rezult_th = list(set(through) & set(textnum_1))
    rezult_in_v = list(set(in_v) & set(textnum_1))
    if rezult_th != []:
        for i_i, text_5 in enumerate(textnum):
            if text_5 == 'через':
                u = i_i
                textnum = ' '.join(textnum[u+1:len(textnum)])
                #print('время до выключения: ',textnum)
                textnum = textnum.split()
                #print(textnum)
                hours_2 = ['часа', 'час']
                hours_3 = []
                for ii, hours_1 in enumerate(textnum):
                    hours_3.append(str(hours_1))
                #print('hours_3 = ', hours_3)
                rez_1 =list(set(hours_3) & set(hours_2))
                #print("rez_1 = ", rez_1)

                if rez_1 != [] :
                    for ii_1, hours_4 in enumerate(textnum):
                        if hours_4 == 'час' or hours_4 == 'часа':
                            i_1 = ii_1
                            clocks = ' '.join(textnum[0:i_1+1])
                            #print('солько ЧАСОВ до выключения : ', clocks)
                            clocks =str(clocks)
                            minutes = ' '.join(textnum[i_1+1:len(textnum)-1])
                            #print('солько минут до выключения : ', minutes)
                            text2int_clock(clocks, numwords={})
                            text2int_minutes(minutes, numwords={})
                            sum_time(rez_minuts, rez_clok)

                else:
                    minutes = ' '.join(textnum[0:len(textnum) - 1])
                    #print('солько минут до выключения : ', minutes)
                    text2int_minutes(minutes, numwords={})
                    sum_time(rez_minuts, 0)
    elif rezult_in_v != []:

        for yy, checking_v in enumerate(textnum):
            if checking_v == 'в':
                stop_yy = yy
                textnum = ' '.join(textnum[stop_yy+1: len(textnum)])
                textnum = textnum.split()
                print("textnum : ", textnum)
                hours_2 = ['часа', 'час', 'часов']
                checking_hour = list(set(textnum) & set(hours_2))
                if checking_hour !=[]:
                    for y, checking_h  in enumerate(textnum):
                        if checking_h == 'часа' or checking_h == 'час' or checking_h == 'часов':
                            y_stop = y
                            print("y", y)
                            hour_h = ' '.join(textnum[0:y_stop+1])
                            minut_h = ' '.join(textnum[y_stop+1:len(textnum)-1])
                            clock_in(hour_h, numwords={})
                            minutes_in(minut_h, numwords={})
                            sum_time_in(rez_minuts_in, rez_clok_in)
                            off_computer(time_offsetting_in)
                else:
                    textnum = ''.join(textnum)
                    textnum = str(textnum)
                    clock_and_min(textnum)
                    off_computer(rez_clok_and_min)





while True:
    text = recognizer_search()
    clock_1(text)



#clock_1('выключи компьтер черерз двадцать минут ')
