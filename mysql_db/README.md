# This is MySQL backup database files.   

## 登錄到 MySQL，系統會提示你輸入 root 用戶的密碼。 
```bash       
$: sudo mysql -u root -p   
f********3       
```
  
## 查詢用戶，進入 MySQL 命令行後，使用以下 SQL 查詢來列出所有用戶  
```bash       
$: SELECT User, Host FROM mysql.user;
+------------------+-----------+  
| User             | Host      |  
+------------------+-----------+  
| debian-sys-maint | localhost |  
| mysql.infoschema | localhost |  
| mysql.session    | localhost |  
| mysql.sys        | localhost |  
| root             | localhost |  
+------------------+-----------+  
5 rows in set (0.00 sec)     
```

## 查詢數據庫名稱    
```bash       
$: SHOW DATABASES;
+--------------------+  
| Database           |  
+--------------------+  
| dawidb             |  
| information_schema |  
| mysql              |  
| performance_schema |  
| sys                |  
| userdb             |  
| versiondb          |  
+--------------------+  
7 rows in set (0.01 sec)      
```


## 退出 MySQL 
```bash
$: EXIT;  
```

Tips: mysqldump 是一個外部命令，不能直接在 MySQL 交互式命令行界面中執行。在系統的終端機中執行 mysqldump 命令，而不是在 MySQL 的命令行中。  


## 備份 其中的一個 MySQL 數據庫（例如 dawidb）  
```bash   
$: mysqldump -u root -p dawidb > /path/to/backup_dawidb.sql  
f********3   
```

## 恢復數據庫   

如果要在新的 MySQL 環境中恢復數據庫，可使用：   
## 1.創建數據庫（如果尚未創建）  
```bash  
$: sudo mysql -u root -p   
$: CREATE DATABASE dawidb;  
$: EXIT;  
```   
## 2.恢復數據庫   
```bash  
$: mysql -u root -p dawidb < /path/to/backup_dawidb.sql 
 ```   
