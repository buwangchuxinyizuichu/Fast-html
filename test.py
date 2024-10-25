from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/selection', methods=['POST'])
def handle_selection():
    data = request.get_json()
    selected_id = data.get('id')
    if selected_id:
        layer_index = int(selected_id.split('-')[1])
        selected_layer_info = layers_info[layer_index]
        return jsonify(selected_layer_info)
    return jsonify({'error': 'Invalid selection'}), 400


if __name__ == '__main__':
    app.run(debug=True)
