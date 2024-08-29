package main

import (
    "database/sql"
    "log"
    "net/http"

    "github.com/gin-gonic/gin"
    _ "github.com/go-sql-driver/mysql"
)


type User struct {
    ID    int       `json:"id"`
    Speed string    `json:"speed"`
    Power string    `json:"power"`
}

type Version struct {
    ID     int       `json:"id"`
    Name   string    `json:"name"`
    Status string    `json:"status"`
}

var db *sql.DB
var db2 *sql.DB

func main() {

    // 连接到MySQL数据库
    var err error
    db, err = sql.Open("mysql", "root:foxconn123@tcp(localhost:3306)/userdb")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    // 测试数据库连接
    err = db.Ping()
    if err != nil {
        log.Fatal(err)
    }

    // 连接到MySQL数据库
    var err2 error
    db2, err2 = sql.Open("mysql", "root:foxconn123@tcp(localhost:3306)/versiondb")
    if err2 != nil {
        log.Fatal(err2)
    }
    defer db2.Close()

    // 测试数据库连接
    err2 = db2.Ping()
    if err2 != nil {
        log.Fatal(err2)
    }



    // 使用默认中间件创建一个Gin路由器
    r := gin.Default()

    // 定义一个简单的GET路由
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{
            "message": "pong",
        })
    })

    // GET请求处理器，获取所有用户信息
    r.GET("/users", func(c *gin.Context) {
        // 查询数据库中所有用户信息
        rows, err := db.Query("SELECT id, speed, power FROM users ORDER BY id DESC LIMIT 10")
        if err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to query database"})
            return
        }
        defer rows.Close()

        // 构建用户列表
        var users []User
        for rows.Next() {
            var user User
            if err := rows.Scan(&user.ID, &user.Speed, &user.Power); err != nil {
                c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to scan rows"})
                return
            }
            users = append(users, user)
        }

        // 检查是否有错误检索行时
        if err := rows.Err(); err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to iterate over rows"})
            return
        }

        // 返回用户列表
        c.JSON(http.StatusOK, users)
    })

    // POST请求处理器，用于接收用户信息并存储到数据库
    r.POST("/user", func(c *gin.Context) {
        // 绑定POST请求的JSON数据到结构体
        var user User
        if err := c.BindJSON(&user); err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }

        // 将用户信息插入数据库
        insertQuery := "INSERT INTO users (speed, power) VALUES (?, ?)"
        _, err := db.Exec(insertQuery, user.Speed, user.Power)
        if err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to insert data into database"})
            return
        }

        // 返回成功响应
        c.JSON(http.StatusOK, gin.H{"message": "User data received and stored successfully"})
    })


    // POST请求处理器，用于批量接收用户信息并存储到数据库
    r.POST("/users", func(c *gin.Context) {
        var users []User
        if err := c.BindJSON(&users); err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }

        // 开始一个事务
        tx, err := db.Begin()
        if err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to begin transaction"})
            return
        }

        // 准备插入查询
        stmt, err := tx.Prepare("INSERT INTO users (speed, power) VALUES (?, ?)")
        if err != nil {
            tx.Rollback()
            c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to prepare statement"})
            return
        }
        defer stmt.Close()

        // 插入每个用户
        for _, user := range users {
            _, err = stmt.Exec(user.Speed, user.Power)
            if err != nil {
                tx.Rollback()
                c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to insert data"})
                return
            }
        }

        // 提交事务
        err = tx.Commit()
        if err != nil {
            tx.Rollback()
            c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to commit transaction"})
            return
        }

        // 返回成功响应
        c.JSON(http.StatusOK, gin.H{"message": "User data received and stored successfully"})
    })












        // 获取status
	r.GET("/version/status", func(c *gin.Context) {
		name := c.Query("name")
		var status string

		query := "SELECT status FROM versions WHERE name = ?"
		err := db2.QueryRow(query, name).Scan(&status)
		if err != nil {
			if err == sql.ErrNoRows {
				c.JSON(http.StatusNotFound, gin.H{"error": "Version not found"})
			} else {
				c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to query database"})
			}
			return
		}

		c.JSON(http.StatusOK, gin.H{"status": status})
	})



    // 创建一个新版本
	r.POST("/version", func(c *gin.Context) {
		var version Version
		if err := c.ShouldBindJSON(&version); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		query := "INSERT INTO versions (name, status) VALUES (?, ?)"
		_, err := db2.Exec(query, version.Name, version.Status)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to insert data"})
			return
		}

		c.JSON(http.StatusOK, gin.H{"message": "Version added successfully"})
	})

	// 修改现有版本
	r.PUT("/version/:name", func(c *gin.Context) {
		name := c.Param("name")
		var version Version
		if err := c.ShouldBindJSON(&version); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		query := "UPDATE versions SET status = ? WHERE name = ?"
		_, err := db2.Exec(query, version.Status, name)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to update data"})
			return
		}

		c.JSON(http.StatusOK, gin.H{"message": "Version updated successfully"})
	})


    // 启动服务器
    r.Run(":8080") // 默认监听并服务于 0.0.0.0:8080
}

