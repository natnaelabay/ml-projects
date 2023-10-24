from flask import Flask,request,jsonify
from torch_utils import get_prediction,transform_image
from validation import isValidFile
# from flask_ngrok import run_with_ngrok
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# run_with_ngrok(app)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

classConversion = {
    0 : "Covid",
    1 : "Normal",
    2 : "Pneumonia"
}

@app.route('/test',methods=['POST'])
def test():
    return "Normal"

@app.route('/classify',methods=['POST'])
# @cross_origin()
def predict():
    if request.method == "POST":
        file = request.files.get('file')
        validate = isValidFile(file)
        if validate:
            return jsonify({'error' : validate})

        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)      
	        # print("Result" + classConversion[prediction.item())
            print("Result: " + classConversion[prediction.item()])
            data = {"prediction" : classConversion[prediction.item()]}
            return jsonify(data)
        except:
            return jsonify({'error' : 'Error during prediction'})

    return jsonify({'error' : 'Invalid request'})
    
if __name__ == "__main__":
  app.run()
