from flask import Flask, Response, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import json
import pyshorteners
from dotenv import load_dotenv
import os
import autoBuy

load_dotenv()


app = Flask(__name__)

account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
twilio_num = os.environ["TWILIO_NUM"]
receiver = os.environ["RECIEVER"]

client = Client(account_sid, auth_token)
productRecords = {}

def shortenURL(url):
    
    #Replace url already in records

    #TinyURL shortener service
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(url)
    
    return short_url

@app.route("/registeralert", methods=['POST'])
def register_alert():
    name = request.data
    res_dict = json.loads(name.decode('utf-8'))
    name = res_dict["product-name"]
    site = res_dict["website-name"]
    link = shortenURL(res_dict["item-link"])


    strike_price = res_dict["buy-price"]
    productRecords[link] = {"platform": site, "name": name, "price": strike_price}

    # Serializing json
    json_object = json.dumps(productRecords, indent=4)
    
    # Writing to sample.json
    with open("productRecords.json", "w") as outfile:
        outfile.write(json_object)

    message = client.messages.create(
                              body=f"""Hi! I'm Shop Buddy! You have just set an alert for {name} 
                              \nLink: {link}
                              \nDesired Price: {strike_price}
                              """,
                              from_= twilio_num,
                              to=receiver
    )

    print(productRecords)
    return Response(status=200, mimetype="text/xml")

@app.route("/sms", methods=['POST'])
def sms_replies():
    """Respond to incoming calls with a SMS message."""


    number = request.form["From"]
    messageBody = request.form["Body"]
    
    # Start our TwiML response
    response = MessagingResponse()

    with open('purchases.json') as db:
        purchases = json.load(db)

    if messageBody in purchases.keys():
        autoBuy.Mockbuy(purchases[messageBody])
        msg = response.message("Will do! Purchase will be made")
    else:
        msg = response.message("I'm sorry I didn't quite catch that")
    
    return Response(str(response), mimetype="text/xml")

@app.route("/tracking", methods=["GET", "POST"])
def getTracking():
    with open('productRecords.json') as db:
        tracking = json.load(db)
    
    jsonPacket = []
    for link, data in tracking.items():
        tmp = {"link": link}
        tmp = tmp | data
        jsonPacket.append(tmp) 
    
    jsonPacket = json.dumps(jsonPacket)
    return Response(response=jsonPacket, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)