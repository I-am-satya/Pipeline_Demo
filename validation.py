import os
import pandas as pd
import json

with open("masking_rules.json", "r") as f:
    rules = json.load(f)

input_dir = "input_files"
output_dir = "output_files"
print(input_dir, output_dir)
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        if os.path.exists(output_path):
            df_input = pd.read_csv(input_path)
            df_output = pd.read_csv(output_path)

            for column in df_input.columns:
                if column in rules:
                    if df_input[column].equals(df_output[column]):
                        print(f"[ERROR] Column '{column}' not masked in {filename}")
                    else:
                        print(f"[OK] Column '{column}' masked in {filename}")
                else:
                    if df_input[column].equals(df_output[column]):
                        print(f"[OK] Column '{column}' unchanged in {filename}")
                    else:
                        print(f"[ERROR] Column '{column}' should not be changed in {filename}")
