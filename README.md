# Intel® HealthAI - Personal Health Companion

Intel® HealthAI is a real-time biometric monitoring and mental health analysis application leveraging artificial intelligence. This project is built with Streamlit and includes three primary functionalities:

1. **Simulated Biometric Monitoring**
2. **Mental Health Sentiment Analysis**
3. **Personalized Health Recommendations**

---

## Features

### 1. Biometric Monitoring
Simulates real-time health metrics such as:
- **Heart Rate (BPM):** Randomly generated values between 60 and 100.
- **Stress Level:** A simulated stress level between 0 and 1.
- **Sleep Quality:** Simulated quality of sleep between 50% and 100%.

### 2. Mental Health Analysis
Analyzes user input (feelings/thoughts) using a pre-trained sentiment analysis model (`distilbert-base-uncased`) from the Hugging Face library. It identifies:
- **Sentiment (Positive/Negative/Neutral)**
- **Confidence Score**

### 3. Personalized Recommendations
Provides health-related recommendations based on biometric data:
- Elevated heart rate warnings.
- Stress level coping strategies.
- General health encouragement for normal metrics.

---

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Required libraries:
  - `streamlit`
  - `numpy`
  - `transformers`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/aathi-star/Personal-Health-Companion.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the Streamlit app:
   ```bash
   streamlit run intel.py
   ```
2. Access the app in your browser at `http://localhost:8501`.

---

## How It Works

### Simulated Biometric Monitoring
- Click the **Start Monitoring** button.
- View real-time simulated health metrics (heart rate, stress level, sleep quality).

### Sentiment Analysis
- Enter your thoughts in the text area under **Mental Health Analysis**.
- Click the **Analyze Sentiment** button to analyze and view your mental health sentiment.

### Personalized Recommendations
- After biometric monitoring, click the **Get Personalized Recommendations** button.
- Recommendations will be based on your monitored heart rate and stress level.

---

## Notes
- **Simulated Data:** Biometric data is simulated for demonstration purposes. For real-world applications, integrate live data from wearable devices.
- **Model:** The sentiment analysis uses the pre-trained `distilbert-base-uncased` model from Hugging Face.

---

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## Acknowledgments
- **Streamlit:** For creating a user-friendly framework for building web applications.
- **Hugging Face:** For providing pre-trained NLP models.
