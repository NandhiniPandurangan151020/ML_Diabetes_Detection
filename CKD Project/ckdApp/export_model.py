import pickle
import joblib
from sklearn.pipeline import Pipeline

# Load the saved scaler and model
scaler = pickle.load(open("scaler.sav", "rb"))
classifier = pickle.load(open("Finalized_model.sav", "rb"))

# Combine them into a pipeline
pipeline = Pipeline([
    ('scaler', scaler),
    ('classifier', classifier)
])

# Save the pipeline as model.pkl
joblib.dump(pipeline, "model.pkl")

print(" Pipeline saved as model.pkl")
