package main

import (
    "database/sql"
    "log"
    "net/http"

    "github.com/gin-gonic/gin"
    _ "github.com/go-sql-driver/mysql"
)

type User struct {
    ID   int    `json:"id"`
    Name string `json:"name"`
    Age  int    `json:"age"`
}

type DataPoint struct {
    Time  int `json:"time"`
    Speed int `json:"speed"`
}

var db *sql.DB
var dataPoints []DataPoint

func main() {
    // 連接到MySQL資料庫
    var err error
    db, err = sql.Open("mysql", "root:foxconn123@tcp(localhost:3306)/userdb")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    // 測試資料庫連接
    err = db.Ping()
    if err != nil {
        log.Fatal(err)
    }

    // 使用預設中間件建立一個Gin路由器
    r := gin.Default()

    // 定義一個簡單的GET路由
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{
            "message": "pong",
        })
    })

    // GET請求處理器，獲取所有user message
    r.GET("/users", func(c *gin.Context) {
        // 查詢資料庫中所有使用者信息
        rows, err := db.Query("SELECT id, name, age FROM users")
        if err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to query database"})
            return
        }
        defer rows.Close()

        // 建立使用者列表
        var users []User
        for rows.Next() {
            var user User
            if err := rows.Scan(&user.ID, &user.Name, &user.Age); err != nil {
                c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to scan rows"})
                return
            }
            users = append(users, user)
        }

        // 檢查是否有錯誤檢索行時
        if err := rows.Err(); err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to iterate over rows"})
            return
        }

        // 返回使用者列表
        c.JSON(http.StatusOK, users)
    })

    // POST請求處理器，用於接收用戶資訊並儲存到資料庫
    r.POST("/user", func(c *gin.Context) {
        // 綁定POST請求的JSON資料到結構體
        var user User
        if err := c.BindJSON(&user); err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }

        // 將使用者資訊插入資料庫
        insertQuery := "INSERT INTO users (name, age) VALUES (?, ?)"
        _, err := db.Exec(insertQuery, user.Name, user.Age)
        if err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to insert data into database"})
            return
        }

        // Return successful response
        c.JSON(http.StatusOK, gin.H{"message": "User data received and stored successfully"})
    })

    // POST請求處理器，用於接收時間和速度數據
    r.POST("/data", func(c *gin.Context) {
        var data DataPoint
        if err := c.BindJSON(&data); err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }
        dataPoints = append(dataPoints, data)
        c.JSON(http.StatusOK, gin.H{"message": "Data received successfully"})
    })

    // GET請求處理器，返回所有時間和速度數據
    r.GET("/data", func(c *gin.Context) {
        c.JSON(http.StatusOK, dataPoints)
    })

    // Start the server
    r.Run(":8080") // By default, it listens and serves at 0.0.0.0:8080
}

