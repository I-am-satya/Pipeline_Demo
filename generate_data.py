from faker import Faker
import numpy as np
import pandas as pd
import re


def generate_synthetic_data(num_samples=1000, seed=42):
  np.random.seed(seed)
  faker=Faker()
  Faker.seed(seed)
  # Generate synthetic data
  names = [faker.name() for _ in range(num_samples)]
  emails = [name.lower().replace(" ",".")+"@infosys.com" for name in names]
  phones = [faker.phone_number() for _ in range(num_samples)]
  ages = np.random.randint(18, 70, size=num_samples)
  
  income = np.random.normal(loc=50000, scale=15000, size=num_samples).astype(int)
  
  purchase_probability = np.clip((income / 100000) + (ages / 100), 0, 1)
  
  purchased = np.random.binomial (1, purchase_probability)

  #Create DataFrame

  df = pd.DataFrame({
    'Name': names,
    'Email':emails,
    'Phone Number': phones,
    'Age': ages,
    'Income': income, 
    'Purchased': purchased
  })
  return df

def main():
  
  df = generate_synthetic_data()

  print("Synthetic data preview:")

  print(df.head())
  print("Data Shape : ", df.shape)

  #Save to CSV

  df.to_csv('synthetic_data.csv', index=False)

  print("Synthetic data saved to 'synthetic_data.csv'.")

if __name__ == "__main__":
    main()
