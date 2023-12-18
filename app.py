from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://lilislediana90:lilis_1602@cluster0.jhzn89k.mongodb.net/')

db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    # sample_receive = request.form['sample_give']
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive,
    }
    db.orders.insert_one(doc)
    return jsonify({'msg': 'complete!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    orders_list = list(db.orders.find({}, {'_id': False}))
    return jsonify({'orders': orders_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)