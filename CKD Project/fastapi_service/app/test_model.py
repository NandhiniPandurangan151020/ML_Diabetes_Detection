# import pickle
# import numpy as np

# # Load your saved model and scaler
# classifier = pickle.load(open('../../Finalized_model.sav', 'rb'))
# scaler = pickle.load(open('../../scaler.sav', 'rb'))

# # Sample input data — replace with values you want to test
# sample = np.array([240, 100, 30, 100, 28.5, 0.987, 6, 50])

# # Scale the input
# sample_scaled = scaler.transform(sample.reshape(1, -1))

# # Make prediction
# prediction = classifier.predict(sample_scaled)

# print("Scaled Input:", sample_scaled)
# print("Prediction:", prediction)


import joblib
import numpy as np

pipeline = joblib.load('../../model.pkl')  # the pipeline with scaler+model

sample = np.array([240, 100, 30, 100, 28.5, 0.987, 6, 50]).reshape(1, -1)

prediction = pipeline.predict(sample)

print("Prediction:", prediction)
