from flask import Flask, render_template, request, redirect, url_for, flash, \
    jsonify
from sqlalchemy.orm import sessionmaker
from restaurants import Base, Restaurant, MenuItem, engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurant_menu_json(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/JSON')
def menu_item_json(restaurant_id, menu_item_id):
    item = session.query(MenuItem).filter_by(id=menu_item_id).one()
    return jsonify(MenuItem=item.serialize)


@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('restaurant_menu.html', restaurant=restaurant, items=items)


@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    if request.method == 'POST':
        new_item = MenuItem(name=request.form['name'],
                            restaurant_id=restaurant_id)
        session.add(new_item)
        session.commit()
        flash('New menu item created!')
        return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))
    else:
        return render_template('new_menu_item.html',
                               restaurant_id=restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_item_id>/edit/',
           methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_item_id):
    menu_item = session.query(MenuItem).filter_by(id=menu_item_id).one()
    if request.method == 'POST':
        old_name = menu_item.name
        menu_item.name = request.form['name']
        session.add(menu_item)
        session.commit()
        flash('Changed: "{}" to: "{}"'.format(old_name, menu_item.name))
        return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))
    else:
        return render_template('edit_menu_item.html',
                               restaurant_id=restaurant_id,
                               menu_item_id=menu_item_id, menu_item=menu_item)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_item_id>/delete/',
           methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_item_id):
    menu_item = session.query(MenuItem).filter_by(id=menu_item_id).one()
    if request.method == 'POST':
        session.delete(menu_item)
        session.commit()
        flash('{} deleted!'.format(menu_item.name))
        return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))
    else:
        return render_template('delete_menu_item.html',
                               restaurant_id=restaurant_id, menu_item_id=menu_item_id,
                               menu_item=menu_item)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.debug = True
    app.run(port=5000)
