import requests,json
param1={"content":"叫我拿了什么叫冯副经理了副书记"}
aa = requests.post("http://127.0.0.1:5000/test11",data=param1)
print(aa.text)

# b = requests.get('http://127.0.0.1:5000/test?content=叫我拿了什么叫冯副经理了副书记').text
# print(b)



