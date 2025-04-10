from flask import Flask, request, jsonify
import torch

# Supposons que ton modèle BiLSTM est chargé ici
# bi_lstm_model = torch.load('ton_modele_bilstm.pth')

app = Flask(__name__)

# Fonction pour prédire avec le modèle BiLSTM
def generate_response(input_seq):
    # Encoder l'input
    enc_out, enc_states = encoder_model.predict(input_seq)

    # Démarrer avec le token <start>
    target_seq = np.zeros((1, 1))
    target_seq[0, 0] = word_index['<start>']

    stop_condition = False
    response = []

    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + [enc_out] + enc_states)

        # Sélectionner le token avec la plus haute probabilité
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_word = None

        for word, index in word_index.items():
            if index == sampled_token_index:
                sampled_word = word
                response.append(word)

        # Condition d'arrêt: <end> ou longueur max atteinte
        if sampled_word == '<end>' or len(response) >= MAX_LENGTH:
            stop_condition = True

        # Mettre à jour la séquence cible
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index

        # Mettre à jour les états
        enc_states = [h, c]

    return ' '.join(response[:-1])  # Exclure le token <end>

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
