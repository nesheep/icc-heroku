from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import numpy as np
import cv2
import image_converting as imcon
from datetime import datetime
import os
import string

#加工画像の保存先フォルダを確認・作成
SAVE_DIR = "./images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

#アプリの作成
app = Flask(__name__, static_url_path="")

#htmlのレンダリング
@app.route('/')
def index():
    return render_template('index.html', images=os.listdir(SAVE_DIR)[::-1])

#ディレクトリからのダウンロード
@app.route('/images/<path:filename>')
def send_js(filename):
    return send_from_directory(SAVE_DIR, filename)

@app.route('/upload', methods=['POST'])
def upload():
    if request.files['image']:

        #クラスター数の入力情報取得
        k=request.form.get('clusterN')

        # 画像として読み込み
        stream = request.files['image'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # 変換
        x,y,z = imcon.Kmeans(img,int(k))

        # 保存
        dt_now = datetime.now().strftime("%Y%m%d%H%M%S_")
        save_path = os.path.join(SAVE_DIR, dt_now+k+".jpg")
        cv2.imwrite(save_path, z)

        print("save", save_path)

        return redirect('/')

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=os.environ.get('PORT', 5000),threaded=True)
#http://127.0.0.1:5000/