from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random



app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search_cafe_by_location():
    query_location = request.args.get("loc")

    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    cafes = result.scalars().all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def patch_new_price(cafe_id):
    # cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    cafe_to_update = db.session.get(Cafe, cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})

    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404


## HTTP DELETE - Delete Record
@app.route("/update-closed/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    cafe_to_update = db.session.get(Cafe, cafe_id)
    user_api_key = request.args.get("api-key")
    if not user_api_key == "TopSecretAPIKey":
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key."), 403
    elif not cafe_to_update:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404
    else:
        db.session.delete(cafe_to_update)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted cafe from database."})


if __name__ == '__main__':
    app.run(debug=True)
