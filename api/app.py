import flask

app = flask.Flask(__name__)

beers = [
    {
        'id': 1,
        'brand': u'guinness',
        'description': u'thicc and delicious',
        'drinkable': True,
    },
    {
        'id': 2,
        'brand': u'modelo',
        'description': u'its modelo time',
        'drinkable': True,
    },
    {
        'id': 3,
        'brand': u'coors',
        'description': u'dads favorite',
        'drinkable': False,
    },
]

@app.route('/satnight/api/v1.0/beers', methods = ['GET'])
def get_beers():
    return(flask.jsonify({'beers': beers}))

@app.route('/satnight/api/v1.0/beers/<int:beer_id>', methods = ['GET'])
def get_beer(beer_id):
    beer = [beer for beer in beers if beer['id'] == beer_id]
    if len(beer) == 0:
        flask.abort(404)
    return(flask.jsonify({'beer': beer[0]}))

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True)
