import openai
import json

class IARequest:
    def __init__(self):
        self.key_info = self.getApiKey()
        openai.api_key = self.key_info.get("api-key")

        self.model_engine = "text-davinci-003"


    def chatGPT_request(self, prompt):            
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024
        )
        return response.choices[0].text.strip()

    def getApiKey(self):
        with open('/home/adrillb/Desktop/TFG/Python/iot-solution/IARequest/API-KEY.json', 'r') as json_file:
            return json.load(json_file)