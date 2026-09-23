import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)

    response_dict = {
        'anger' : 'None',
        'disgust' : 'None',
        'fear' : 'None',
        'joy' : 'None',
        'sadness' : 'None',
        'dominant_emotion' : 'None'
    }

    if response.status_code == 200 :
        formatted_response = json.loads(response.text)
        
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        response_dict = {
            'anger' : anger_score,
            'disgust' : disgust_score,
            'fear' : fear_score,
            'joy' : joy_score,
            'sadness' : sadness_score
        }
        dominant_key = max(response_dict, key=response_dict.get)
        response_dict['dominant_emotion'] = dominant_key 
    
    return response_dict
   
  
