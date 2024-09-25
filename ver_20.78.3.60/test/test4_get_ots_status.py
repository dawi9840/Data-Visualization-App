import os
import sys
# 將上一層資料夾的路徑加入 sys.path，這樣 Python 就能找到並匯入上一層資料夾中的 BB.py 檔案中的函數。
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from client import get_ota_status

from typing import List, Dict
from datetime import datetime

def test_get_ots_status():
    ota_status_url = "http://20.78.3.60:8080/version/status?name=hhtd24"
    ota_status = get_ota_status(ota_status_url)['status']
    print('Get ota ststus: ', ota_status)

    if(ota_status=='000' or ota_status=='000' or ota_status=='011'):
        web_status = 'Last update: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("web_status: ", web_status)

    
    if(ota_status=='100' or ota_status=='110' or ota_status=='111'):
        web_status = "New update is ready"
        print("web_status: ", web_status)


if __name__ == '__main__':

    test_get_ots_status()

