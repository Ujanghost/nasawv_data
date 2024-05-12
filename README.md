# nasawv_data
----

## Satellite Image Downloader

This Python script allows you to download satellite images using NASA's Worldview API. It retrieves images from the MODIS Terra Surface Reflectance Bands143 layer for a specified time period and geographic region.

### Usage

1. Ensure you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Modify the script to specify the start date, end date, bounding box coordinates, and folder path where you want to save the images.
5. Run the script using `python satellite_image_downloader.py`.

### Parameters

- `start_date`: The start date for the image time period in "YYYY-MM-DD" format.
- `end_date`: The end date for the image time period in "YYYY-MM-DD" format.
- `bbox`: The bounding box coordinates (longitude, latitude) of the area of interest in the format `(min_lon, min_lat, max_lon, max_lat)`.
- `folder_path`: The path to the folder where you want to save the downloaded images.

### Example

```python
start_date = "2022-01-01"
end_date = "2022-01-01"
bbox_cords = (73.4218, 18.4151, 73.5445, 18.4463)  # Bounding box coordinates for your area of interest
folder_path = 'satellite_images'

# Download satellite images
download_satellite_images(start_date, end_date, bbox_cords, folder_path)
```

### Contributing

If you have any suggestions or improvements for this script, feel free to open an issue or submit a pull request. Your contributions are highly appreciated!

Happy coding! 🚀
