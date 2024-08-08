import requests
from typing import List, Dict
from datetime import datetime

def test_GET_display(url:str, url_type:str):
    try:
        print("GET data type: ", url_type)

        request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 記錄並格式化當前的時間
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print("Received data:", data, "\n")
            print(f'data length: {len(data)}')
            print(f"Request time: {request_time}")
            print('-----'*10)
        else:
            print("Failed to retrieve data:", response.status_code, "\n")
    except requests.exceptions.RequestException as e:
        print("Error during request:", e)


def get_rest_data(url: str) -> List[Dict[str, int]]:
    # return the GET data
    print("data type: ", url)
    response = requests.get(url)

    if response.status_code == 200:
        # print("Received data: ", response.json(), "\n")
        return response.json()
    else:
        print("Failed to retrieve data:", response.status_code, "\n")


def get_ota_status(url: str) -> List[Dict[str, str]]:
    print("data type: ", url)
    response = requests.get(url)

    if response.status_code == 200:
        # print("Received data: ", response.json(), "\n")
        return response.json()
    else:
        print("Failed to retrieve data:", response.status_code, "\n")


if __name__ == '__main__':
    user_url = "http://20.78.3.60:8080/users"
    data_url = "http://20.78.3.60:8080/data"
    speed_url = "http://20.78.3.60:8080/speed"
    power_url = "http://20.78.3.60:8080/power"

    can_status_url = "http://20.78.3.60:8080/version/status?name=can"
    ota_status_url = "http://20.78.3.60:8080/version/status?name=hhtd24"

    # test_GET_display(data_url, 'data')
    # test_GET_display(speed_url, 'speed')
    # test_GET_display(power_url, 'power')
    test_GET_display(user_url, 'users')
    test_GET_display(can_status_url, 'status')
    test_GET_display(ota_status_url, 'status')
