# This is MySQL backup database files.   

## 登錄到 MySQL，系統會提示你輸入 root 用戶的密碼。   
$: sudo mysql -u root -p   
f********3    

## 查詢用戶，進入 MySQL 命令行後，使用以下 SQL 查詢來列出所有用戶    
$: SELECT User, Host FROM mysql.user; 
![image](https://github.com/user-attachments/assets/6d3fdf9a-db7f-409e-ad9d-aedfe4af627c)      
5 rows in set (0.00 sec)    

## 查詢數據庫名稱    
$: SHOW DATABASES;    
![image](https://github.com/user-attachments/assets/9f5d8254-f603-4e4e-a254-5671c4ddcf28)   
7 rows in set (0.01 sec)  

## 退出 MySQL  
$: EXIT;  

## mysqldump 是一個外部命令，不能直接在 MySQL 交互式命令行界面中執行。  
## 在系統的終端機中執行 mysqldump 命令，而不是在 MySQL 的命令行中。  

## 備份 其中的一個 MySQL 數據庫（例如 dawidb）  
$: mysqldump -u root -p dawidb > /path/to/backup_dawidb.sql  
f********3   

## 恢復數據庫   
## 如果要在新的 MySQL 環境中恢復數據庫，可使用：   

## 1.創建數據庫（如果尚未創建）   
$: sudo mysql -u root -p   
$: CREATE DATABASE dawidb;  
$: EXIT;  

## 2.恢復數據庫   
$: mysql -u root -p dawidb < /path/to/backup_dawidb.sql 
 
