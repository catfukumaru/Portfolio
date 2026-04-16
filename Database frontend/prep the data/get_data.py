import kagglehub

# Download latest version
path = kagglehub.dataset_download("terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database")

print("Path to dataset files:", path)