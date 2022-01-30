def bigger_price(limit: int, data: list) -> list:
    """
        Дана таблица всех доступных продуктов на складе. Данные представлены в виде
        списка словарей (a list of dicts). Найти ТОП самых дорогих товаров.
        Входные данные: Число и список словарей (int and list of dicts). Каждый
        словарь имеет 2 ключа "name" и "price".
        Выходные данные: Такой же как, и второй аргумент.
    """
    lst = []
    data = sorted(data, key=lambda i: i['price'], reverse=True)
    for index in range(limit):
        lst.append(data[index])
    return lst


if __name__ == '__main__':
    print(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"
    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"
