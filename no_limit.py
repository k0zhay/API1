import requests
import links


def no_limit():
    """
    limit - ожидаемое кол-во адресов
    Функция возвращает фактическое кол-во адресов
    """

    params_limit = {
        "amenity": 'pub',
        "format": 'json'
    }

    response = requests.get(url=links.search_url,
                            params=params_limit)

    result = response.json()
    if response.ok:
        return len(result)
