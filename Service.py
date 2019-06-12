#!flask/bin/python
import jieba

from flask import Flask,request
app = Flask(__name__)
@app.route("/test11",methods = ['POST','GET'])
def login():
    if request.method == "POST":
        content = request.form.get('content')
        print('Post: ' + content)
        aa = (' '.join(jieba.cut(content)))
        return aa
    if request.method == "GET":
        content = request.args.get('content')
        print('Get:    ' + content)
        aa = (' '.join(jieba.cut(content)))

        return  aa
if __name__ == '__main__':
  app.run(debug=True)