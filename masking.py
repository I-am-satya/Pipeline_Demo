import os
import pandas as pd
import json
from faker import Faker

fake = Faker()


with open("masking_rules.json", "r") as f:  
    rules = json.load(f)

digit_map = str.maketrans("0123456789", "9876543210")

os.makedirs("output_files", exist_ok=True)

for filename in os.listdir("input_files"):
    if filename.endswith(".csv"):
        input_path = os.path.join("input_files", filename)
        df = pd.read_csv(input_path)

        for column, rule in rules.items():
            if column in df.columns:
                if rule == "fake_name":
                    df[column] = [fake.name() for _ in range(len(df))]
                elif rule == "email_from_name":
                    if "Customer_Name" in df.columns:
                        df[column] = df["Customer_Name"].apply(
                            lambda name: name.lower().replace(" ", ".") + "@gmail.com"
                        )
                    else:
                        df[column] = [fake.email() for _ in range(len(df))]
                elif rule == "fake_phone":
                    df[column] = [fake.msisdn()[:10] for _ in range(len(df))]
                elif rule == "digit_transform":
                    df[column] = df[column].astype(str).apply(lambda x: x.translate(digit_map))

        output_path = os.path.join("output_files", filename)
        df.to_csv(output_path, index=False)

print("✅ Masking completed. Files saved to output_files/")
