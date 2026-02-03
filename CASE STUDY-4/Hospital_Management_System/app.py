from flask import Flask, request, jsonify

app = Flask(__name__)
patients = []

#Home route
@app.route("/")
def home():
    return "Welcome to Hospital Management System"

#Fetch all patients
@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(patients), 200

#Get single patient by ID
@app.route("/api/patients/<int:patient_id>", methods=["GET"])
def get_patient(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return jsonify(patient), 200
    return jsonify({"error": "Patient not found"}), 404

#Register a patient
@app.route("/api/patients", methods=["POST"])
def add_patient():
    data = request.json
    new_patient = {
        "id": len(patients) + 1,
        "name": data.get("name"),
        "age": data.get("age"),
        "gender": data.get("gender"),
        "contact": data.get("contact"),
        "disease": data.get("disease"),
        "doctor": data.get("doctor")
    }
    patients.append(new_patient)
    return jsonify(new_patient), 201

#Update patient info
@app.route("/api/patients/<int:patient_id>", methods=["PUT"])
def update_patient(patient_id):
    data = request.json
    for patient in patients:
        if patient["id"] == patient_id:
            patient.update(data)
            return jsonify(patient), 200
    return jsonify({"error": "Patient not found"}), 404

@app.route("/api/patients/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            return jsonify({"message": "Patient deleted successfully"}), 200
    return jsonify({"error": "Patient not found"}), 404


if __name__ == "__main__":
    app.run(debug=True,port=5002)