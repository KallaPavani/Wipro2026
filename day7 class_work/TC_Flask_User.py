from flask import Flask,request,jsonify

app1=Flask(__name__)

users = [
    {"id":1,"name":"Pavani"},
    {"id":2,"name":"Preethi"}
    ]

@app1.route("/",methods=["GET"])
def home():
    return "Welcome to my Course App"

@app1.route("/users",methods=["GET"])
def get_users():
    return jsonify(users)

@app1.route("/users/<int:user_id>",methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"]==user_id:
            return jsonify(user)
    return jsonify({"error":"404 user not found"}), 404

@app1.route("/users",methods=["POST"])
def add_user():
    data=request.json
    new_user={"id":len(users)+1,"name":data.get("name")}
    users.append(new_user)
    return jsonify(new_user),201
@app1.route("/users/<int:user_id>",methods=["PUT"])
def update_user_put(user_id):
    data=request.json
    for user in users:
        if user["id"]==user_id:
            user["name"]=data.get("name")
            return jsonify(user),200
    return jsonify({"error":"404 user not found"}), 404


@app1.route("/users/<int:user_id>", methods=["PATCH"])
def update_user_patch(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name")
            return jsonify(user)
    return jsonify({"message": "user not found"}), 404

@app1.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "404 user not found"}), 404



if __name__=="__main__":
    app1.run(debug=True,port=5001)



