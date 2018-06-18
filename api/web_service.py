from flask import Flask
from flask import jsonify

from generator.creative_generator import generate_personalized_creative, generate_personalized_creatives

app = Flask(__name__)


@app.route("/")
def whoami():
    return "Welcome to Rokt-a-thon! We are Team ROKTMind!"


@app.route('/roktmind/candidate_creatives/<int:userid>/<int:creativeid>/<int:memberid>')
def generate_creatives(userid, creativeid, memberid):
    return jsonify(generate_personalized_creatives(userid, creativeid, memberid))


@app.route('/roktmind/optimal_creative/<int:userid>/<int:creativeid>/<int:memberid>')
def generate_creative(userid, creativeid, memberid):
    return jsonify(generate_personalized_creative(userid, creativeid, memberid))


if __name__ == '__main__':
    app.secret_key = 'ROCKMind'
    app.run(debug=True)
