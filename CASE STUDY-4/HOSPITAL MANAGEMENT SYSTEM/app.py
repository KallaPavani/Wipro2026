from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)
patients = []

@app.route("/")
def home():
    return render_template("register.html")

# ============ API ===============

@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(patients), 200

@app.route("/api/patients", methods=["POST"])
def add_patient():
    data = request.json
    patient = {   # ✅ singular
        "id": len(patients) + 1,
        "name": data["name"],
        "age": data["age"],
        "gender": data["gender"],
        "contact": data["contact"],
        "disease": data["disease"],
        "doctor": data["doctor"]
    }
    patients.append(patient)     # ✅ list append
    return jsonify(patient), 201

@app.route("/api/patients/<int:pid>", methods=["GET"])
def get_patient(pid):
    for p in patients:
        if p["id"] == pid:
            return jsonify(p)
    return jsonify({"error": "Patient not found"}), 404

@app.route("/api/patients/<int:pid>", methods=["PUT"])
def update_patient(pid):
    data = request.json
    for p in patients:
        if p["id"] == pid:
            p.update(data)
            return jsonify(p)
    return jsonify({"error": "Patient not found"}), 404

@app.route("/api/patients/<int:pid>", methods=["PATCH"])
def patch_patient(pid):
    data = request.json
    for p in patients:
        if p["id"] == pid:
            p.update(data)
            return jsonify(p), 200
    return jsonify({"error": "Patient not found"}), 404

@app.route("/api/patients/<int:pid>", methods=["DELETE"])
def delete_patient(pid):
    for p in patients:
        if p["id"] == pid:
            patients.remove(p)
            return jsonify({"message": "Patient deleted successfully"}), 200
    return jsonify({"error": "Patient not found"}), 404


# ------------ WEB -------------

@app.route("/register", methods=["POST"])
def register_patient_web():
    patient = {
        "id": len(patients) + 1,
        "name": request.form["name"],
        "age": request.form["age"],
        "gender": request.form["gender"],
        "contact": request.form["contact"],
        "disease": request.form["disease"],
        "doctor": request.form["doctor"]
    }
    patients.append(patient)
    return redirect(url_for("list_patients"))

@app.route("/patients")
def list_patients():
    return render_template("patients.html", patients=patients)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
