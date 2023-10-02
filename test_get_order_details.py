import sender_stand_requests


# Андрей Яковлев, 9-поток, Финальный проект. Инженер по тестированию плюс
def get_number_of_track():
    track_number = sender_stand_requests.post_new_order()
    return track_number.json()["track"]


# тест для задания
def test_get_order_details():
    track_number = get_number_of_track()
    get_response = sender_stand_requests.get_order_number(track_number)
    assert get_response.status_code == 200
