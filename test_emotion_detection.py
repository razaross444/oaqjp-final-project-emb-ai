from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_detector(self):

        # test case for 'joy'
        result_1 = emotion_detector("I am glad this happened")
        self.assertTrue(result_1["dominant_emotion"] == "joy")

        # test case for 'anger'
        result_2 = emotion_detector("I am really mad about this")
        self.assertTrue(result_2["dominant_emotion"] == "anger")

        #test case for 'disgust'
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertTrue(result_3["dominant_emotion"] == "disgust")

        #test case for 'sadness'
        result_4 = emotion_detector("I am so sad about this")
        self.assertTrue(result_4["dominant_emotion"] == "sadness")

        #test case for 'fear'
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertTrue(result_5["dominant_emotion"] == "fear")

unittest.main
