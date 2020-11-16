import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np

from string import punctuation

import numpy as np

from flask import Flask, jsonify, request
from flask_cors import CORS

import logging

app = Flask(__name__)
CORS(app)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Vocabulary
vocab_to_int = np.load("../data/vocab_to_int.npy", allow_pickle = True).item()

# MODEL
class SentimentAnalyzer(nn.Module):
    def __init__(
        self,
        vocab_size,
        output_size,
        embedding_dim,
        hidden_dim,
        n_layers
    ):
        super(SentimentAnalyzer, self).__init__()
        
        # Output layer size
        self.output_size = output_size
        
        # Number of LSTM layers
        self.n_layers = n_layers
        
        # Hidden layer dimension of LSTM cell
        self.hidden_dim = hidden_dim
        
        # Embedding layer
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx = -1)
        
        # LSTM layer
        self.lstm = nn.LSTM(
            embedding_dim,
            hidden_dim,
            n_layers,
            dropout = 0.5,
            batch_first = True
        )
        
        # Fully connected layer
        self.fc = nn.Linear(hidden_dim, output_size)
        
    def forward(self, x, hidden):
        
        # Xs are going to be of size BATCH_SIZE x SEQ_LEN
        # We are interested in the batch size, so x.size(0)
        # will give us that
        batch_size = x.size(0)
        
        # Output from the embedding layer
        embeds = self.embedding(x)
        
        # Output and new hidden layer from
        # LSTM layer
        lstm_out, hidden = self.lstm(embeds, hidden)
        
        # We'll convert that LSTM output into a contiguous
        # tensor. This prevents certain runtime errors
        # from occuring when certain operations happen
        # (like getting a view of a transposed tensor)
        lstm_out = lstm_out.contiguous().view(-1, self.hidden_dim)
        
        # Output after dropping some neurons with
        # 30% dropout rate
        out = F.dropout(lstm_out, 0.3)
        
        # Output of fully connected layer
        out = self.fc(out)
        
        # Our labels are -1, 0 and 1
        # Tanh(x) belongs to the interval [-1, 1]
        tanh_out = F.tanh(out)
        tanh_out = tanh_out.view(batch_size, -1)
        tanh_out = tanh_out[:,-1]
        
        return tanh_out, hidden
    
    
    def init_hidden(self, batch_size):
        weight = next(self.parameters()).data
        
        hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_(), 
                 weight.new(self.n_layers, batch_size, self.hidden_dim).zero_())
        return hidden

def pad_features(comments_int, seq_length):
    features = np.zeros((len(comments_int), seq_length), dtype = int)
    
    for i, comment in enumerate(comments_int):
        comment_len = len(comment)
        
        if comment_len <= seq_length:
            zeros = list(np.zeros(seq_length - comment_len))
            new = zeros + comment        
        elif commment_len > seq_length:
            new = comment[0:seq_length]
        
        features[i,:] = np.array(new)
    
    return features

def tokenize(comment):
    comment = comment.lower()
    text = ''.join([char for char in comment if char not in punctuation])

    words = text.split(" ")

    ints = []
    ints.append([vocab_to_int[word] for word in words if word in list(vocab_to_int.keys())])
    
    return ints

model = torch.load("../models/SentimentAnalyzerBestModel.pth", map_location = torch.device('cpu'))
seq_len = 150

def verdict(x):
    if x < 0.45:
        return "negative"
    elif x >= 0.45 and x <= 0.75:
        return "neutral"
    else:
        return "positive"

@app.route("/predict", methods = ["POST"])
def predict():
    print("lmao")
    model.eval()
    
    comment = request.json
    ints = tokenize(comment)
    features = torch.from_numpy(pad_features(ints, seq_len))

    batch_size = features.size(0)
    hidden_state = model.init_hidden(batch_size)
    
    out, hidden_state = model(features, hidden_state)
    pred = torch.round(out.squeeze())

    # print(f'Prediction: {(out.item() + 1) / 2:.4f} | Verdict: {verdict(out.item())} | Ints: {ints}')

    response = jsonify(f"{(out.item() + 1) / 2:.4f}")

    return response
    
if __name__ == "__main__":
    app.run()