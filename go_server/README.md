
# How to use the go server?   

### Start the go server app in background  
```bash        
$: sudo su  
$: cd ~/Data-visualization-app/go_server/kuma  
$: nohup go run main.go &  
```   

### Kill the Go app's PID with the background server, and restart the app.     
#### 1.找到進程 ID (PID)  
```bash     
$: ps aux | grep update_flask.py  
```  

####  2. 終止進程  
一旦知道了 ID，可以使用 kill 來終止該進程  
```bash   
$: kill 12345  
```   

#### 3. Restart go server app  
```bash   
$: nohup go run main.go &  
```     
