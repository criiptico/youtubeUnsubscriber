from flask import Flask, request, abort, jsonify
from flask_restx import Api, Resource, fields
from flask_cors import CORS
import urllib.parse
import requests
import json
import time


app = Flask(__name__)
api = Api(app, version='1.0', title='FilterYTSubs API',
    description='The back end system of FilterYTSubs.',
)

CORS(app, origins=["http://localhost:5173"])

auth_ns = api.namespace('login-auth-code', description='filter-yt-subs-api-authentication-code')
ops_ns = api.namespace('filter-yt-api', description='filter-yt-subs-api-operations')

global ACCESS_TOKEN, REFRESH_TOKEN, ACCESS_TOKEN_EXPIRES_IN, ACCESS_TOKEN_RETRIEVED_AT

@auth_ns.route('/', strict_slashes=False)
class LoggingIn(Resource):
    def post(self):
        data = request.json
        # print("Received data:", data)
        code = data.get("code")
        # print("Authentication code:", code)
        
        # print("Exchanging Authorization Code for Access and Refresh Code")
        cs_f = open("client_secret.json")
        client_secret = json.load(cs_f)
        cs_f.close()

        to_exchange = {
            'code': code,
            'client_id': client_secret['web']['client_id'],
            'client_secret': client_secret['web']['client_secret'],
            'redirect_uri': client_secret['web']['redirect_uris'][0],
            'grant_type': 'authorization_code',
        }
        # print(to_exchange)

        try:
            url = client_secret['web']['token_uri']
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
            }
            parameters = to_exchange
            exchange_response = requests.post(url=url, headers=headers, params=parameters) # the response is all of the http file
            exchange_response = exchange_response.json() # parses the text section of the http response

            with open("exchange_response.json", "w") as file:
                file = open("exchange_response.json", "w")
                json.dump(exchange_response, file)
                file.close()

            ACCESS_TOKEN_RETRIEVED_AT = int(time.time()) + 1
            ACCESS_TOKEN = exchange_response['access_token']
            REFRESH_TOKEN = exchange_response['refresh_token']
            ACCESS_TOKEN_EXPIRES_IN = exchange_response['expires_in']

            print("The access code was retrieved at:", ACCESS_TOKEN_RETRIEVED_AT)
            print("The access code expires at:", ACCESS_TOKEN_EXPIRES_IN)

        except Exception as e:
            print(f"Error during token exchange: {e}")
            abort(500, "An error occurred during token exchange.")

        # Test different ways to request data from each endpoint.
            # Note: Find the documentation and link it in a markdown somewhere on here.

        # Put the code flow that's below into a function, then call the function.
        url = "https://www.googleapis.com/youtube/v3/channels"
        parameters = {
            'part': "snippet,contentDetails,statistics",
            'mine': 'true',
        }
        headers = {
            'Authorization': f"Bearer {ACCESS_TOKEN}",
            'Accept': 'application/json',
        }

        youtube_response = None
        try:
            youtube_response = requests.get(url=url, headers=headers, params=parameters) # Is this received as a json file?
            youtube_response = youtube_response.json() # .json() converts the response into json
        except:
            print("Error: Cannot process get request to youtube api")

        if youtube_response is None:
            print("no data received from:", url)
        else:
            with open("youtube_response.json", "w") as f:
                f = open("youtube_response.json", "w")
                json.dump(youtube_response, f)
                f.close()
            print(youtube_response)

        # Use id to update and retrieve data from the database <- ideally the next step

        return jsonify({
            "title": "Logging in: Basic User Data",
            "name": youtube_response['items'][0]['snippet']['title'],
            "id": youtube_response['items'][0]['id'],
            "picture": youtube_response['items'][0]['snippet']['thumbnails']['default'], # This returns a json object, check if it works
        })

# @ops_ns.route('/')
# class ManageSubs(Resource):
#     def get(self):
#         print("Hi")
#         if LOGGED_IN:
#             return {'response' : 'Logged in!'}, 201
#         else:
#             return {'response' : 'Not Logged in!'}, 201
        
#     def post(self):
#         print("Bye")
#         return {'wait' : 'uh oh...'}

if __name__ == '__main__':
    app.run(debug=True)