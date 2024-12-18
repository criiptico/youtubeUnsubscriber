# Note: put each class in its own file and include ConnectDatabase and YouTube_API in the main file as objects
# Also note: you can run both ConnectDatabase and YouTube_API objects as async so it'd be faster
    # How?... This is a question for another day.



# Only a single ConnectDatabase object is neccessary for this app
# In the future this needs to be inside of the topic modeling function so that it can be assigned categories, but I'll worry about that when I get to it.
class ConnectDatabase(): # This is meant to abstract the actual sql code that is happening way under the hood.
    # Key:
    # element -> channel name, sub count, things about the channel you're subscribed to
    # keyword -> value of the channel name, value of the sub count, value about the elements of the channels you're subscribed to
    
    def __init__(self) -> None:
        self.url = "" # To connect with the remote database

    # Passing user_info to createt the user table with
    def create_user_table(self, user_info):
        pass

    # Passing element to specify which entry's element you want to refer to when you want to refer an entry
    # Passing keyword to specify the keyword that the element needs to have to refer it
    def update_user_entry(self, element, keyword):
        pass

    # Passing element to specify which entry's element you want to refer to when you want to refer an entry
    # Passing keyword to specify the keyword that the element needs to have to refer it
    def delete_user_entry(self, element, keyword):
        pass

    # Deletes a table. Must specify which table since the sql code is generally the same. (The user can opt to delete their profile if they'd like to.)
    def delete_whole_table(self, table, sql_statement, params):
        pass


    # Passing the subscriptions to create the subscription table with
    def create_subscription_table(self, subscriptions):
        pass
    
    # Passing element to specify the element you want to order something in the table by (for example a channel name and sub count)
    # Passing order_by to specify if you'd like to order in ascending or descending order
    def get_order(self, element, order_by): # Returns the names or all relevant subscriptions data
        pass

    # def get_group(): # Will be implemented in the topic modeling sprint
    #     pass

    # Passing element to specify which entry's element you want to refer to when you want to refer an entry
    # Passing keyword to specify the keyword that the element needs to have to refer it
    def delete_subscription_entry(self, element, keyword):
        pass

    # Passing element to specify which entry's element you want to refer to when you want to refer an entry
    # Passing keyword to specify the keyword that the element needs to have to refer it
    def insert_subscription_entry(self, element, keyword):
        pass
    

    



# Only a SINGLE YouTube_API object will be made to actively communicate with the youtube api and implicitly with the google api
class YouTube_API(): # This is the class that exclusively communicates with the YouTube API
    # The point is to make this generic so that I can change each input that's there every time a request is made.
    
    def __init__(self, authorization_code, client_secret_location):
        self.authorization_code = authorization_code
        self.client_secret_location = client_secret_location

        self.access_token = ""
        self.refresh_token = ""
        self.access_token_expires_in = -1 # Seconds
        self.access_token_retrieved_at = -1 # Use current time to get seconds and compare with expires in

        self._google_api = GoogleOAuth2_API(authorization_code, client_secret_location)

        # ~~~ Will create a separate class outside of the YouTube_API class so that it can be used when data doesn't need to be retrieved from the YouTube API
            ##### self._user_db = # Need to create a class that establishes a connection with the remote database. | Request the user's channel info and use the returned id as the id in the remote database 

    def request(self, method, url, parameters, headers):
        if method == "GET":
            return self._get_data(url, parameters, headers)
        elif method == "POST":
            return self._post_data(url, parameters, headers)
        elif method == "DELETE": # <---- Review what the method to send a delete request on something is
            return self._delete_data(url, parameters, headers)
        else:
            raise ValueError("[YouTube_API] Invalid HTTP Method Provided")
        
    def _get_data(self, url, parameters, headers):
        pass

    def _post_data(self, url, parameters, headers):
        pass

    def _delete_data(self, url, parameters, headers): # In the future add an insert data function.
        pass    

    # def get_user_info():
    #     url = "https://www.googleapis.com/youtube/v3/channels"
    #     parameters = {
    #         'part': "snippet,contentDetails,statistics",
    #         'mine': 'true',
    #     }
    #     headers = {
    #         'Authorization': f"Bearer {ACCESS_TOKEN}"
    #     }

class GoogleOAuth2_API(): # Might need to be initialized in this whole program and defined in another file since it needs to 
    def __init__(self, authorization_code, client_secret_location):
        self.auth_code = authorization_code
        self.client_secret_loc = client_secret_location
    
    def get_tokens(self): # Must return a dictionary with values with the initial tokens
        pass

    def validate_tokens(self): # Must return a dictionary with values
        pass