import requests, json

def emotion_detector(text_to_analyze):
    
    # request config
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": { "text": text_to_analyze }}

    # request to watson api
    response = requests.post(url, json = input_json, headers=header)

    # test status code
    if response.status_code == 400:
        return  {"anger" : None, 
                 "disgust" : None,
                 "fear" : None,
                 "joy" : None,
                 "sadness" : None,
                 "dominant_emotion" : None}

    # convert response to dictionary
    dict_response = json.loads(response.text)
    
    # dictionary for emotions only
    emotions = dict_response["emotionPredictions"][0]["emotion"]

    # find the highest emotion value and grab the key
    domEmotion = max(emotions, key=emotions.get)

    # add the dominant emotion to the emotions dict
    emotions["dominant_emotion"] = domEmotion

    return emotions
