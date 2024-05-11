import os
import requests

# Function to download satellite images using NASA Worldview API
def download_satellite_images(start_date, end_date, bbox, folder_path):
    # Define API endpoint
    url = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wmts.cgi"

    # Define parameters for the request
    params = {
        "SERVICE": "WMTS",
        "REQUEST": "GetTile",
        "VERSION": "1.0.0",
        "LAYER": "MODIS_Terra_SurfaceReflectance_Bands143",
        "FORMAT": "image/jpeg",
        "TIME": f"{start_date}/{end_date}",
        "TILEMATRIXSET": "EPSG4326_250m",
        "TILEMATRIX": "3",
        "TILEROW": "0",
        "TILECOL": "0",
        "BOUNDINGBOX": f"{bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]}"
    }

    # Send request to the API
    response = requests.get(url, params=params)

    # Save the image to a file
    if response.status_code == 200:
        image_path = os.path.join(folder_path, f"image_{start_date}_{end_date}.jpg")
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download image.")

# Example usage
start_date = "2022-01-01"
end_date = "2022-01-01"
bbox_cords = (73.4218, 18.4151, 73.5445, 18.4463)  # Bounding box coordinate place you for your area of interest
folder_path = 'satellite_images'

# Create folder to save images if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Download satellite images
download_satellite_images(start_date, end_date, bbox_cords, folder_path)
