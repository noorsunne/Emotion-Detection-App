import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load clean CSV
df = pd.read_csv("emotions.csv")
print("📊 Sample Data:")
print(df.head())

# Feature Extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])  # input: text
y = df['emotion']                         # label: emotion

# Train the model
model = MultinomialNB()
model.fit(X, y)

# Predict loop
while True:
    sentence = input("💬 Enter a sentence (or 'stop' to quit): ")
    if sentence.lower() == 'stop':
        print("👋 Exiting...")
        break

    input_vec = vectorizer.transform([sentence])
    prediction = model.predict(input_vec)
    print("🧠 Detected Emotion:", prediction[0])
