from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from gtts import gTTS
from config import DATABASE_URI, TTS_LANGUAGE

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False)


@app.route('/generate', methods=['POST'])
def generate_audio():
    token = request.headers.get('Authorization')

    if not Token.query.filter_by(token=token).first():
        return jsonify({'error': 'Invalid token'}), 401

    text = request.form.get('text')

    tts = gTTS(text=text, lang=TTS_LANGUAGE)
    tts.save('output.mp3')

    return send_file('output.mp3')


if __name__ == '__main__':
    app.run()
