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
            ask = 'Уважаемый пользователь, задайте команду начиная со слово: выклчи компьютер'
            engin = init_engin()
            sound(engin, ask)
            print('скажите команду')
            audio = recogniser.listen(microfon, 5,5)
        except Exception as ex:
            print('ошибка: ', ex )
            return ''

        data = recogniser.recognize_google(audio, language='ru')
        return data.lower()

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

        minut_1 = ['ноль', 'мину']

        minut_1_5 = ["ноль", "полтора"]

        units_n = []
        for i in range(0, 10):
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

        for idx, word in enumerate(minut_1):
            numwords[word] = (1, idx)

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

def sum_time(rez_minuts, rez_clok):
    global time_offsetting
    time_offsetting = rez_clok + rez_minuts
    print('Итогое время до выключения компьтера: ', time_offsetting)

    return time_offsetting

def clock_1(textnum = str):

    textnum = textnum.split()
    for idx, text_3 in enumerate(textnum):
        if text_3 == 'через':
            i = idx
            textnum = ' '.join(textnum[i+1:len(textnum)])
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


def shutdown_PK(time_off):
    if time_off == 0:
        return ''

    time.sleep(time_off)
    os.system('shutdown -s')




while True:
    text = recognizer_search()
    clock_1(text)
    shutdown_PK(time_offsetting)


#clock_1('выключи компьтер черерз двадцать минут ')
