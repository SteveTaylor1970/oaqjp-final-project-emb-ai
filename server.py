"""
    Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
        This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the scores of different
        emotions for the provided text.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)

    output = "\'anger\': " + str(result['anger']) + ", "
    output = output + "\'disgust\': " + str(result['disgust']) + ", "
    output = output + "\'fear\': " + str(result['fear']) + ", "
    output = output + "\'joy\': " + str(result['joy']) + ", "
    output = output + "\'sadness\': " + str(result['sadness']) + ". "
    output = output + "The dominant emotion is: " + (result['dominant_emotion'])
    
    return "For the given statement, the system response is {}"\
    .format(output)
    
    
@app.route("/")
def render_index_page():
    """
        This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template('index.html')

if __name__ == "__main__":
    """
        This functions executes the flask app and deploys it on localhost:5000
    """
    app.run(host="0.0.0.0", port=5000)
