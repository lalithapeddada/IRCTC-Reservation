from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure MySQL URI (replace with your own credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/railway_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database object
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.Enum('admin', 'user'), nullable=False)

# Define the Train model
class Train(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    source = db.Column(db.String(80), nullable=False)
    destination = db.Column(db.String(80), nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    train_id = db.Column(db.Integer, db.ForeignKey('train.id'), nullable=False)
    seats_booked = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', backref=db.backref('bookings', lazy=True))
    train = db.relationship('Train', backref=db.backref('bookings', lazy=True))


# Route to register a user
@app.route('/register', methods=['POST'])
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Check if username already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({"message": "Username already exists"}), 400

    # If username is available, create a new user
    new_user = User(username=data['username'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201


# Route to log in a user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/add_train', methods=['POST'])
def add_train():
    data = request.get_json()  # Get the data from the request body
    # Create a new Train object
    new_train = Train(
        name=data['name'],
        source=data['source'],
        destination=data['destination'],
        total_seats=data['total_seats'],
        available_seats=data['available_seats']
    )
    # Add the new train to the database and commit the session
    db.session.add(new_train)
    db.session.commit()
    return jsonify({"message": "Train added successfully"}), 201


# Route to view train availability
@app.route('/trains', methods=['GET'])
def get_trains():
    source = request.args.get('source')
    destination = request.args.get('destination')
    trains = Train.query.filter_by(source=source, destination=destination).all()
    result = []
    for train in trains:
        result.append({
            "id": train.id,
            "name": train.name,
            "available_seats": train.available_seats
        })
    return jsonify(result)

# Route to book a seat
@app.route('/book', methods=['POST'])
def book_seat():
    data = request.get_json()
    train = Train.query.get(data['train_id'])
    if train and train.available_seats >= data['seats_booked']:
        new_booking = Booking(user_id=data['user_id'], train_id=data['train_id'], seats_booked=data['seats_booked'])
        train.available_seats -= data['seats_booked']
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking successful"})
    return jsonify({"message": "Not enough seats available"}), 400

@app.route('/')
def home():
    return "Welcome to the Railway Reservation System!"

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
