# import requests
#
# def extract_coordinates_from_google_maps_url(google_maps_url, api_key):
    #Make a request to the Geocoding API
    # response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?place_id={google_maps_url}&key={api_key}')
    #
    #Parse the response
    # data = response.json()
    # print(data)
    # if data['status'] == 'OK':
    #     location = data['results'][0]['geometry']['location']
    #     latitude = location['lat']
    #     longitude = location['lng']
    #     return latitude, longitude
    # else:
    #     print(f"Error: {data['status']}")
    #     return None
#
#Example usage
# google_maps_url = "Sa4bA8bTUiDRGCzW7"  # Replace with the actual place ID or identifier
# api_key = "GOOGLE_API_KEY"  # Replace with your API key
# coordinates = extract_coordinates_from_google_maps_url(google_maps_url, api_key)
#
# if coordinates:
#     print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")
#
#
#
