# Python program to find current  
# weather details of any city 
# using openweathermap api 
# Following guide: https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

# import required modules
#json is already installed with 3.8
import requests, json, re

def checkWeather():
    # Enter your API key here
    api_key = "4a67c29e55e85ca95c17b4240e7fb9a4"

    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Give city name 
    city_name = input("Enter city name : ") 

    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

    # get method of requests module 
    # return response object 
    response = requests.get(complete_url)
    #print (response)

    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    #print (x)

    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 

        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
        
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"]

        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 

        # print following values 
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description))

        if(is_word_in_text("rain", weather_description)):
            print (" yes")
            #Send gmail to me
        else:
            #don't send nothing
            print( "no")

    else: 
        print(" City Not Found ")   


#https://stackoverflow.com/a/45587730
def is_word_in_text(word, text):
    """
    Check if a word is in a text.

    Parameters
    ----------
    word : str
    text : str

    Returns
    -------
    bool : True if word is in text, otherwise False.

    Examples
    --------
    >>> is_word_in_text("Python", "python is awesome.")
    True

    >>> is_word_in_text("Python", "camelCase is pythonic.")
    False

    >>> is_word_in_text("Python", "At the end is Python")
    True
    """
    pattern = r'(^|[^\w]){}([^\w]|$)'.format(word)
    pattern = re.compile(pattern, re.IGNORECASE)
    matches = re.search(pattern, text)
    return bool(matches)

def main():
    checkWeather()

if __name__ == "__main__":
    main()