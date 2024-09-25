# Data-Visualization-App 
Flask Application for Data Visualization with Dynamic Plot Updates.

## Overview (orange area part)   
![web_data_visual_overview_github](https://github.com/user-attachments/assets/11cf50c2-f0fa-40c4-bb02-92205fffe3fb)    


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
![image](https://github.com/user-attachments/assets/26edf9a4-0f42-4fbb-8bef-d6a56a6a4850)
```bash   
$: conda create --name hhtd24 python=3.8      
$: conda activate hhtd24
```
Install relate modules  
```bash    
$: pip install requests matplotlib flask pytz     
```
 


## File Description  
client.py: 執行測試接收GET資料。    
```bash       
$: python client.py      
```

post_2_server.py: 運行可以直接PUT一筆資料至雲端。    
```bash       
$: pyhton post_2_server.py          
```

update_flask.py:運行時，可以依造 terminal 上顯示的網址，link 到 browser 上看 local 端視覺化結果。       
```bash           
$: python update_flask.py      
```    
![image](https://github.com/user-attachments/assets/da1ff787-d239-4058-832a-33e35e10ba48) 
![image](https://github.com/user-attachments/assets/420200c3-5a21-492a-9118-755cec7b9dd4)  

## Simple Web server:Ngrok  
Step1. 從 [ngrok官網](https://dashboard.ngrok.com/get-started/your-authtoken) 下載壓縮檔案 (這邊直接在./web_server folder 解壓縮就好)。
```bash 
$: cd ./web_server
$: unzip ./ngrok-v3-stable-windows-amd64.zip -d ./   
```

Step2.To get token
![image](https://github.com/user-attachments/assets/64a74d9a-63e9-4175-b705-491e9eb1b5e2)

Step3.Open terminal to config token setting
```bash
# Config token setting
$: ngrok authtoken <YOUR_AUTH_TOKEN>
```     

Step4.Start the server to check the result.    
```bash
# Finally, to start the server
$: ngrok http 5000    
```
![image](https://github.com/user-attachments/assets/683bdf4a-81b0-42c6-ab6a-2d8e7c7da1a1)    
![image](https://github.com/user-attachments/assets/54a91a43-37fc-42a1-bc1b-1430313ed93d)    


