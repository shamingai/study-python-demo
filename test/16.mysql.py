# -*- coding: utf-8 -*- 
# @Time : 2020/7/18 6:15 AM 
# @Author : zhaotong 
# @File : 16.mysql.py

import pymysql
import sshtunnel
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.199.162', port=22, username='root', password='buzhidao')

# 执行命令
# stdin, stdout, stderr = ssh.exec_command('ls')
# # # 获取命令结果
# result = stdout.read()

# # 关闭连接
# ssh.close()
print(1)

with sshtunnel.SSHTunnelForwarder(
        ('192.168.199.162', 22),
        ssh_username='root',
        ssh_password='buzhidao',
        remote_bind_address=('192.168.199.162', 3306),
        local_bind_address=('127.0.0.1', 13306)
) as tunnel:
    conn = pymysql.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        port=13306,
        database='house',
    )
    cursor = conn.cursor()
    query = "select version();"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)

# 关闭连接
ssh.close()