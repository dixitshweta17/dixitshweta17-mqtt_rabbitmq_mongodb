from flask import Flask, request, jsonify
from datetime import datetime
import pymongo   #for mongodb

app= Flask(__name__)    #To define our Flask Object

#DB Settings
RABBITMQ_HOST = 'localhost'
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = 'mqtt_db'
COLLECTION_NAME = 'messages'

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

@app.route('/status_count', methods=['GET'])
def get_status_count():
    start_time = request.args.get('start')
    end_time = request.args.get('end')

    start_dt = datetime.fromisoformat(start_time)   #(YYYY-MM-DDTHH:MM:SS).
    end_dt = datetime.fromisoformat(end_time)


    pipeline = [
        {"$match":{"timestamp":{"$gte": start_dt, "$lt": end_dt}}},
        {"$group":{"_id":"$status", "count":{"$sum":1}}}
    ]

    results = list(collection.aggregate(pipeline))
    
    # print("get_status_count", get_status_count())
    print('results', results)
    return jsonify(results)
    
if __name__ == '__main__':
    app.run(debug=True)