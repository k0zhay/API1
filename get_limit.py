import requests
import links


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

    response = requests.get(url=links.search_url,
                            params=params_limit)

    result = response.json()
    if response.ok:
        return len(result)
