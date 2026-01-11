import io
import os
from werkzeug.utils import secure_filename
import uuid
from datetime import datetime 
from flask_restful import Api
from flask import Flask, render_template, redirect, url_for, request, abort, session, jsonify
from werkzeug.serving import WSGIRequestHandler
from utils import *
from random import randint

from data import db_session
from data.items import Items
from data.colors import Colors
from data.factures import Factures
from data.types import Types
from data.photos import Photos

app = Flask(__name__)
app.config["SECRET_KEY"] = "TorezKirZ"
app.config['UPLOAD_FOLDER'] = 'uploads'

api = Api(app)

db_session.global_init('db/tkz.db')

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def main_page():
    session = db_session.create_session()

    kips = []
    data = session.query(Items).filter((Items.typee_id == 1)).all()
    for i in range(len(data) // 5):
        if 36 <= i*5 + randint(1, 5) <= 40:
            continue
        kips.append(data[i*5 + randint(1, 5) - 1])
    kips_plane = []
    kips_fin = []
    kips_oldtown = []
    kips_rock = []
    kips_marble = []
    kips_base = []
    for item in kips:
        item_dict = {"name": item.name,
            "size": item.size,
            "id": item.id,
            "price_no_package": item.price_no_package,
            "filepath": session.query(Photos).filter(item.id == Photos.id).first().filepath}
        if item.facture_id == 1: kips_plane.append(item_dict)
        elif item.facture_id == 2: kips_fin.append(item_dict)
        elif item.facture_id == 3: kips_oldtown.append(item_dict)
        elif item.facture_id == 4: kips_rock.append(item_dict)
        elif item.facture_id in [5, 6]: kips_marble.append(item_dict)
        elif item.facture_id == 7: kips_base.append(item_dict)
    
    tiles = []
    data = session.query(Items).filter((Items.typee_id == 2)).all()
    for i in range(len(data) // 5):
        tiles.append(data[i*5 + randint(1, 5) - 1])
    tiles_oldtown = []
    tiles_rock = []
    tiles_marble = []
    tiles_base = []
    tiles_path = []
    for item in tiles:
        item_dict = {"name": item.name,
            "size": item.size,
            "id": item.id,
            "price_no_package": item.price_no_package,
            "filepath": session.query(Photos).filter(item.id == Photos.id).first().filepath}
        if item.facture_id == 3: tiles_oldtown.append(item_dict)
        elif item.facture_id == 4: tiles_rock.append(item_dict)
        elif item.facture_id in [5, 6]: tiles_marble.append(item_dict)
        elif item.facture_id == 7: tiles_base.append(item_dict)
        elif item.facture_id == 8: tiles_path.append(item_dict)


    param = {
        'kips_plane': kips_plane, 
        'kips_fin': kips_fin, 
        'kips_oldtown': kips_oldtown, 
        'kips_rock': kips_rock, 
        'kips_marble': kips_marble,
        'kips_base': kips_base,
        'tiles_oldtown': tiles_oldtown, 
        'tiles_rock': tiles_rock, 
        'tiles_marble': tiles_marble,
        'tiles_base': tiles_base,
        'tiles_path': tiles_path,
    }
    return render_template('main.html', **param)


@app.route('/about', methods=['GET'])
def apps_panel():
    return render_template('about.html')


@app.route('/item/<int:id>', methods=['GET'])
def get_items(id):
    session = db_session.create_session()
    if id % 5 == 0:
        id -= 4;
    else:
        id = (id - (id % 5)) + 1
    data = session.query(Items).filter(Items.id.between(id, id + 4)).all()
    items = []
    for item in data:
        item_dict = {"name": item.name,
            "size": item.size,
            "id": item.id,
            "amount_per_meter": item.amount_per_meter,
            "weight": item.weight,
            "amount": item.amount,
            "price_no_package": item.price_no_package,
            "color": session.query(Colors).filter(item.color_id == Colors.id).first().color.lower(),
            "filepath": session.query(Photos).filter(item.id == Photos.id).first().filepath}
        if item_dict['amount_per_meter'] is None:
            item_dict['amount_per_meter'] = '-'
        items.append(item_dict)
    param = {'items': items}
    return render_template('product.html', **param)


def main():
    session = db_session.create_session()
    session.commit()
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()
