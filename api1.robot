*** Settings ***
Library    get_limit.py
Library    no_limit.py
Library    find_cdek.py
Library    geocoding.py

*** Variables ***
${x}    19

*** Test Cases ***
Limit val
    [Documentation]    Произвольный параметр limit, который входит в допустимый промежуток.
    ...                Ожидается, что количество записей совпадет

    ${limit}=    get_limit     ${3}
    Should Be Equal  ${limit}  ${3}


Limit max
    [Documentation]    Параметр limit больше максимума.
   ...                 Ожидается, что api вернет только максимальное кол-во.

    ${limit}=    get_limit     ${55}
    Should Be Equal  ${limit}  ${50}

Limit default
    [Documentation]    Параметр limit не задан, ожидаемое кол-во записей равно дефолтному.

    ${limit}=    no_limit
    Should Be Equal  ${limit}  ${10}

Find cdek
   [Documentation]    Тест с заранее подготовленными данными (адреса СДЭК с оффициального сайта).
   ...                Ожидается, что на всех адресах находятся пункты выдачи СДЭК.

   ${count}=    find_cdek
   Should Be Equal  ${count}       ${5}

Geocoding
    [Documentation]    Тест с заранее подготовленными данными (адреса) по которым находим координаты.
    ...                По найденым координатам пытаемся найти исходный адрес (обратное геокодирование).
    ...                Если в полученном результате получены: город, улица и номер дома - тест
    ...                пройден. Если хотя бы один из этих параметров не обнаружен - не пройден.
    ...                Проверяем только один результат поиска (параметр limit = 1).
    ...                Спойлер: всё плохо, номер дома он наотрез отказывается выдавать(
    ${count}=    geocoding
    Should Be Equal  ${count}       ${5}
