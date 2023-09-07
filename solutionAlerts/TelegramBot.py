import telegram
import json

class TelegramBot:
    def __init__(self):
        settings = self.getUserSettings()
        self.TOKEN = settings.get("TOKEN")
        self.CHAT_ID = settings.get("CHAT_ID")
        self.bot = telegram.Bot(token=self.TOKEN)
        
    async def send_message(self, message):
        for id in self.CHAT_ID:
            await self.bot.send_message(chat_id=id, text=message)

    def getUserSettings(self): 
        with open('/home/adrillb/Desktop/TFG/Python/iot-solution/solutionAlerts/userSettingsTelegram.json', 'r') as json_file:
            return json.load(json_file)