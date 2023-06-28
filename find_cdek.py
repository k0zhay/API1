import requests
import links


def find_cdek():
    """
    На входе файл с перечисленными адресами пунктов СДЭК.
    Функция возвращает ответ на запрос в формате json, в котором мы ищем упоминаение "СДЭК".
    Как правило, если не спервого раза, то со второго, он говорит о том, есть ли по данному
    адресу пункт СДЭК (с первого раза иногда выдает просто полный адрес здания).
    """

    count = 0  # Количество адресов из списка, по которым обнаружен пункт СДЭК

    addresses_list = open('cdek.txt', 'r', encoding='utf-8')  # endcoding нужен, т.к. кириллицу не читает
    addr = addresses_list.readline()
    while addr:
        addr = str(addr).split(',')

        params_limit = {
            "city": addr[0],
            "street": addr[1],
            "house_number": addr[2],
            "limit": 2,
            "amenity": 'post_office',
            "format": 'json'
        }

        response = requests.get(url=links.search_url,
                                params=params_limit)

        result = response.json()
        addr1 = result[0]['display_name']
        addr2 = result[1]['display_name']

        if response.ok and ('СДЭК' in addr1 or 'СДЭК' in addr2):
            count += 1

        addr = addresses_list.readline()  # Переходим к следующему адресу

    return count
