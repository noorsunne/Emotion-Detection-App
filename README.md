💬 Emotion Detection App
A simple machine learning-based emotion detection system built using Python. This app can predict the emotion behind a given sentence (like joy, sadness, anger, etc.) using a text classification model.

📁 Dataset
The model is trained on a custom dataset (train.txt) containing emotional sentences and their corresponding emotions (labels).

Example from dataset:

sql
Copy
Edit
i felt anger when at the end of a telephone call ; anger
The data is preprocessed and converted into a clean CSV format using pandas.

🧠 Technologies Used
Tool / Library	Purpose
Python	Programming Language
Pandas	Data Handling & Preprocessing
Scikit-learn	Machine Learning (Naive Bayes model)
CountVectorizer	Text Vectorization

🛠️ Features
Takes user input as a sentence.

Predicts the emotion from a set of trained categories.

CLI-based (Command Line Interface) — user types sentences directly.

Clean data preprocessing using pandas.

Currently being improved to add a GUI with Streamlit (coming soon 🚀).

🖥️ How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/emotion-detection-app.git
Install dependencies:

nginx
Copy
Edit
pip install pandas scikit-learn
Run the data converter (optional):

nginx
Copy
Edit
python convert.py
Run the emotion detector:

css
Copy
Edit
python main.py
📌 Example Output
less
Copy
Edit
💬 Enter a sentence (or 'stop' to quit): i feel very sad today
🧠 Detected Emotion: sadness
🔧 Future Plans
 CLI-based emotion detector

 Add Streamlit GUI (in progress 💻)

 Improve dataset and model accuracy

 Add support for Urdu & multilingual input

🧕 Created by
Noor – Passionate about using AI/ML to build emotionally intelligent apps 💖
