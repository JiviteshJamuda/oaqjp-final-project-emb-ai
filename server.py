"""Importing modules"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Detector"""
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant = response["dominant_emotion"]

    # if the text given was empty and None was returned
    if dominant is None:
        return "Invalid text! Please try again!."

    # Output
    res = f"For the given statement, the system response is 'anger': {anger}, "
    res += f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
    res += f"The dominant emotion is <b>{dominant}</b>."
    return res

@app.route("/")
def render_index_page():
    """Render"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
