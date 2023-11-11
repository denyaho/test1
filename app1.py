from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route("/")#ルートのアドレスにそれ以下のものを設置する
def hello():
    html=render_template("index.html",a="テスト")
    return html

if __name__=="__main__":
    app.run()