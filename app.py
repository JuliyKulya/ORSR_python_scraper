from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

@app.route('/get_all_data', methods=['POST'])
def get_all_data():
    # Get the value of 'IČO' from the JSON data in the request
    code = request.json.get('IČO')
    # Convert the code to a string
    code_str = str(code[0])
    # Search for a record in the database
    result = collection.find_one({"IČO": code_str})

    if result:
        result.pop('_id', None)
        return jsonify(result)
    else:
        return jsonify({"error": "IČO not found"}), 404

@app.route('/data_retrieval', methods=['GET'])
def data_retrieval():
    # get all rows from database with only required fields
    result = collection.find({}, {'_id': 0, 'IČO': 1, 'Obchodné meno': 1})

    #Convert the result to a list of dictionaries
    data = list(result)

    return jsonify(data)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)