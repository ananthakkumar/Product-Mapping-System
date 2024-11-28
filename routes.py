from flask import render_template, request, redirect, url_for
from . import db
from .models import ProductMapping
from .utils import normalize_text, match_product, load_mapping

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    input_name = request.form.get('product_name')
    mappings = load_mapping()
    match, confidence = match_product(input_name, mappings)

    if match:
        return render_template('match.html', match=match, confidence=confidence)
    else:
        return render_template('match.html', manual=True, input_name=input_name)

@app.route('/add_mapping', methods=['POST'])
def add_mapping():
    supplier_name = request.form.get('supplier_name')
    standardized_name = request.form.get('standardized_name')
    new_mapping = ProductMapping(supplier_name=supplier_name, standardized_name=standardized_name)
    db.session.add(new_mapping)
    db.session.commit()
    return redirect(url_for('index'))
