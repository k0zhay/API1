import requests
import links


def geocoding():
    """
    На входе файл с перечисленными адресами пунктов СДЭК.
    Сначала проводим прямое геокодирование (ПГ) и получаем координаты, соответствующие указанному
    адресу. После проводим обратное геокодирование (ОГ) и проверяем, получим ли мы тот же адрес при
    поиске по координатам. В итоге считаем, сколько получено совпадений.
    Спойлер: всё очень плохо(
    В принципе, можно даже ввести балльную систему: если все параметры совпали - 3 балла,
    улица и город - 2 балла, только город - 1 балл "за старание".
    """

    # Количество адресов, для которых при обратном геокодировании получили правильный адрес:
    count = 0

    addresses_list = open('cdek.txt', 'r', encoding='utf-8')  # endcoding нужен, т.к. кириллицу не читает
    addr = addresses_list.readline()
    while addr:
        addr = str(addr).split(',')

        # Параметры для поиска прямым геокодированием (direct geocoding)
        dir_geo_params = {
            "city": addr[0],
            "street": addr[1],
            "house_number": addr[2],
            "limit": 1,
            "format": 'json'
        }

        dir_response = requests.get(url=links.search_url, params=dir_geo_params)

        dir_geocoding = dir_response.json()  # Полный результат при поиске по адресу

        if dir_response.ok:  # Если запрос успешен,переходим к ОГ

            latitude = dir_geocoding[0]['lat']  # Полученная после ПГ широта
            longitude = dir_geocoding[0]['lon']  # Полученная после ПГ долгота

            # Параметры для поиска по полученным координатам (reverse geocoding)
            rev_geo_params = {
                'lat': latitude,
                'lon': longitude,
                "limit": 1,
                "format": 'json'
            }

            rev_response = requests.get(url=links.reverse_url, params=rev_geo_params)

            rev_geocoding = rev_response.json()  # Полный результат при поиске по ОГ
            rev_address = rev_geocoding['display_name']  # Полученный адрес по ОГ

            # Дом и улица объединены, чтобы мы случайно не "нашли" номер дома в индексе
            if rev_response.ok and addr[0] and rev_address and \
                    (addr[2] + ', ' + addr[2]) in rev_address:
                count += 1

            addr = addresses_list.readline()  # Переходим к следующему адресу

    print(count)
    return count


geocoding()