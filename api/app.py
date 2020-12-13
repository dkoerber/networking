import flask as f

app = f.Flask(__name__)

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
    return(f.jsonify({'beers': beers}))

@app.route('/satnight/api/v1.0/beers/<int:beer_id>', methods = ['GET'])
def get_beer(beer_id):
    beer = [beer for beer in beers if beer['id'] == beer_id]

    if len(beer) == 0:
        f.abort(404)

    return(f.jsonify({'beer': beer[0]}))

@app.route('/satnight/api/v1.0/beers', methods = ['POST'])
def add_beer():
    if not f.request.json or not 'brand' in f.request.json:
        f.abort(400)

    beer = {
        'id': beers[-1]['id'] + 1,
        'brand': f.request.json['brand'],
        'description': f.request.json.get('description', ""),
        'drinkable': True,
    }
    beers.append(beer)

    return(f.jsonify({'beer': beer}), 201)

@app.route('/satnight/api/v1.0/beers/<int:beer_id>', methods = ['PUT'])
def update_beer(beer_id):
    beer = [beer for beer in beers if beer['id'] == beer_id]

    if len(beer) == 0:
        f.abort(404)
    if not f.request.json:
        f.abord(400)
    if 'brand' in f.request.json and not isinstance(f.request.json['brand'], str):
        f.abort(400)
    if 'description' in f.request.json and not isinstance(f.request.json['description'], str):
        f.abort(400)
    if 'drinkable' in f.request.json and not isinstance(f.request.json['drinkable'], bool):
        f.abort(400)

    beer[0]['brand'] = f.request.json.get('brand', beer[0]['brand'])
    beer[0]['description'] = f.request.json.get('description', beer[0]['description'])
    beer[0]['drinkable'] = f.request.json.get('drinkable', beer[0]['drinkable'])

    return(f.jsonify({'beer': beer[0]}))

@app.route('/satnight/api/v1.0/beers/<int:beer_id>', methods = ['DELETE'])
def delete_beer(beer_id):
    beer = [beer for beer in beers if beer['id'] == beer_id]

    if len(beer) == 0:
        f.abort(404)
    beers.remove(beer[0])

    return(f.jsonify({'result': True}))

@app.errorhandler(400)
def bad_request(error):
    return(f.make_response(f.jsonify({'error': 'Bad request'}), 400))

@app.errorhandler(404)
def not_found(error):
    return(f.make_response(f.jsonify({'error': 'Not found'}), 404))

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True)
