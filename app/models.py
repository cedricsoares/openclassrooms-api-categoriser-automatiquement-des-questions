from flask_sqlalchemy import SQLAlchemy
from .views import app

db = SQLAlchemy(app)

class Predictions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_text = db.Column(db.Text(), nullable=False)
    preprocessed_text = db.Column(db.Text(), nullable=False)
    vectorized_text = db.Column(db.Text(), nullable=False)
    predicted_tags = db.Column(db.String(255), nullable=False)

    def __init__(self,
                original_text,
                preprocessed_text,
                vectorized_text,
                predicted_tags):
        self.original_text = original_text
        self.preprocessed_text = preprocessed_text
        self.vectorized_text = vectorized_text
        self.predicted_tags = predicted_tags

    def __repr__(self):
        return f"<id {self.id}, text {self.original_text}, tags {self.predicted_tags}>"

db.create_all()