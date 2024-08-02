# Data-Visualization-App 
Flask Application for Data Visualization with Dynamic Plot Updates.

## 前置   
前置1: 雲端 server 能連上
 ```bash
# Connect to the hhtd24 server
$: ssh ebg@20.78.3.60

# Start the server
$: cd kuma
$: go run main.go
```
![image](https://github.com/user-attachments/assets/56aab720-85da-4158-baf0-d1aec7c2828c) 

前置2: Code env setting (local env)   
```bash   
$: conda create --name hhtd24 python=3.8      
$: conda activate hhtd24   
$: pip install requests matplotlib flask pyOpenSSL flask-cors    
```
![image](https://github.com/user-attachments/assets/d4af6de3-8d4e-4888-9255-bc9f1ab0bbdf)   


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

## Simple Web server:Ngrok  
Step1. 從[ngrok官網](https://dashboard.ngrok.com/get-started/your-authtoken)下載 ngrok 檔案 (這邊先做好，直接在./web_server folder 解壓縮就好)。

Step2.To get token
![image](https://github.com/user-attachments/assets/64a74d9a-63e9-4175-b705-491e9eb1b5e2)

Step3.Open terminal to config token setting
```bash
# Config token setting
$: ngrok authtoken <YOUR_AUTH_TOKEN>

# Finally, to start the server
$: ngrok http 5000    
```
![image](https://github.com/user-attachments/assets/683bdf4a-81b0-42c6-ab6a-2d8e7c7da1a1)    
![image](https://github.com/user-attachments/assets/54a91a43-37fc-42a1-bc1b-1430313ed93d)    


