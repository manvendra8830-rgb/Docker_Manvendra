from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "Backend is running successfully."
    })


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    try:
        data = request.get_json(silent=True) or {}

        item_name = str(data.get("itemName", "")).strip()
        item_description = str(data.get("itemDescription", "")).strip()

        if not item_name or not item_description:
            return jsonify({
                "error": "Item Name and Item Description are required."
            }), 400

        item_id = str(uuid.uuid4())

        return jsonify({
            "message": "To-Do item processed successfully.",
            "itemId": item_id,
            "itemName": item_name,
            "itemDescription": item_description
        }), 201

    except Exception as error:
        return jsonify({
            "error": "An error occurred while processing the request.",
            "details": str(error)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
