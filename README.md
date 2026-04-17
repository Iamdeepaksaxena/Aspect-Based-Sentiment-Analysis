# Aspect-Based-Sentiment-Analysis
>This project implements **Aspect-Based Sentiment Analysis (ABSA)** to identify sentiments toward specific aspects within text. Unlike traditional sentiment analysis, it provides fine-grained insights by classifying opinions at the aspect level.



---
<p align="center"> <img src="https://raw.githubusercontent.com/iamdeepaksaxena/Aspect-Based-Sentiment-Analysis/main/assets/image.png" width="600"> </p> 

<p align="center"> <img src="https://raw.githubusercontent.com/iamdeepaksaxena/Aspect-Based-Sentiment-Analysis/main/assets/image2.png" width="600"> </p>

🧩 Project Structure
project/
│
├── app.py
├── src/
│   └── main.py
│
└── templates/
    └── index.html

## 🚀 Features
- 🧠 Aspect-Based Sentiment Analysis (ABSA) using transformer models
- 🔍 Analyze sentiment for custom user-defined aspects
- 💬 Supports multiple aspects input (comma-separated)
- ⚡ Real-time sentiment prediction via Flask web app
- 📊 Displays negative, neutral, positive probabilities for each aspect
- 🌐 Also provides overall sentiment of the sentence 

---

## ⚙️ Installation

```
1️⃣ Clone the Repository 
git clone https://github.com/Iamdeepaksaxena/Aspect-Based-Sentiment-Analysis.git
2️⃣ Create a Virtual Environment
python -m venv venv
.\venv\Scripts\activate   # For Windows
3️⃣ Install Dependencies
pip install -r requirements.txt

🧩 Run the App
python src/app.py

```


## References
🧠 ABSA Model
🔗 https://huggingface.co/yangheng/deberta-v3-base-absa-v1.1
💬 Sentiment Analysis Model
🔗 https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment

