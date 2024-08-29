# connect to hhtd24 server
$: ssh ebg@20.78.3.60

# 若是要 sudo 的話
$: sudo su
# 密碼: ebg


# 開 server
$: cd dawi
$: go run main.go


# Turn off server
$: lsof -i :8080
$: kill -9 [8080's PID]





