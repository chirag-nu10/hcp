from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

@app.route('/')
def hello():

    directory = "hcp-search-extract"
    json_data = []

    for filename in os.listdir(directory):

        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                json_data.append(data)

            # print(f"Successfully read: {filename}")
        except json.JSONDecodeError:
            print(f"Error reading {filename}: Invalid JSON")
        except IOError:
            print(f"Error reading {filename}: File read error")
    
    print(f"Total JSON files read: {len(json_data)}")

    output = ""
    for data in json_data:
        output += str(data)

    return output

if __name__ == '__main__':
    app.run(debug=True)