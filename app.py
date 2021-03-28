from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from bson.objectid import ObjectId
import requests


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://viniciusvn:Spphqk12@owlhouse.nbmdy.mongodb.net/movies'
}

db = MongoEngine()
db.init_app(app)

class Movies(db.Document):
    id = db.ObjectIdField(primary_key=True)
    title = db.StringField(max_length=(256), required=True)
    author = db.StringField(max_length=(256))


    def to_json(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author
        }

@app.route('/addmovie', methods=['POST'])
def addmovie():
    movie_data = request.get_json()

    new_movie = Movies(id=ObjectId(), title=movie_data['title'], author=movie_data['author'])
    new_movie.save()

    return 'Done', 201

@app.route('/moedasvalores')
def movieslist():
    
    moedas = requests.get('https://economia.awesomeapi.com.br/json/all')


    return moedas.json()
if __name__ == '__main__':
    app.run(debug=True)