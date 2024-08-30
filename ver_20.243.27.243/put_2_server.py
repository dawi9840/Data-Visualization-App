import requests

def put_can_status(can_status: str):  
    print('put_can_status()')
    can_url = "http://20.243.27.243:8080/version/can"  # URL for PUT request

    data = {'status' : can_status}

    # 發送 PUT 請求以發送數據
    response = requests.put(can_url, json=data)

    # 檢查請求是否成功
    if response.status_code == 200:
        print(f"Data posted successfully: {data}")
    else:
        print(f"Failed to post data: {response.status_code}, {response.text}")

def put_ota_status(ota_status: str):
    """
    ota status:
    -----------------------------------------------------------------------------------
    web	ota	can	 
    0	0	0	初始狀態
    1	0	0	暴力駕駛發生，由CAN將整組flag 變成100
    1	1	0	OTA發現web flag變成1，OTA修改整組flag 變成110
    1	1	1	CAN發現ota flag變成1，開始進行演算法更新，更新完成後，CAN將整組flag 變成111
    0	0	0	WEB有reset鍵，點擊時WEB將整組flag變成000
    -----------------------------------------------------------------------------------
    """
    ota_url = "http://20.243.27.243:8080/version/hhtd24"  # URL for PUT request

    data = {'status' : ota_status}

    # 發送 PUT 請求以發送數據
    response = requests.put(ota_url, json=data)

    # 檢查請求是否成功
    if response.status_code == 200:
        print(f"Data posted successfully: {data}")
    else:
        print(f"Failed to post data: {response.status_code}, {response.text}")

def reset_put_ota_status(ota_status: str):
    ota_url = "http://20.243.27.243:8080/version/hhtd24"  # URL for PUT request

    data = {'status' : ota_status}

    # 發送 PUT 請求以發送數據
    response = requests.put(ota_url, json=data)

    # 檢查請求是否成功
    if response.status_code == 200:
        print(f"Data posted successfully: {data}")
    else:
        print(f"Failed to post data: {response.status_code}, {response.text}")

if __name__ == '__main__':
    
    put_can_status('1') # Input string 0 or 1.
    put_ota_status('100') # Input ota staus string for test. 000, 100, 110, 111, 000
