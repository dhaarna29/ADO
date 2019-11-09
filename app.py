from flask import Flask, request, jsonify
import requests
import base64
import io
from google.cloud import vision
from google.cloud.vision import types
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='F:/WebD/react/AwesomeProject/api-test-5195f987539c.json'


app = Flask(__name__)
url="https://vision.googleapis.com/v1/images:annotate"
api_key='AIzaSyA_1Oro_J8ndG62rzAZvhPQsmTuQWTrMXM'

@app.route('/image/', methods=['POST'])
def get_image():
    client = vision.ImageAnnotatorClient()
    with io.open('images.jpg', 'rb') as image_file1:
        content = image_file1.read()
    content_image = types.Image(content=content)
    response = client.document_text_detection(image=content_image)
    document = response.full_text_annotation
    print(document)
    return {}
    # img=request.data
    # content = img
    # img_request = {"requests": [{
    #     'image': {'content': content},
    #     'features': [{
    #         'type': 'TEXT_DETECTION',
    #         'maxResults': 20
    #     }]
    # }]
    # }
    # response = requests.post(url,
    #                          data=json.dumps(img_request),
    #                          params={'key': api_key},
    #                          headers={'Content-Type': 'application/json'})
    # print(response)
    # for idx, resp in enumerate(response.json()['responses']):
    #     print(resp)
    # return response.text

def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)