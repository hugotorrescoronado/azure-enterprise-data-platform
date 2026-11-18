@'
import requests
import pandas as pd

URL = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(URL)
    response.raise_for_status()

    df = pd.DataFrame(response.json())

    df.to_csv(
        "../datasets/api_users.csv",
        index=False
    )

    print("API ingestion completed")

except Exception as e:
    print(f"Error: {e}")
'@ | Out-File python\api_ingestion.py