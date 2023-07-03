from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if 'hello' in incoming_msg:
        msg.body('Hello! I am a chatbot. How can I assist you?')
        responded = True
    if 'wikipedia' in incoming_msg:
        msg.body('Wikipedia is a free online encyclopedia.')
        responded = True
    if not responded:
        msg.body('Sorry, I did not understand. Could you try again with a different phrase?')
    return str(resp)

if __name__ == "__main__":
    app.run()
