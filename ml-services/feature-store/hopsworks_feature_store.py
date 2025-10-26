"""
Hopsworks Feature Store integration (Community Edition)
This module provides a basic setup for connecting to Hopsworks Feature Store using the hopsworks Python SDK.
"""

import hopsworks

class HopsworksFeatureStore:
    def __init__(self, project_name: str, api_key: str):
        self.project_name = project_name
        self.api_key = api_key
        self.connection = None
        self.feature_store = None

    def connect(self):
        """Connect to Hopsworks and get the feature store object."""
        self.connection = hopsworks.connection(
            project=self.project_name,
            api_key_value=self.api_key
        )
        self.feature_store = self.connection.get_feature_store()
        return self.feature_store

    def get_feature_group(self, name: str, version: int = 1):
        """Get a feature group by name and version."""
        if not self.feature_store:
            self.connect()
        return self.feature_store.get_feature_group(name=name, version=version)

    def get_feature_view(self, name: str, version: int = 1):
        """Get a feature view by name and version."""
        if not self.feature_store:
            self.connect()
        return self.feature_store.get_feature_view(name=name, version=version)

# Example usage (uncomment and fill in your credentials to use):
# store = HopsworksFeatureStore(project_name="your_project", api_key="your_api_key")
# fs = store.connect()
# fg = store.get_feature_group("your_feature_group", version=1)
# fv = store.get_feature_view("your_feature_view", version=1)
