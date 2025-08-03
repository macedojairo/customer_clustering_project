from pathlib import Path

# define the root path of the project
project_folder = Path(__file__).resolve().parents[1]


# define the paths to your original and cleaned datasets
original_data = project_folder / "Data" / "raw" / "Mall_Customers.csv"

cleaned_data = project_folder / "Data" / "Mall_Customers_no_CustomerID.csv"

# define the folder where your trained models will be saved
models_folder = project_folder / "models"

# define other useful folders (e.g., for reports and images)
reports_folder = project_folder / "reports"
images_folder = reports_folder / "images"

# set a random state for reproducibility in model training and evaluation
random_state = 42

# define a custom RGB color (dark red) for consistent visual styling
rgb_color = (162 / 255, 37 / 255, 56 / 255)

palette = "coolwarm"


