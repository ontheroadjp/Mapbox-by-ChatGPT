import requests

# Function to search for a location using Mapbox Geocoding API
def search_location(location_name):
    # Replace "YOUR_MAPBOX_ACCESS_TOKEN" with your actual Mapbox access token
    MAPBOX_ACCESS_TOKEN = "YOUR_MAPBOX_ACCESS_TOKEN"
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{location_name}.json?access_token={MAPBOX_ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    if data['features']:
        # Assuming the first result is the closest match
        closest_location = data['features'][0]
        return closest_location['place_name'], closest_location['center']
    else:
        return None, None

# Function to generate map preview URL using Mapbox Static Images API
def generate_map_preview(latitude, longitude, style):
    # Replace "YOUR_MAPBOX_ACCESS_TOKEN" with your actual Mapbox access token
    MAPBOX_ACCESS_TOKEN = "YOUR_MAPBOX_ACCESS_TOKEN"
    url = f"https://api.mapbox.com/styles/v1/mapbox/{style}/static/{latitude},{longitude},10,0,0/800x600?access_token={MAPBOX_ACCESS_TOKEN}"
    return url

# Main function
def main():
    # Step 1: Input the location to estimate
    location_name = input("Enter the location to estimate: ")

    # Step 2: Search for the nearest location
    closest_location_name, coordinates = search_location(location_name)
    if closest_location_name is None:
        print("Location not found.")
        return

    # Step 3: Confirm the estimated latitude and longitude
    print(f"The estimated location is: {closest_location_name}")
    confirmation = input("Is this the correct location? (yes/no): ")
    if confirmation.lower() != 'yes':
        latitude = float(input("Enter the correct latitude: "))
        longitude = float(input("Enter the correct longitude: "))
    else:
        latitude, longitude = coordinates

    # Step 4: Choose the map style
    print("Choose a map style:")
    print("1. light-v10")
    print("2. dark-v10")
    print("3. outdoors-v11")
    print("4. satellite-streets-v11")
    style_choice = input("Enter the number of the desired style: ")
    styles = ["light-v10", "dark-v10", "outdoors-v11", "satellite-streets-v11"]
    try:
        style = styles[int(style_choice) - 1]
    except IndexError:
        print("Invalid choice.")
        return

    # Step 5: Generate map preview
    map_url = generate_map_preview(latitude, longitude, style)
    print("Map preview URL:")
    print(map_url)

if __name__ == "__main__":
    main()
