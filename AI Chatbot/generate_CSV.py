import pandas as pd
import os

# Ensure the "data" directory exists
os.makedirs("data", exist_ok=True)

data = {
    "review": [
        "I love this movie, it was amazing!", 
        "Worst film ever, completely boring.", 
        "Great acting, fantastic story.", 
        "Terrible acting, waste of time.", 
        "Absolutely fantastic experience!", 
        "Horrible plot, I couldn't finish it.", 
        "Brilliant cinematography!", 
        "Bad film.", 
        "Good one.", 
        "Disappointing movie.", 
        "I hated everything about it.", 
        "Loved the characters and plot.", 
        "Awful script!", 
        "No good at all.", 
        "Perfect movie.", 
        "Terrible.", 
        "Excellent!", 
        "Bad!", 
        "Good!", 
        "Boring.", 
        "Amazing!", 
        "Outstanding performance!", 
        "Not bad, actually quite good.", 
        "Bad but also good.", 
        "Good but not bad.", 
        "Not great, not terrible.", 
        "Could have been better, but not bad overall.", 
        "Not the best, but not bad either.", 
        "Good movie, just a few issues.", 
        "So so.", 
        "Meh.", 
        "Don't know how I feel.", 
        "It's okay, not amazing but not bad.", 
        "Neither good nor bad.", 
        "Mediocre experience.", 
        "Mixed feelings.", 
        "It was alright.", 
        "Fine, not great.", 
        "Nothing special.", 
        "Indifferent.", 
        "Absolutely fantastic, best movie ever!", 
        "The worst experience of my life!", 
        "Flawless execution, incredible performances!", 
        "Horrific film, nothing redeemable about it.", 
        "Bad!", "So bad!", "Really bad!", "Absolutely bad!", "Terrible!", "Completely horrible!", 
        "Horrible!", "Horrific!", "Worst thing ever!", "Disgusting!"
    ],
    "sentiment": [
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 
        1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
        1, 0, 1, 0, 0, 0, 0, 0, 0, 0
    ]
}

# Debugging: Print lengths before creating DataFrame
print(f"Total reviews: {len(data['review'])}")
print(f"Total sentiment labels: {len(data['sentiment'])}")

# Ensure both lists have the same length
min_length = min(len(data["review"]), len(data["sentiment"]))
data["review"] = data["review"][:min_length]
data["sentiment"] = data["sentiment"][:min_length]

df = pd.DataFrame(data)
csv_path = "data/sentiment_data.csv"
df.to_csv(csv_path, index=False)

print(f"CSV file created successfully: {csv_path}")
