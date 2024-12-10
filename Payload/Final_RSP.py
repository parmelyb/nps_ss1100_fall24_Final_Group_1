################################
#Remote Sensing Payload
################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.ndimage import sobel
import tkinter as tk
from tkinter import filedialog


def select_file():
    """Open a file dialog to select a file and return the file path."""
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV Files", "*.csv")])
    return file_path


def get_file_path(prompt="Enter file path:"):
    """Prompt the user to manually enter a file path."""
    return input(prompt)


def load_band_data(file_path):
    """Load band data from a CSV file, removing the first row and first column."""
    try:
        # Load the CSV into a DataFrame
        df = pd.read_csv(file_path, header=None)

        # Drop the first row and the first column
        df = df.drop(index=0)
        df = df.drop(columns=df.columns[0])

        # Convert the DataFrame to a NumPy array
        return df.to_numpy()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as exc:
        print(f"Error loading the file {file_path}: {exc}")
        return None


def check_band_dimensions(R, G, B):
    """Check if the dimensions of the RGB bands are the same."""
    if R.shape == G.shape == B.shape:
        print("(Bands have the same dimensions) -> Proceeding To Stack")
    else:
        print(f"Band dimensions are different: R {R.shape}, G {G.shape}, B {B.shape}")
        return False
    return True


def create_rgb_image(R, G, B):
    """Create an RGB image by stacking R, G, and B bands."""
    rgb_image = np.stack((R, G, B), axis=-1)
    print("Stacking RGB Images...")
    return rgb_image


def check_for_invalid_values(image):
    """Check and handle NaN (Not a Number) or Infinite values in the image."""
    if np.any(np.isnan(image)):
        print("Warning: Image contains NaN values!")
        image = np.nan_to_num(image, nan=0)  # Replace NaNs with 0
    if np.any(np.isinf(image)):
        print("Warning: Image contains infinite values!")
        image = np.nan_to_num(image, posinf=255, neginf=0)  # Replace Inf with 255, -Inf with 0
    return image


def radiance_to_reflectance(rgb_image, k=0.8, b=0.1):
    """Convert radiance to reflectance."""
    reflectance_image = k * rgb_image + b
    reflectance_image = np.clip(reflectance_image, 0.0, 255)  # Clip the values to [0, 255]
    print("Radiance Converted to Reflectance...")
    return reflectance_image


def rescale_to_dn(reflectance_image):
    """Rescale the reflectance image to digital numbers (DN)."""
    # Ensure reflectance is within the range [0, 1]
    reflectance_image = np.clip(reflectance_image, 0, 100)
    # Scale to the range [0, 255] and convert to uint8 (8-bit)
    dn_image = (reflectance_image * 20).astype(np.uint8)
    print("Reflectance Image Rescaled to Digital Numbers...")
    return dn_image


def apply_sharpening_filter(image):
    """Apply a sharpening filter to enhance image details."""
    # Sobel filter for edge detection (sharpness)
    sobel_x = sobel(image, axis=0)
    sobel_y = sobel(image, axis=1)
    gradient_magnitude = np.hypot(sobel_x, sobel_y)

    # Sharpen the image by increasing the contrast in high-gradient areas
    sharpened_image = image + gradient_magnitude * 0.3  # Increased sharpening strength
    sharpened_image = np.clip(sharpened_image, 0, 255)  # Ensure pixel values stay within range
    print("Sharpening Digital Numbers Image...")
    return sharpened_image.astype(np.uint8)  # Ensure the image is in uint8 format


def histogram_equalization(image):
    """Apply histogram equalization to enhance contrast."""
    # Flatten image and calculate the histogram
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()  # Cumulative distribution function
    cdf_normalized = cdf / cdf[-1]  # Normalize the CDF to the range [0, 1]

    # Use linear interpolation of the CDF to map pixel values to equalized values
    image_equalized = np.interp(image.flatten(), bins[:-1], cdf_normalized * 255)
    return image_equalized.reshape(image.shape).astype(np.uint8)


def apply_gamma_correction(image, gamma=1.2):
    """Apply gamma correction to brighten the image."""
    # Normalize the image to the range [0, 1]
    image_normalized = image / 255.0
    image_gamma_corrected = np.power(image_normalized, gamma)
    # Rescale back to the range [0, 255]
    return np.clip(image_gamma_corrected * 255, 0, 255).astype(np.uint8)


def save_image(image):
    """Save the image to a file."""
    # Ask the user to select a folder to save the file
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    folder_path = filedialog.askdirectory(title="Select folder to save the image")

    if folder_path:
        # Ask for the file name
        file_name = input("Enter the file name (without extension): ") + '.png'

        # Ensure the folder exists
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Save the image
        file_path = os.path.join(folder_path, file_name)
        plt.imshow(image)
        plt.axis('off')  # Hide axes for cleaner image
        plt.savefig(file_path, format='png', bbox_inches='tight', pad_inches=0)
        print(f"Image saved to: {file_path}")
    else:
        print("No folder selected, image not saved.")


# Main logic
def main():
    # Prompt user for file selection (fallback to manual input if necessary)
    try:
        print("Please select the Red band file:")
        R_file = select_file()
        print(f"Loading file from: {R_file}")
        print("Please select the Green band file:")
        G_file = select_file()
        print(f"Loading file from: {G_file}")
        print("Please select the Blue band file:")
        B_file = select_file()
        print(f"Loading file from: {B_file}")
    except Exception as e:
        print("GUI file dialog failed, falling back to manual input.")
        R_file = get_file_path("Please enter the path for the Red band file: ")
        G_file = get_file_path("Please enter the path for the Green band file: ")
        B_file = get_file_path("Please enter the path for the Blue band file: ")

    # Load the band data
    R_data = load_band_data(R_file)
    G_data = load_band_data(G_file)
    B_data = load_band_data(B_file)
    print("Loading Band Data...")

    if R_data is None or G_data is None or B_data is None:
        print("Error Loading Band Data. Exiting...")
    else:
        # Check if the bands have the same dimensions
        if check_band_dimensions(R_data, G_data, B_data):
            # Create the RGB image
            rgb_image = create_rgb_image(R_data, G_data, B_data)

            # Clean the image before casting
            rgb_image = check_for_invalid_values(rgb_image)

            # Convert radiance to reflectance
            reflectance_image = radiance_to_reflectance(rgb_image)

            # Display the Reflectance Image
            plt.imshow(reflectance_image.astype(np.uint8))
            plt.title("Reflectance Image")
            print("Reflectance Image Displayed. -> ")
            plt.show()

            # Rescale the reflectance image to Digital Numbers (DN)
            dn_image = rescale_to_dn(reflectance_image)

            # Apply histogram equalization to enhance contrast
            dn_image_equalized = histogram_equalization(dn_image)

            # Apply gamma correction to improve brightness and contrast
            dn_image_gamma_corrected = apply_gamma_correction(dn_image_equalized)

            # Apply sharpening to enhance details
            dn_image_sharpened = apply_sharpening_filter(dn_image_gamma_corrected)

            # Display the sharpened DN image
            plt.imshow(dn_image_sharpened)
            plt.title("Enhanced Digital Numbers Image")
            print("Enhanced Digital Numbers Image Displayed. -> ")
            plt.show()

            # Save the enhanced DN image
            save_image(dn_image_sharpened)


if __name__ == "__main__":
    main()