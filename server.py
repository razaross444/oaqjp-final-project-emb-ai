"""
This module contains Flask api endpoints
to serve files and data pertaining to 
Emotion Detection

"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/")
def index():
    """
    Index
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotions():
    """
    GET endpoint that expects 'textToAnalyze'
    string and returns emotion metrics from
    Watson 
    """
    # get text from querystring
    text_to_analyze = request.args.get("textToAnalyze")

    # call into service for analysis
    analysis = emotion_detector(text_to_analyze)

    if analysis['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    message = f"""For the given statement,
                the system response is 
                'anger': {analysis['anger']},
                'disgust': {analysis['disgust']},
                'fear': {analysis['fear']},
                'joy': {analysis['joy']} and 
                'sadness': {analysis['sadness']}.
                The dominant emotion is 
                {analysis['dominant_emotion']}."""

    return message

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
