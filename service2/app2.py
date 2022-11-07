from flask import Flask, request, jsonify, current_app, g
import time

# client = pymongo.MongoClient("mongodb+srv://ncku_gwhsu:123@cluster0.wtz5pwg.mongodb.net/?retryWrites=true&w=majority")
# db = client['containers']['delay1']  # service1

app = Flask(__name__)


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        # just calculate
        ans = []

        for i in range(2000):
            tmp = i**(i+1)
            ans.append(tmp)
        # data = request.form
        # global num_req
        # num_req = data['num']

        return 'store data to mongodb'
    else:
        return 'Hello Dcnlab'


if __name__ == '__main__':
    # start_time = time.time()
    app.run('0.0.0.0', debug=True)  # threaded=False


