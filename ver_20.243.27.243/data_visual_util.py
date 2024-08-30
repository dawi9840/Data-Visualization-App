import json
import pytz
from datetime import datetime
from typing import List, Dict, Tuple
from client import get_rest_data


def get_utc_2_taipei_time_zone(time_formate: str) -> str:
    """
    Converts the current UTC time to Taipei time zone and formats it.

    Args:
        time_format (str): A format string for datetime, e.g., '%Y-%m-%d %H:%M' or '%Y-%m-%d %H:%M:%S'.

    Returns:
        str: The formatted date and time string in Taipei time zone.
    """
    utc_time = datetime.now(pytz.utc)                               # 設定 UTC 時區
    taipei_time = utc_time.astimezone(pytz.timezone('Asia/Taipei')) # 將 UTC 時間轉換為 Asia/Taipei 時區
    return taipei_time.strftime(time_formate)                       


def extract_speed_and_power(data: Dict[str, str]) -> Tuple[List[int], List[int]]:
    """
    Extracts the 'speed' and 'power' values from the given data dictionary.

    Args:
        data (Dict[str, str]): A dictionary containing at least 'speed' and 'power' keys
                               with string representations of lists.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing two lists: 'speed' and 'power'.
                                     Returns (None, None) if an error occurs.
    """
    try:
        if not data['speed'] or not data['power']:
            raise ValueError("Speed or power data is missing or empty")
        
        speed = json.loads(data['speed'].replace("'", '"'))
        power = json.loads(data['power'].replace("'", '"'))
        return speed, power
    except KeyError as e:
        print(f"KeyError: {e} not found in the data")
        return None, None
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e} while parsing the lists")
        return None, None


def test_extract_speed_and_power():
    user_url:str = "http://20.243.27.243:8080/users"
    user_data: List[Dict[str, int]] = get_rest_data(user_url)

    for i in range(0, len(user_data)): 
        print(f"Index[{i}]:\n{user_data[i]}\n")

        speed, power = extract_speed_and_power(user_data[i])
        print(f"speed[{i}]: {speed}\n")
        print(f"power[{i}]: {power}\n")


def test_get_utc_2_taipei_time_zone():
    # '%Y-%m-%d %H:%M' or '%Y-%m-%d %H:%M:%S'
    time_formate = '%Y-%m-%d %H:%M:%S'
    current_time: str = get_utc_2_taipei_time_zone(time_formate)
    print(f'current_time: {current_time}')


if __name__ == '__main__':
    test_extract_speed_and_power()
    test_get_utc_2_taipei_time_zone()
