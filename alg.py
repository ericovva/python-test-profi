#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import re

def parse(input_str):
    '''
    По условию задачи, я полагаю, что цифры, входящие в номер телефона,
    могут быть разделены любыми символами в любом количестве.
    Если я знаю все коды регионов и операторов, то я могу смело парсить строку по ним.
    А именно: итерируюсь по строке, встречаю цифру, сохраняю, иду дальше, встречаю еще пару цифр, конкатинирую первый, если код нашелся, беру следующие 7 симовлов.
              Если код не нашелся беру еще одну следующую цифру, ищу код из трех последних цифр, если не нашел конкатинирую первую цифру, ищу снова. Если не нашел - неверный input, если нашел, то опять таки беру следующие 7 символов.
    Однако, как я понял, задача подразумевает то, что коды я не знаю, и должен сам разбить строку начиная сначала на валидные номера телефонов. Которые валидны только по длине, и в строке долно быть ровно столько цифр, сколько будет необходмо и достаточно чтобы построить n номеров. Единственный критерий по которому я уверенно могу сказать, что это начало номер - +7. Я полагаю, что у меня могут встречаться номера из 7 символов - домашний без кода, из 10 символов - которые начинаются с кода, причем с любого, из 11 символов - тот же, что из 10, только в начале есть +7 или 8. Исходя из этих данных я понял, что строку разюить на номера телефонов, если я встретил, например, 21 цифру, можно, как минимум, 2мя способами 7, 7, 7 или 10, 11. Таким образом, чтобы было возможно прогнать тесты, я принял меру решать неоднозначность таким образом, что алгоритм пытается всегда начинать с поиска коротких номеров. В случае с 21 это будет 7, 7, 7. В случае с 24 это будет 7, 7, 10, а не 10, 7, 7.
    '''
    final = []
    input_digits = [ ]
    was_plus = False
    first_number = False
    for char in input_str:
        if char.isdigit():
            if char == '7' and was_plus:
                final.extend(make_phones(input_digits, first_number))
                input_digits = []
                first_number = True
            input_digits.append(char)
        elif char == '+':
            was_plus = True
            continue
        was_plus = False

    final.extend(make_phones(input_digits, first_number))
    return final

def make_phones(digits, first_number):
    print(digits)
    result = []
    def make_it(tlen, digits):
        phone = ''.join(digits[:tlen])
        if tlen == 7:
            phone = '8495' + phone
        elif tlen == 10:
            phone = phone + '8'
        else:
            phone = re.sub('^7','8',phone)
        result.append(phone)
        digits = digits[tlen:]
        return digits

    terms = [7,10,11]

    if first_number:
        digits = make_it(11, digits)

    path = count_value(len(digits), terms)

    for tlen in path:
        digits = make_it(tlen, digits)
    return result

def count_value(value, terms):
    for term in reversed(terms):
        if term > value:
            terms.remove(term)

    if len(terms) == 0:
        return []
    #init
    path = [0] * (value+1)
    path[0] = 1
    for term in terms:
        path[term] = 1
    
    #make path
    for i in range(min(terms),value):
        if not path[i]:
            continue

        for term in terms:
            if i + term <= value:
                path[i + term] = 1
    
    #find path
    saved = []
    cur = value
    while(cur != 0):
        stop = True
        for term in terms:
            if (path[cur - term] and cur - term >= 0):
                saved.append(term)
                cur -= term
                stop = False

        if (stop):
            break

    return saved
st = "-3440987--+7---9--1----5----294----03---75-------89152940375-------9263394039----"
print(st)
print(parse(st))
