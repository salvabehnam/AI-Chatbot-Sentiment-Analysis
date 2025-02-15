import joblib
import numpy as np

model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def chatbot():
    print("Chatbot is running... Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        transformed_input = vectorizer.transform([user_input])
        prediction_probs = model.predict_proba(transformed_input)[0]
        prediction_class = np.argmax(prediction_probs)
        confidence = np.max(prediction_probs)

        if confidence < 0.28:
            prediction_class = 2

        if prediction_class == 1:
            sentiment = "Positive 😊"
        elif prediction_class == 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        print(f"Chatbot: {sentiment} (Confidence: {confidence:.2f})")

chatbot()
