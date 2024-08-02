# Data-Visualization-App 
Flask Application for Data Visualization with Dynamic Plot Updates.

## 前置   
前置1: 雲端 server 能連上
 ```bash
# Connect to hhtd24 server
$: ssh ebg@20.78.3.60

# Start the server
$: cd kuma
$: go run main.go
```
![image](https://github.com/user-attachments/assets/56aab720-85da-4158-baf0-d1aec7c2828c) 

前置2: Code Env (local端環境)   
```bash   
$: conda create --name hhtd24 python=3.8      
$: conda activate hhtd24   
$: pip install requests matplotlib flask pyOpenSSL flask-cors    
```


## File Description  
```bash   
client.py: 執行測試接收GET資料。    
$: python client.py      

post_2_server.py: 運行可以直接PUT一筆資料至雲端。    
$: pyhton post_2_server.py       

update_flask.py:運行時，可以依造 terminal 上顯示的網址，link 到 browser 上看視覺化結果。      
$: python update_flask.py      
```
![image](https://github.com/user-attachments/assets/da1ff787-d239-4058-832a-33e35e10ba48) 
![image](https://github.com/user-attachments/assets/420200c3-5a21-492a-9118-755cec7b9dd4) 

