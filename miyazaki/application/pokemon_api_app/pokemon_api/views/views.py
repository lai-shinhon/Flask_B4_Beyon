from flask import request, redirect, url_for, render_template, flash, session
from pokemon_api import app
from pokemon_api import db
from pokemon_api.models.pokemons import Pokemon



@app.route('/')
def index_page():
    return render_template('pokemons/index.html')


@app.route('/get')
def get_page():
    return render_template('pokemons/get.html')


@app.route('/show')
def show_page():
    pokemons = Pokemon.query.order_by(Pokemon.get_at.desc()).all()
    return render_template('pokemons/show.html', pokemons = pokemons)


@app.route('/pokemon_get', methods=['POST'])
def pokemon_get():
    p_name = request.form['pokemon_name']
    p_id = request.form['pokemon_id']
    p_height = request.form['pokemon_height']
    p_weight = request.form['pokemon_weight']
    p_types = request.form['pokemon_types']
    p_image_url = request.form['pokemon_image']
    
    print(p_name)

    if Pokemon.query.get(p_name) is None:
        pokemon = Pokemon(
            name = p_name,
            id = p_id,
            height = p_height,
            weight = p_weight,
            types = p_types,
            image_url = p_image_url,
        )
        db.session.merge(pokemon)
        db.session.commit()
        flash(f'{p_name}が図鑑に登録されました！')
        return render_template('pokemons/index.html')
    else:
        flash(f'{p_name}はすでに登録されています')
        return render_template('pokemons/index.html')
    
@app.route('/show/<string:name>', methods=['POST'])
def show_pokemon(name):
    pokemon = Pokemon.query.get(name)
    return render_template('pokemons/show_pokemon.html', pokemon = pokemon)
    

@app.route('/deleate/<string:name>', methods=['POST'])
def delete_pokemon(name):
    pokemon = Pokemon.query.get(name)
    p_name = pokemon.name
    db.session.delete(pokemon)
    db.session.commit()
    flash(f'{p_name}を逃がした！')
    return render_template('pokemons/index.html')