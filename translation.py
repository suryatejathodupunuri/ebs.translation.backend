from flask import Flask,request,jsonify
from flask_cors import CORS
import requests
app=Flask(__name__)
CORS(app)
@app.route('/api/test')

def test():
    return "Backend running successfully."
        
@app.route('/api/translation', methods=['POST'])
def translate():
      try:
        data = request.json
        src=data['src']
        tar=data['tar']
        inp=data['inp']
        payload = {
            
    "pipelineTasks": [
        {
            "taskType": "translation",
            "config": {
                "language": {
                    "sourceLanguage": src,
                    "targetLanguage": tar
                },
                "serviceId": "ai4bharat/indictrans-v2-all-gpu--t4"
            }
        }
    ],
    "inputData": {
        "input": [
            {
                "source": inp
            }
        ]
    }
}
        
        api_url = "https://dhruva-api.bhashini.gov.in/services/inference/pipeline"
        headers = {
        "Authorization": "oq49byMkhuyCQ8AGP9HCfh2-AXtEJ5nXDCRMVxadKcNshL67TDmjjUuIT5I0rvQd",
        "Content-Type": "application/json"
    }
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            target = response_data['pipelineResponse'][0]['output'][0]['target']
            return jsonify({'output':target},{'status':'SUCCESS'}),200
        else:
            return jsonify({"error": "Failed to fetch translation from the API"}), response.status_code
      except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)