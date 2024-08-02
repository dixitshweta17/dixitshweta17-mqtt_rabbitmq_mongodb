from flask import Flask, request, jsonify
from datetime import datetime
import pymongo
from dateutil import parser  # Import dateutil parser

app = Flask(__name__)

# DB Settings
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = 'mqtt_db'
COLLECTION_NAME = 'messages'

# Initialize MongoDB client
client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

for doc in collection.find():
    print(doc)

@app.route('/status_count', methods=['GET'])
def get_status_count():
    start_time = request.args.get('start')
    end_time = request.args.get('end')

    if not start_time or not end_time:
        return jsonify({"error": "start and end parameters are required"}), 400

    try:
        # Use dateutil.parser to parse ISO 8601 date strings
        start_dt = parser.isoparse(start_time)
        end_dt = parser.isoparse(end_time)
    except ValueError as e:
        return jsonify({"error": f"Invalid date format: {str(e)}"}), 400

    # Print datetime range for debugging
    print(f"Start datetime: {start_dt}")
    print(f"End datetime: {end_dt}")

    # Define the aggregation pipeline
    pipeline = [
    {"$match": {"timestamp": {"$gte": start_dt, "$lt": end_dt}}},
    {"$group": {"_id": "$status", "count": {"$sum": 1}}},
    {"$sort": {"_id": 1}}  # Optional: sort results by status
]
    
    # Print the pipeline for debugging
    print("Aggregation pipeline:", pipeline)

    try:
        # Execute the aggregation pipeline
        results = list(collection.aggregate(pipeline))
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


    # print('Results:', results)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
