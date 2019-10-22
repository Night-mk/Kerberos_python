# Kerberos Web 服务

## 一、项目目录结构
```json
    // 整个kerberos web服务项目
    -kerberosWeb
        // 接口主要修改目录
        -kerberosService
            // 处理接口的名称，比如'register'
            api_urls.py 
            // 处理所有的接口，比如'注册服务，修改密码服务'
            api_views.py
            // 其他文件没目前不需要做什么修改，想了解可以看一下Django的应用app部分

        // web服务启动目录, 用于启动web服务器, 也不用管
        -KerberosWeb
        // 测试目录，包含了目前新加的几个加密算法和测试用例

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

```

## 二、项目进度

### 1、已经完成的内容
```json
1. web服务器的基本搭建
2. 3DES, AES, 密钥生成算法（已经和java端调通）
3. 接口示例
4. 可以用client简单模拟请求内容，以及可以得到服务器的返回结构
```

### 2、需要你补充的内容
```json
1. 所有的接口实现（接口参考《Kerberos API》这个文档，主要是把你之前写的东西当做库移植过来，并且要返回json格式的数据）
2. 数据库构建（注册用的数据库【保存用户信息】，访问控制器的数据库【保存访问控制矩阵AC】）
3. 测试所有接口
4. 访问控制矩阵(AC)的更新，需要和区块链沟通，更新策略需要处理不少代码估计
```

## 三、web服务启动测试细节

### 1、启动服务器
```json
// 使用django框架，在项目根目录下执行下面的代码，可以构建一个127.0.0.1:8080的服务器
python manage.py runserver 127.0.0.1:8080
```

### 2、客户端访问地址
```json
// 本地运行客户端只需要访问下面的ip，具体看一下client.py
ip:8080/kerberosService/api
```

### 3、局域网配置
```json
    参考链接：https://blog.csdn.net/yangmingqian/article/details/54691598
```

### 4、数据库启动
```json
    // 安装好mongodb, 执行下面代码
    mongod --dbpath [DATABASE_PATH]
```

## 四、补充函数
```json
    // 接口在api_views.py
    // 文件添加接口
    ac_add()
    // all.py 数据库处理
    ac_add_database()

    // 权限设置接口
    ac_set_permission()
    // all.py 数据库处理
    ac_set_permission_database()

    // all.py 获取AC函数
    ac_get_permission()

```

数据库mongoengine操作教程：
https://www.2cto.com/database/201710/689987.html

#管理员数据库
connect('admindata', host='localhost', port=27017)

#访问控制矩阵
connect('IDO1', host='localhost', port=27017)
可能需要重新创建

#用户信息数据库
connect('IDdata', host='localhost', port=27017)

```
//接口用到的所有函数都封装在文件夹 /apifunc 的 all.py 中 
```

