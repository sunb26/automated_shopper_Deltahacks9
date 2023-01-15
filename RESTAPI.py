from flask import Flask, Response, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)


@app.route("/registeralert", methods=['POST'])
def register_alert():
    name = request.form["From"]
    message = client.messages.create(
                              body=f'Hi {name}! You have created an alert for',
                              from_='',
                              to=''
                          )
    
    return Response()

@app.route("/sms", methods=['POST'])
def sms_replies():
    """Respond to incoming calls with a MMS message."""


    number = request.form["From"]
    message_body = request.form["Body"]

    # Start our TwiML response
    response = MessagingResponse()

    # Add a text message
    msg = response.message(number)
    return Response(str(response), mimetype="text/xml")


if __name__ == "__main__":
    app.run(debug=True)