import requests
import pandas as pd
import configparser
import os
import json

class LinkedInProfileFetcher:
    def __init__(self, config_file="config.ini"):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.api_key = config['API']['api_key']
        self.api_endpoint = config['API']['api_endpoint']
        self.output_file = config['OUTPUT']['filename']
        self.json_file = config['OUTPUT']['json_filename']
        self.headers = {'Authorization': f'Bearer {self.api_key}'}

    def fetch_profile(self, linkedin_profile_url):
        params = {'linkedin_profile_url': linkedin_profile_url}
        response = requests.get(self.api_endpoint, params=params, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

    def save_to_excel(self, data):
        if os.path.exists(self.output_file):
            existing_df = pd.read_excel(self.output_file, sheet_name="LinkedIn Profile")
            new_df = pd.DataFrame([data])
            updated_df = pd.concat([existing_df, new_df], ignore_index=True)
        else:
            updated_df = pd.DataFrame([data])
        
        updated_df.to_excel(self.output_file, index=False, sheet_name="LinkedIn Profile")
        print(f"Data saved to {self.output_file}")

    def save_to_json(self, data):
        with open(self.json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {self.json_file}")

if __name__ == "__main__":
    linkedin_url = input("Enter LinkedIn profile URL: ")

    fetcher = LinkedInProfileFetcher()
    try:
        profile_data = fetcher.fetch_profile(linkedin_url)
        print(json.dumps(profile_data, indent=4))
        fetcher.save_to_json(profile_data)
        data_to_save = {
            'First Name': profile_data.get('first_name', ''),
            'Last Name': profile_data.get('last_name', ''),
            'Location': profile_data['experiences'][0].get('location', '') if profile_data.get('experiences') else ''
        }
        fetcher.save_to_excel(data_to_save)
    except Exception as e:
        print(f"Error: {e}")