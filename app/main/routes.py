from app.main import bp
from flask import request, jsonify
from app.sql.SQLiteDatabaseReader import SQLiteDatabaseReader
from app.main.databases import get_databases
from app.llama import llama
DATABASES_PATH = "db/"


@bp.route('/sql/db', methods=['GET'])
def databases():
    return jsonify(get_databases())


@bp.route('/sql/query', methods=['POST'])
def generate_query():
    try:
        data = request.get_json()

        if "input" in data and "dataset" in data:
            input_string = data["input"]
            dataset = data["dataset"]

            prompt = llama.prepare_prompt(dataset, input_string)
            result = llama.request_llama(prompt)

            response = {
                "result": result
            }
            return jsonify(response), 200
        else:
            return jsonify({"error": "Invalid request body"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/sql/data', methods=['POST'])
def run_query():
    try:
        data = request.get_json()

        if "query" in data and "dataset" in data:
            query = data["query"]
            dataset = data["dataset"]

            sql_reader = SQLiteDatabaseReader(f"{DATABASES_PATH + dataset}.db")
            sql_reader.connect()

            columns, rows = sql_reader.execute_query(query)

            sql_reader.close()

            response = {
                "columns": columns,
                "rows": rows
            }

            return jsonify(response), 200
        else:
            return jsonify({"error": "Invalid request body"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
