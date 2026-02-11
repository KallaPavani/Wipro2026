from flask import Flask, request, jsonify

app = Flask(__name__)

restaurants= []
dishes=[]
users=[]
orders=[]
ratings=[]

restaurants_id_counter=1
dish_id_counter=1
user_id_counter=1
order_id_counter=1
rating_id_counter=1

#============================== Restaurant Module ==============================================
#1. Register Restaurant
@app.route("/api/v1/restaurants", methods=["POST"])
def register_restaurants():
    global restaurants_id_counter
    data = request.get_json()
    if not data or not data.get("name"):
        return jsonify({"error": "REstaurant name is required"}), 400

    #Check duplicate
    for r in restaurants:
        if r["name"] == data["name"]:
            return jsonify({"error": "Restaurant name already exists"}), 409

    restaurant = {
        "id": restaurants_id_counter,
        "name": data["name"],
        "category": data.get("category"),
        "location": data.get("location"),
        "contact": data.get("contact"),
        "enabled": True
    }
    restaurants.append(restaurant)
    restaurants_id_counter+=1
    return jsonify(restaurant), 201

#2. View Restaurant
@app.route("/api/v1/restaurants/<int:restaurant_id>", methods=["GET"])
def view_restaurant(restaurant_id):
    for r in restaurants:
        if r["id"] == restaurant_id:
            return jsonify(r), 200
    return jsonify({"error": "restaurant not found"}), 404

#3. Update Restaurant
@app.route("/api/v1/restaurants/<int:restaurant_id>", methods=["PUT"])
def update_restaurant(restaurant_id):
    data = request.get_json()
    for r in restaurants:
        if r["id"] == restaurant_id:
            r.update(data)
            return jsonify(r), 200
    return jsonify({"error": "restaurant not found"}), 404

#4. Disable Restaurant
@app.route("/api/v1/restaurants/<int:restaurant_id>/disable", methods=["PUT"])
def disable_restaurant(restaurant_id):
    for r in restaurants:
        if r["id"] == restaurant_id:
            r["enabled"] = False
            return jsonify({"message": "Restaurant disabled"}), 200
    return jsonify({"error": "restaurant not found"}), 404

#5. Get all restaurants
@app.route('/api/v1/restaurants', methods=['GET'])
def get_all_restaurants():
    enabled = request.args.get('enabled')

    if enabled:
        filtered = [r for r in restaurants if str(r["enabled"]).lower() == enabled.lower()]
        return jsonify(filtered), 200

    return jsonify(restaurants), 200

#6. Delete Restaurant
@app.route("/api/v1/restaurants/<int:restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    global restaurants

    for r in restaurants:
        if r["id"] == restaurant_id:
            restaurants.remove(r)
            return jsonify({"message": "Restaurant deleted"}), 200

    return jsonify({"error": "restaurant not found"}), 404

#========================================= Dish Module ===================================================
#1. Add Dish
@app.route("/api/v1/restaurants/<int:restaurant_id>/dishes", methods=["POST"])
def add_dish(restaurant_id):
    global dish_id_counter
    data=request.get_json()
    #Check if restaurant exists
    restaurant_exists=any(r["id"]==restaurant_id for r in restaurants)
    if not restaurant_exists:
        return jsonify({"error": "restaurant not found"}), 404
    new_dish={
        "id": dish_id_counter,
        "restaurant_id": restaurant_id,
        "name": data.get("name"),
        "type": data.get("type"),
        "price": data.get("price"),
        "available_time": data.get("available_time"),
        "enabled": True
    }
    dishes.append(new_dish)
    dish_id_counter+=1
    return jsonify(new_dish), 201

#2. Update Dish
@app.route("/api/v1/dishes/<int:dish_id>", methods=["PUT"])
def update_dish(dish_id):
    data = request.get_json()
    for dish in dishes:
        if dish["id"] == dish_id:
            dish.update(data)
            return jsonify(dish), 200

    return jsonify({"error": "dish not found"}), 404

#3. Enable/Disable Dish
@app.route("/api/v1/dishes/<int:dish_id>/status", methods=["PUT"])
def update_dish_status(dish_id):
    data = request.get_json()

    for dish in dishes:
        if dish["id"] == dish_id:
            dish["enabled"] = data.get("enabled", dish["enabled"])
            return jsonify({"message": "Dish status updated"}), 200

    return jsonify({"error": "Dish not found"}), 404

#4. Delete Dish
@app.route("/api/v1/dishes/<int:dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    for dish in dishes:
        if dish["id"] == dish_id:
            dishes.remove(dish)
            return jsonify({"message": "Dish deleted"}), 200

    return jsonify({"error": "Dish not found"}), 404

#================================================User Module ==========================================================
#1.Register User
@app.route("/api/v1/users", methods=["POST"])
def register_user():
    global user_id_counter
    data=request.get_json()

    if not data or not data.get("name"):
        return jsonify({"error": "user name required"}), 400
    user={
        "id": user_id_counter,
        "name": data.get("name"),
        "email": data.get("email"),
        "enabled": True
    }
    users.append(user)
    user_id_counter+=1
    return jsonify(user), 201

#2. Search Restaurants
@app.route("/api/v1/restaurants/search", methods=["GET"])
def search_restaurants():
    name=request.args.get('name')
    category=request.args.get('category')
    location=request.args.get('location')
    result=restaurants
    if name:
        result=[r for r in result if name.lower() in r["name"].lower()]
    if category:
        result=[r for r in result if r.get("category") == category]
    if location:
        result=[r for r in result if r.get("location") == location]

    return jsonify(result), 200

#4. Place order
@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    global order_id_counter
    data=request.get_json()

    user_id=data.get("user_id")
    restaurant_id=data.get("restaurant_id")
    dish_ids=data.get("dish_ids")

    #Validate user
    if not any(u["id"]==user_id for u in users):
        return jsonify({"error": "user not found"}), 404

    #Validate restaurant
    if not any(r["id"] == restaurant_id for r in restaurants):
        return jsonify({"error": "restaurant not found"}), 404

    #Validate dishes
    selected_dishes = [d for d in dishes if d["id"] in dish_ids]
    if not selected_dishes:
        return jsonify({"error": "dish not found"}), 400
    total_price = sum(d["price"] for d in selected_dishes)

    order={
        "id": order_id_counter,
        "user_id": user_id,
        "restaurant_id": restaurant_id,
        "dishes": dish_ids,
        "total_price": total_price,
        "status": "Placed"
    }
    orders.append(order)
    order_id_counter+=1

    return jsonify(order), 201

#5. Ratings
@app.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    global rating_id_counter
    data = request.get_json()
    rating={
        "id": rating_id_counter,
        "user_id": data.get("user_id"),
        "restaurant_id": data.get("restaurant_id"),
        "rating": data.get("rating"),
        "comment": data.get("comment")
    }
    ratings.append(rating)
    rating_id_counter+=1
    return jsonify(rating), 201

# View Orders by User
@app.route("/api/v1/users/<int:user_id>/orders", methods=["GET"])
def get_orders_by_user(user_id):
    user_orders=[o for o in orders if o["user_id"] == user_id]
    if not user_orders:
        return jsonify({"message": "No orders found"}), 404
    return jsonify(user_orders), 200

#View Orders by Restaurant
@app.route("/api/v1/restaurants/<int:restaurant_id>/orders", methods=["GET"])
def get_orders_by_restaurant(restaurant_id):
    restaurant_orders = [o for o in orders if o["restaurant_id"] == restaurant_id]
    if not restaurant_orders:
        return jsonify({"message": "No orders found"}), 404
    return jsonify(restaurant_orders), 200

#Approve Restaurant
@app.route("/api/v1/admin/restaurants/<int:restaurant_id>/approve", methods=["PUT"])
def approve_restaurant(restaurant_id):
    for r in restaurants:
        if r["id"] == restaurant_id:
            r["approved"] = True
            return jsonify({"message": "Restaurant approved"}), 200
    return jsonify({"error": "Restaurant not found"}), 404

#Admin View All Orders
@app.route("/api/v1/admin/orders", methods=["GET"])
def admin_view_orders():
    return jsonify(orders), 200

#Admin View Ratings
@app.route("/api/v1/admin/ratings", methods=["GET"])
def admin_view_ratings():
    return jsonify(ratings), 200


if __name__ == "__main__":
    app.run(debug=True)