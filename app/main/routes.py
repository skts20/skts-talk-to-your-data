from app.main import bp
from flask import request, jsonify
from app.sql.SQLiteDatabaseReader import SQLiteDatabaseReader


@bp.route('/sql/query', methods=['POST'])
def process_json():
    try:
        data = request.get_json()

        if "input" in data and "dataset" in data:
            input_string = data["input"]
            dataset = data["dataset"]

            # llama processing -----

            response = {
                #     tutaj dajemy wynik z llamy
            }
            return jsonify(response), 200
        else:
            return jsonify({"error": "Invalid request body"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/sql/data', methods=['POST'])
def process_json():
    try:
        data = request.get_json()

        if "query" in data and "dataset" in data:
            query = data["input"]
            dataset = data["dataset"]

            sql_reader = SQLiteDatabaseReader(dataset)
            sql_reader.connect()

            result = sql_reader.execute_query(query)

            sql_reader.close()

            response = {
                # dajemy w jakiesjs fajnej strukturce
                result
            }
            return jsonify(response), 200
        else:
            return jsonify({"error": "Invalid request body"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
