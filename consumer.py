from kafka import KafkaConsumer
from flask import Flask, jsonify
import json
import threading

app = Flask(__name__)

media_global = 0.0

@app.route('/media', methods=['GET'])
def get_media():
    return jsonify({"media": media_global})

def consumir_kafka():
    global media_global

    consumer = KafkaConsumer(
        'temperatura',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    dados = []

    for msg in consumer:
        evento = msg.value
        dados.append(evento)

        media_global = sum(
            d['temperatura'] for d in dados
        ) / len(dados)

        print("Nova média:", media_global)

if __name__ == '__main__':
    threading.Thread(target=consumir_kafka, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
