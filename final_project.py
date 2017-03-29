from flask import Flask, render_template
app = Flask(__name__)


# Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}
restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

# Fake Menu Items
items = [{'name': 'Cheese Pizza', 'description': 'made with fresh cheese',
          'price': '$5.99','course': 'Entree', 'id': '1'},
         {'name': 'Chocolate Cake', 'description': 'made with Dutch Chocolate',
          'price': '$3.99', 'course': 'Dessert', 'id': '2'},
         {'name': 'Caesar Salad',
          'description': 'with fresh organic vegetables', 'price': '$5.99',
          'course': 'Entree', 'id': '3'},
         {'name': 'Iced Tea', 'description': 'with lemon', 'price': '$.99',
          'course': 'Beverage', 'id': '4'},
         {'name': 'Spinach Dip', 'description': 'creamy dip with fresh spinach',
          'price': '$1.99', 'course': 'Appetizer', 'id': '5'}]
item = {'name': 'Cheese Pizza', 'description': 'made with fresh cheese',
        'price': '$5.99', 'course': 'Entree', 'id': '1'}


@app.route('/')
@app.route('/restaurants/')
def restaurants_list():
    return render_template('restaurants_list.html', restaurants=restaurants)


@app.route('/restaurants/new')
def new_restaurant():
    return render_template('new_restaurant.html')


@app.route('/restaurants/<int:restaurant_id>/edit/')
def edit_restaurant(restaurant_id):
    return render_template('edit_restaurant.html', restaurant=restaurant)


@app.route('/restaurants/<int:restaurant_id>/delete/')
def delete_restaurant(restaurant_id):
    return render_template('delete_restaurant.html', restaurant=restaurant)


@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def restaurant_menu(restaurant_id):
    return render_template('restaurant_menu.html', restaurant=restaurant,
                           items=items)


@app.route('/restaurants/<int:restaurant_id>/menu/new/')
def new_menu_item(restaurant_id):
    return render_template('new_menu_item.html', restaurant_id=restaurant['id'])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/edit/')
def edit_menu_item(restaurant_id, menu_item_id):
    return render_template('edit_menu_item.html', restaurant=restaurant,
                           menu_item=item, menu_item_id=menu_item_id)


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>/delete/')
def delete_menu_item(restaurant_id, menu_item_id):
    # return "This page is for deleting menu item {}".format(menu_item_id)
    return render_template('delete_menu_item.html', restaurant=restaurant,
                           menu_item=item)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
