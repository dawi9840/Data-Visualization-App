import requests

def put_can_status(can_status: str):  
    can_url = "http://20.78.3.60:8080/version/can"  # URL for PUT request

    data = {'status' : can_status}

    # 發送 PUT 請求以發送數據
    response = requests.put(can_url, json=data)

    # 檢查請求是否成功
    if response.status_code == 200:
        print(f"Data posted successfully: {data}")
    else:
        print(f"Failed to post data: {response.status_code}, {response.text}")

if __name__ == '__main__':
    # Input string 0 or 1
    put_can_status('0')
