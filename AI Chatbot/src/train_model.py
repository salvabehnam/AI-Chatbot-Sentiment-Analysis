import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/sentiment_data.csv")

X_train, X_test, y_train, y_test = train_test_split(df["review"], df["sentiment"], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(ngram_range=(1, 3), stop_words="english", min_df=1, max_df=0.85, sublinear_tf=True)
X_train_tfidf = vectorizer.fit_transform(X_train)

model = LogisticRegression(max_iter=800, solver="lbfgs")
model.fit(X_train_tfidf, y_train)

joblib.dump(model, "models/sentiment_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Model trained and saved!")
