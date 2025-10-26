"""
API Service for United Nations World Tourism Organization (UNWTO) Tourism Statistics Database
Provides endpoints for tourism levels in NATO countries.
"""

import requests
from typing import List, Dict

UNWTO_API_BASE = "https://api.unwto.org/v1/statistics"
NATO_COUNTRIES = [
    "Albania", "Belgium", "Bulgaria", "Canada", "Croatia", "Czech Republic", "Denmark", "Estonia", "France",
    "Germany", "Greece", "Hungary", "Iceland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Montenegro",
    "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
    "Spain", "Turkey", "United Kingdom", "United States"
]

class UNWTOTourismAPI:
    """
    Service to fetch tourism statistics for NATO countries from UNWTO API.
    """
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def get_tourism_levels(self, year: int) -> List[Dict]:
        """
        Fetch tourism statistics for all NATO countries for a given year.
        Returns a list of country data dicts.
        """
        results = []
        for country in NATO_COUNTRIES:
            url = f"{UNWTO_API_BASE}/arrivals?country={country}&year={year}"
            try:
                resp = self.session.get(url)
                resp.raise_for_status()
                data = resp.json()
                results.append({"country": country, "data": data})
            except Exception as e:
                results.append({"country": country, "error": str(e)})
        return results

    def get_country_tourism(self, country: str, year: int) -> Dict:
        """
        Fetch tourism statistics for a specific NATO country for a given year.
        """
        if country not in NATO_COUNTRIES:
            return {"error": "Country not in NATO list."}
        url = f"{UNWTO_API_BASE}/arrivals?country={country}&year={year}"
        try:
            resp = self.session.get(url)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

# Example usage:
# api = UNWTOTourismAPI(api_key="YOUR_UNWTO_API_KEY")
# print(api.get_tourism_levels(2023))
# print(api.get_country_tourism("France", 2023))
