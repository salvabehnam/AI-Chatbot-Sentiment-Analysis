# 🗣️ Sentiment Analysis Chatbot using Machine Learning
This project builds a **machine learning chatbot** that classifies text into **Positive 😊, Negative 😞, or Neutral 😐** sentiment.  
We use **TF-IDF Vectorization** and **Logistic Regression** to train the model on **real-world sentiment data**.

## 📌 Features
- **Three-Class Sentiment Analysis (Positive, Negative, Neutral)**
- **Pre-Trained Logistic Regression Model**
- **Custom Dataset with Strong Sentiment Reinforcement**
- **Modular Code (Dataset, Chatbot)**

## 📂 Project Structure
    AI_Chatbot/
    ├── README.md                   
    ├── requirements.txt            
    │
    ├── data/                        
    │   ├── sentiment_data.csv      
    │
    ├── models/                      
    │   ├── sentiment_model.pkl      # Pre-Trained Model
    │   ├── vectorizer.pkl           # TF-IDF Vectorizer
    │
    ├── src/                         
    │   ├── chatbot.py               
    │
    ├── generate_csv.py            

## 📊 Dataset
- The dataset used is **custom-built sentiment data**.
- Users must generate the dataset by running:
  
      python generate_csv.py
  
## 🚀 Installation & Usage
  🔹 1️⃣ Clone the Repository
    
      git clone https://github.com/YOUR_GITHUB/AI_Chatbot.git
      cd AI_Chatbot
      
  🔹 2️⃣ Install Dependencies
    
      pip install -r requirements.txt
  
  🔹 3️⃣ Generate Dataset
      
      python generate_csv.py

  🔹 4️⃣ Run the Chatbot  
  Users can interact with the chatbot:
  
      python src/chatbot.py

## 🔥 Results & Performance
  - The chatbot correctly identifies **positive, negative, and neutral sentiments** based on user input.
  - It provides a **confidence score** for each prediction, helping users understand how certain the model is.
  - The dataset includes a mix of **strong and mixed sentiments**, improving classification accuracy.
  - Works well with **common phrases** but may have some difficulty with **sarcasm and complex expressions**.


## ✨ Technologies Used
- Python
- Scikit-learn
- Pandas & NumPy
- Joblib (for model saving & loading)
