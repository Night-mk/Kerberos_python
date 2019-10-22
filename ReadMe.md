# Kerberos 服务

## 一、项目目录结构
```json
    // kerberos 功能函数目录
    -apifunc
        // kerberos接口底层功能实现
        socket.py
    
    // kerberos数据库目录
    -database
        // mongodb可执行文件目录
        -mongodb
        // mongodb数据库文件存储目录
        -test_data
    
    // kerberos web服务项目目录
    -kerberosWeb
        // 接口编辑目录
        -kerberosService
            // 处理接口的名称，比如'register'
            api_urls.py 
            // 处理所有的接口，比如'注册服务，修改密码服务'
            api_views.py
            // 其他文件没目前不需要做什么修改，想了解可以参考Django的应用app部分

        // web服务启动目录, 用于启动web服务器，用于配置服务器的网络服务
        -KerberosWeb

        // 接口测试目录，包含多个加密算法和测试用例
        -test
            // 3DES加解密算法(已经和云服务调好了)
            3DES.py
            // AES加解密算法
            AES.py
            // 密钥生成算法，PBKDF2算法，具体的看《密钥生成算法&加密算法（AES，3DES）》
            key_gen.py
            // 客户端模拟测试函数
            client.py 
        
        -record
            // 3DES,AES,密钥生成算法文档
            密钥生成算法&加密算法（AES，3DES）.docx
            // API文档
            Kerberos API.html
    
    // kerberos底层功能实现模块目录（分离版）
    -Kerveros

    // Kerberos服务socket测试目录
    -test

    // kerberos 服务简介
    ReadMe.md

```

## 二、Kerberos web服务启动测试

### 1、启动服务器
```json
// 使用django框架，在项目根目录下执行下面的代码，可以构建一个127.0.0.1:8080的服务器
python manage.py runserver 127.0.0.1:8080
```

### 2、客户端访问地址
```json
// 本地运行客户端只需要访问下面的ip，简单的访问示例可以参考client.py
ip:8080/kerberosService/api
```

### 3、局域网配置
```json
// 对项目目录/KerberosWeb/KerberosWeb/settings.py文件中的ALLOWED_HOSTS参数进行设置，例如
ALLOWED_HOSTS = ['192.168.1.106']
```

### 4、数据库启动
```json
// 安装好mongodb, 执行下面代码
mongod --dbpath [DATABASE_PATH]
```

## 三、Kerberos web服务mongoDB数据库表说明
```json
// 用户身份表
IDdata
// 管理员身份表
admindata
// 访问控制矩阵表
ACdata
```

