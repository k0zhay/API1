import requests


search_url = "https://nominatim.openstreetmap.org/search"


def get_limit(limit):
    """
    limit - ожидаемое кол-во адресов
    Функция возвращает фактическое кол-во адресов
    """

    params_limit = {
        "amenity": 'pub',
        "limit": limit,
        "format": 'json'
    }

    response = requests.get(url=search_url,
                            params=params_limit)

    result = response.json()
    if response.ok:
        return len(result)


def no_limit():
    """
    limit - ожидаемое кол-во адресов
    Функция возвращает фактическое кол-во адресов
    """

    params_limit = {
        "amenity": 'pub',
        "format": 'json'
    }

    response = requests.get(url=search_url,
                            params=params_limit)

    result = response.json()
    if response.ok:
        return len(result)


def cdek_addresses():

    """
    Аргумент функции (file_name) - имя файла в кавычках.
    Функция возвращает ответ на запрос в формате json, в котором мы ищем упоминаение "СДЭК".
    Как правило, если не спервого раза, то со второго, он говорит о том, есть ли по данному
    адресу пункт СДЭК (с первого раза иногда выдает просто полный адрес здания).
    """

    count = 0  # Количество адресов из списка, по которым обнаружен пункт СДЭК

    addresses = open('cdek.txt', 'r', encoding='utf-8')  # endcoding нужен, т.к. кириллицу не читает
    addr = addresses.readline()
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

        response = requests.get(url=search_url,
                                params=params_limit)

        result = response.json()
        addr1 = result[0]['display_name']
        addr2 = result[1]['display_name']

        if response.ok and ('СДЭК' in addr1 or 'СДЭК' in addr2):
            count += 1

        addr = addresses.readline()

    return count
