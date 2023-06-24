*** Settings ***
Library    API1.py
Library  API1.py

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

limit cdek
   [Documentation]    Тест с заранее подготовленными данными (адреса СДЭК с оффициального сайта).
   ...                Ожидается, что на всех адресах находятся пункты выдачи СДЭК.
   ${limit}=    cdek_addresses
   Should Be Equal  ${limit}       ${5}
