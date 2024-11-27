from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)
app.secret_key = 'a2d1c3f7e9a4b6d7c8f0e1d2c3a4b5c6' # Required for session handling

#print(f"Secret Key: {app.secret_key}")

# MongoDB setup
username = "rbhogate"
password = "World@123"
host = "ssoapp.rgo6i.mongodb.net"
database_name = "survey_data"

# Encode username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)


MONGO_URI = f"mongodb+srv://{encoded_username}:{encoded_password}@{host}/{database_name}?retryWrites=true&w=majority" # Replace with your MongoDB connection string
client = MongoClient(MONGO_URI)
db = client['survey_data']  # Database name
collection = db['responses']  # Collection name

@app.route('/conveningbasics.html', methods=['GET', 'POST'])
def convening_basics():
    if request.method == 'POST':
        session['convening_basics'] = request.form.to_dict(flat=False)
        print("Convening Basics Data:", session['convening_basics'])
        return jsonify({"message": "Data received", "data": session['convening_basics']})
    return render_template('conveningbasics.html')

@app.route('/conveningformatsandspaces.html', methods=['GET', 'POST'])
def convening_formats_and_spaces():
    if request.method == 'POST':
        session['convening_formats_and_spaces'] = request.form.to_dict(flat=False)
        print("Convening Formats and Spaces Data:", session['convening_formats_and_spaces'])
        return jsonify({"message": "Data received", "data": session['convening_formats_and_spaces']})
    return render_template('conveningformatsandspaces.html')

@app.route('/spacephotos.html', methods=['GET', 'POST'])
def space_photos():
    if request.method == 'POST':
        session['space_photos'] = request.form.to_dict(flat=False)
        print("Space Photos Data:", session['space_photos'])
        return jsonify({"message": "Data received", "data": session['space_photos']})
    return render_template('spacephotos.html')

@app.route('/timesandcounts.html', methods=['GET', 'POST'])
def times_and_counts():
    if request.method == 'POST':
        session['times_and_counts'] = request.form.to_dict(flat=False)
        print("Times and Counts Data:", session['times_and_counts'])
        return jsonify({"message": "Data received", "data": session['times_and_counts']})
    return render_template('timesandcounts.html')

@app.route('/proceduresandnorms.html', methods=['GET', 'POST'])
def procedures_and_norms():
    if request.method == 'POST':
        session['procedures_and_norms'] = request.form.to_dict(flat=False)
        print("Procedures and Norms Data:", session['procedures_and_norms'])
        return jsonify({"message": "Data received", "data": session['procedures_and_norms']})
    return render_template('proceduresandnorms.html')

@app.route('/activities.html', methods=['GET', 'POST'])
def activities():
    if request.method == 'POST':
        session['activities'] = request.form.to_dict(flat=False)
        print("Activities Data:", session['activities'])
        return jsonify({"message": "Data received", "data": session['activities']})
    return render_template('activities.html')

@app.route('/organizingandmobilizing.html', methods=['GET', 'POST'])
def organizing_and_mobilizing():
    if request.method == 'POST':
        session['organizing_and_mobilizing'] = request.form.to_dict(flat=False)
        print("Organizing and Mobilizing Data:", session['organizing_and_mobilizing'])
        return jsonify({"message": "Data received", "data": session['organizing_and_mobilizing']})
    return render_template('organizingandmobilizing.html')

@app.route('/publicsphere.html', methods=['GET', 'POST'])
def public_sphere():
    if request.method == 'POST':
        session['public_sphere'] = request.form.to_dict(flat=False)
        print("Public Sphere Data:", session['public_sphere'])
        return jsonify({"message": "Data received", "data": session['public_sphere']})
    return render_template('publicsphere.html')

@app.route('/decisionmaking.html', methods=['GET', 'POST'])
def decision_making():
    if request.method == 'POST':
        session['decision_making'] = request.form.to_dict(flat=False)
        print("Decision Making Data:", session['decision_making'])
        return jsonify({"message": "Data received", "data": session['decision_making']})
    return render_template('decisionmaking.html')

@app.route('/planningstrategizing.html', methods=['GET', 'POST'])
def planning_strategizing():
    if request.method == 'POST':
        session['planning_strategizing'] = request.form.to_dict(flat=False)
        print("Planning and Strategizing Data:", session['planning_strategizing'])
        return jsonify({"message": "Data received", "data": session['planning_strategizing']})
    return render_template('planningstrategizing.html')

@app.route('/leaders.html', methods=['GET', 'POST'])
def leaders():
    if request.method == 'POST':
        session['leaders'] = request.form.to_dict(flat=False)
        print("Leaders Data:", session['leaders'])
        return jsonify({"message": "Data received", "data": session['leaders']})
    return render_template('leaders.html')

@app.route('/interactionstyles.html', methods=['GET', 'POST'])
def interaction_styles():
    if request.method == 'POST':
        session['interaction_styles'] = request.form.to_dict(flat=False)
        print("Interaction Styles Data:", session['interaction_styles'])
        return jsonify({"message": "Data received", "data": session['interaction_styles']})
    return render_template('interactionstyles.html')

@app.route('/socialboundaries.html', methods=['GET', 'POST'])
def social_boundaries():
    if request.method == 'POST':
        session['social_boundaries'] = request.form.to_dict(flat=False)
        print("Social Boundaries Data:", session['social_boundaries'])
        return jsonify({"message": "Data received", "data": session['social_boundaries']})
    return render_template('socialboundaries.html')

@app.route('/fieldnotes.html', methods=['GET', 'POST'])
def field_notes():
    if request.method == 'POST':
        session['field_notes'] = request.form.to_dict(flat=False)
        print("Field Notes Data:", session['field_notes'])
        return jsonify({"message": "Data received", "data": session['field_notes']})
    return render_template('fieldnotes.html')
# @app.route('/socialboundaries.html', methods=['GET', 'POST'])
# def social_boundaries():
#     if request.method == 'POST':
#         session['interaction_styles'] = request.form.to_dict()
#         return redirect(url_for('field_notes'))
#     return render_template('socialboundaries.html')

# @app.route('/fieldnotes.html', methods=['GET', 'POST'])
# def field_notes():
#     if request.method == 'POST':
#         session['field_notes'] = request.form.to_dict()

#         # Combine all data from the session into a single JSON document
#         final_data = {
#             "convening_basics": session.get('convening_basics'),
#             "convening_formats_and_spaces": session.get('convening_formats_and_spaces'),
#             "space_photos": session.get('space_photos'),
#             "times_and_counts": session.get('times_and_counts'),
#             "procedures_and_norms": session.get('procedures_and_norms'),
#             "activities": session.get('activities'),
#             "organizing_and_mobilizing": session.get('organizing_and_mobilizing'),
#             "public_sphere": session.get('public_sphere'),
#             "decision_making": session.get('decision_making'),
#             "planning_strategizing": session.get('planning_strategizing'),
#             "leaders": session.get('leaders'),
#             "interaction_styles": session.get('interaction_styles'),
#             "social_boundaries": session.get('social_boundaries'),
#             "field_notes": session.get('field_notes')

#         }

#         # Save to MongoDB
#         collection.insert_one(final_data)
        
#         # Clear session after saving
#         session.clear()

#     return render_template('fieldnotes.html')

@app.route("/")
def home():
    return render_template("index.html")  # This will load your main HTML page

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)
