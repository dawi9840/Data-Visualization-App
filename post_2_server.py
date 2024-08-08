import random
import requests
from typing import List, Dict
import json


def post_data(url: str, data: Dict[str, int]):
    # 發送 POST 請求以發送數據
    response = requests.post(url, json=data)
    # 檢查請求是否成功
    if response.status_code == 200:
        print(f"Data posted successfully:\n {data}")
    else:
        print(f"Failed to post data: {response.status_code}, {response.text}")

def post_continuous_user(user: List[str], time: List[int]):
    url = 'http://20.78.3.60:8080/user'
    # 確保 power 和 time 的長度相同
    for i in range(min(len(user), len(time))):
        post_data(url, {"speed": user[i], "power": time[i]})

def post_continuous_speed(speed: List[str], time: List[int]):
    url = 'http://20.78.3.60:8080/speed'
    # 確保 speed 和 time 的長度相同
    for i in range(min(len(speed), len(time))):
        post_data(url, {"speed": speed[i], "time": time[i]})

def post_continuous_power(power: List[str], time: List[int]):
    url = 'http://20.78.3.60:8080/power'
    # 確保 power 和 time 的長度相同
    for i in range(min(len(power), len(time))):
        post_data(url, {"power": power[i], "time": time[i]})

def test_dawi_generate_data():
    time: List[int] = generate_num_y(150)

    # post speed continuous example
    speed: List[int] = generate_random(len(time), 360)  # 生成與 time 長度相同的 0~370 亂數列表
    post_continuous_speed(speed, time)

    # post speed continuous example
    power: List[int] = generate_random(len(time), 110)  # 生成與 time 長度相同的 0~110 亂數列表
    post_continuous_power(power, time)

    # print("speed:", speed, " , len: ", len(speed))
    # print("time:", time, " , len: ", len(time)) 
    print("power:", power, " , len: ", len(power))

def post_a_user_data_2_server():
    user_url = 'http://20.78.3.60:8080/user'

    time: List[int] = generate_num_y(50)
    # print('time:', time, '\n')
    
    speed_int: List[int] = generate_random(len(time), 360)
    # print('speed_int:', speed_int, " len(speed_int): ", len(speed_int), '\n')
    
    power_int: List[int] = generate_random(len(time), 100)
    # print('power_int:', power_int, " len(power_int): ", len(power_int),  '\n')

    speed_str: List[str] = convert_list_to_str(speed_int)
    print('speed_str:', speed_str, " \nlen(speed_str): ", len(speed_str), ", len(speed_int): ", len(speed_int), '\n')
    
    power_str: List[str] = convert_list_to_str(power_int)
    print('power_str:', power_str, " \nlen(power_str): ", len(power_str), ", len(power_int): ", len(power_int),'\n')

    post_data(user_url, {"speed": speed_str, "power_str": power_str})

# Util
def generate_num_y(input: int) -> List[int]:
    result = []
    for i in range(0, input, 1):
        result.append(i)
    return result

def generate_random(length: int, max_value: int) -> List[int]:
    result = []
    for _ in range(length):
        result.append(random.randint(0, max_value))
    return result

def convert_list_to_str(input_list: List[int]) -> str:
    return json.dumps(input_list)

if __name__ == '__main__':

    post_a_user_data_2_server()
