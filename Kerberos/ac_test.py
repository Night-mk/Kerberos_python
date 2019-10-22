import pymongo
import json

# mongod --dbpath "G:\python\Kerberos\FZUKerberosweb\FZUKerberos\数据库\test_data"

'''
	数据库添加操作,创建新表操作
	参数说明: 
    folder_permission: "1"表示全部权限都一致，"0"表示有差异
	permission: [1,1,1]表示全部权限
	valid_time: null表示没有时间限制
	# mongod --dbpath "G:\python\Kerberos\FZUKerberosweb\FZUKerberos\数据库\test_data"
'''

def ac_add_database(ido,folder_name,files):
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    # 数据库名称
    mydb = myclient['ACdata']
    # ido_folder 表名称
    folder_table = mydb["ido_folder"]
    '''
        ido_folder数据库添加数据
    '''
    ido_folder_data = {
        "IDc": ido,
        "IDo": ido,
        "file_folder": folder_name,
        "folder_permission": "1"
    }
    # 判断数据是否存在
    if folder_table.count_documents(ido_folder_data) == 0:
        # 数据不存在再插入
        folder_table.insert_one(ido_folder_data)
        # print('none')

    # folder_table.delete_many({"IDo": ido,})
    
    '''
        file_table数据库添加数据
    '''
    file_table =  mydb[folder_name+"_table"]
    idc_file_data = []
    for file in files: 
        data = {
            "IDc": ido,
            "file_name": file,
            "permission": [1,1,1],
            "valid_time": "null"
        }
        idc_file_data.append(data)
    # 插入数据
    file_table.insert_many(idc_file_data)
    # file_table.delete_many({"IDc": ido})
    
    # for x in folder_table.find():
    #     print(x)
    # for x in file_table.find():
    #     print(x)
    # mylist = mydb.list_collection_names()
    # print('table: ',mylist)

    # ido_folder数据库添加数据

# ac_add_database("Bilibili","comic_video1",["file4"])

def db_search():
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    # 数据库名称
    mydb = myclient['ACdata']
    # ido_folder 表名称
    folder_table = mydb["ido_folder"]
    file_table =  mydb["comic_video1_table"]

    print("ido_folder")
    for x in folder_table.find():
        print(x)
    
    print("comic_video1_table")
    for x in file_table.find():
        print(x)

# db_search()


'''
    权限设置操作，设置用户对于文件夹和文件的权限
'''
def ac_set_permission_database(ido,idc,permission,type1,valid_time,folder_name,files):
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    # 数据库名称
    mydb = myclient['ACdata']
    
    '''
        ido_folder设置权限
    '''
    # ido_folder 表名称
    folder_table = mydb["ido_folder"]
    # 设置文件夹权限
    folder_permission = "0"
    if type1=="folder":
        folder_permission="1"
    
    ido_folder_data = {
        "IDc": idc,
        "IDo": ido,
        "file_folder": folder_name,
        "folder_permission": folder_permission
    }
    # 判断数据是否存在
    if folder_table.count_documents({"IDc": idc,"IDo": ido,"file_folder": folder_name}) == 0:
        # 数据不存在再插入
        folder_table.insert_one(ido_folder_data)
    else: 
        # 更新文件夹
        myquery = {"IDc": idc,"IDo": ido,"file_folder": folder_name}
        newvalues = { "$set": { "folder_permission": folder_permission } }
        folder_table.update_one(myquery, newvalues)

    '''
        file_table设置权限
        每个数据分开处理
    '''
    file_table =  mydb[folder_name+"_table"]
    file_permission = [0,0,0]
    if permission=="01": #read
        file_permission = [0,0,1]
    elif permission=="10": # download
        file_permission = [0,1,0]
    elif permission=="11": # read&&download
        file_permission = [0,1,1]
    
    for file in files: 
        data = {
            "IDc": idc,
            "file_name": file,
            "permission": file_permission,
            "valid_time": valid_time
        }
        
        if file_table.count_documents({"IDc": idc,"file_name": file}) == 0:
            # 插入数据
            file_table.insert_one(data)
        else: 
            # 更新权限
            myquery = {"IDc": idc,"file_name": file}
            newvalues = { "$set": { "permission": file_permission, "valid_time": valid_time } }
            file_table.update_one(myquery, newvalues)
    
    print("complete set")
        

# ac_set_permission_database("Bilibili","muke","10","file","2019-09-30","comic_video1",["file3"])
# ac_set_permission_database("Bilibili","guojun","11","folder","2019-09-30","comic_video1",["file1","file2"])


'''
    权限获取操作, 获取特定用户对于特定版权
'''
def ac_get_permission(idc,ido):
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    # 数据库名称
    mydb = myclient['ACdata']
    
    folder_table = mydb["ido_folder"]

    ac_permission = dict()
    ac_permission["IDc"]=idc
    ac_permission["permission"]={}
    # ac_permission = {
    #     "IDc": idc
    # }

    # 根据idc,ido查询idc控制的所有文件夹名称
    controlled_folder = folder_table.find({"IDc": idc,"IDo": ido,})

    for folder in controlled_folder:
        folder_name = folder["file_folder"]
        file_table =  mydb[folder_name+"_table"]
        folder_permission = folder["folder_permission"]
        ac_permission["permission"][folder_name]={}

        #  权限相同的情况
        if folder_permission == "1":
            perm = file_table.find({"IDc": idc}).limit(1)[0]["permission"]
            # print(type(perm))
            perm.append(1)
            # 添加时间检查

            ac_permission["permission"][folder_name][folder_name]=perm
        # 权限不同的情况, 列出对每个文件的权限
        else: 
            files = file_table.find({"IDc": idc})
            ac_permission["permission"][folder_name][folder_name]=[0,0,0,0]
            # 循环添加每个文件的权限
            # 添加时间检查
            for file in files:
                perm = file["permission"]
                ac_permission["permission"][folder_name][file["file_name"]]=perm

    # 将字典转为json
    # ac_permission_json = json.dump(ac_permission)
    print(ac_permission)
    
    return ac_permission

ac_get_permission("muke","Bilibili")
ac_get_permission("guojun","Bilibili")
ac_get_permission("Bilibili","Bilibili")