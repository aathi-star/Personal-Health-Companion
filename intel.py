try:
    import os
    os.environ['KMP_DUPLICATE_LIB_OK']="TRUE"
    import streamlit as st
    import numpy as np
    from transformers import pipeline
    import time
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(f"Missing required module: {e.name}. Please install it using 'pip install {e.name}'.")

st.title("Intel® HealthAI - Personal Health Companion")
st.write("Real-time biometric monitoring and mental health analysis using AI")

# Section 1: Simulated Biometric Monitoring
heart_rate = None
stress_level = None
sleep_quality = None

def simulate_biometric_data():
    heart_rate = np.random.randint(60, 100)  # Simulated heart rate in BPM
    stress_level = np.random.uniform(0, 1)  # Stress level (0 to 1)
    sleep_quality = np.random.uniform(50, 100)  # Sleep quality (0 to 100%)
    return heart_rate, stress_level, sleep_quality

st.subheader("Biometric Monitoring")
if st.button("Start Monitoring"):
    with st.spinner("Collecting data..."):
        time.sleep(2)
        heart_rate, stress_level, sleep_quality = simulate_biometric_data()
    st.session_state['heart_rate'] = heart_rate
    st.session_state['stress_level'] = stress_level
    st.session_state['sleep_quality'] = sleep_quality
    st.success("Data Collected!")
    st.metric("Heart Rate (BPM)", heart_rate)
    st.metric("Stress Level", f"{stress_level:.2f}")
    st.metric("Sleep Quality (%)", f"{sleep_quality:.2f}")

# Section 2: Mental Health Analysis
def analyze_sentiment(user_input):
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased")
    return sentiment_pipeline(user_input)

st.subheader("Mental Health Analysis")
user_input = st.text_area("How are you feeling today?", placeholder="Share your thoughts...")
if st.button("Analyze Sentiment"):
    with st.spinner("Analyzing your response..."):
        sentiment = analyze_sentiment(user_input)
        st.success("Analysis Complete!")
        st.write("Sentiment:", sentiment[0]["label"])
        st.write("Confidence:", f"{sentiment[0]['score']:.2f}")

# Section 3: Recommendations
def generate_recommendations(heart_rate, stress_level):
    recommendations = []
    if heart_rate > 90:
        recommendations.append("Your heart rate is elevated. Consider taking a short break or practicing deep breathing exercises.")
    if stress_level > 0.7:
        recommendations.append("High stress detected. Engage in a mindfulness activity or a quick relaxation session.")
    if not recommendations:
        recommendations.append("All metrics are within healthy ranges. Keep up the good work!")
    return recommendations

if st.button("Get Personalized Recommendations"):
    if 'heart_rate' in st.session_state and 'stress_level' in st.session_state:
        recommendations = generate_recommendations(st.session_state['heart_rate'], st.session_state['stress_level'])
        st.subheader("Recommendations")
        for rec in recommendations:
            st.write("-", rec)
    else:
        st.error("Please start biometric monitoring first.")

# Note: This code is a starting point. The biometric data generation is simulated. For real-world applications, 
# progressing to integrate APIs or SDKs for wearable devices to fetch live biometric data.
