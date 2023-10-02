import requests
import configuration
import data

# Создание нового заказа
def post_new_order():
    return requests.post(configuration.URL + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)

# Получение номера заказа
def get_order_number(track_number):
    return requests.get(configuration.URL + configuration.GET_ORDER_PATH,
                        params={"t": track_number})
