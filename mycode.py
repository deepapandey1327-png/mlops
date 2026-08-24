import pandas as pd
import os

# Create data folder
os.makedirs("data", exist_ok=True)

# Create sample product data
df = pd.DataFrame({
    "product": ["Laptop", "Phone", "Headphones"],
    "price": [55000, 25000, 3000],
    "category": ["Electronics", "Electronics", "Accessories"]
})

# Save data as CSV
df.to_csv("data/products.csv", index=False)

print("Data saved successfully to data/products.csv")