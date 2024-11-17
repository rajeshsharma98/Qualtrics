from flask import Flask, render_template

app = Flask(__name__)

@app.route('/conveningbasics.html')
def convening_basics():
    return render_template('conveningbasics.html')


@app.route('/conveningformatsandspaces.html')
def convening_formats_and_spaces():
    return render_template('conveningformatsandspaces.html')

@app.route('/spacephotos.html')
def space_photos():
    return render_template('spacephotos.html')

@app.route('/timesandcounts.html')
def times_and_counts():
    return render_template('timesandcounts.html')

@app.route('/proceduresandnorms.html')
def procedures_and_norms():
    return render_template('proceduresandnorms.html')

@app.route('/activities.html')
def activities():
    return render_template('activities.html')

@app.route('/organizingandmobilizing.html')
def organizing_and_mobilizing():
    return render_template('organizingandmobilizing.html')

@app.route('/publicsphere.html')
def public_sphere():
    return render_template('publicsphere.html')

@app.route('/decisionmaking.html')
def decision_making():
    return render_template('decisionmaking.html')

@app.route('/planningstrategizing.html')
def planning_strategizing():
    return render_template('planningstrategizing.html')

@app.route('/leaders.html')
def leaders():
    return render_template('leaders.html')

@app.route('/interactionstyles.html')
def interaction_styles():
    return render_template('interactionstyles.html')

@app.route('/socialboundaries.html')
def social_boundaries():
    return render_template('socialboundaries.html')

@app.route('/fieldnotes.html')
def field_notes():
    return render_template('fieldnotes.html')

@app.route("/")
def home():
    return render_template("index.html")  # This will load your main HTML page

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)