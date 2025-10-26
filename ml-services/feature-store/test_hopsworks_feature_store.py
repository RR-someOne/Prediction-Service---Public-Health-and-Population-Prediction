import unittest

from unittest.mock import patch, MagicMock
from hopsworks_feature_store import HopsworksFeatureStore

class TestHopsworksFeatureStore(unittest.TestCase):
    @patch('hopsworks.connection')
    def test_connect_success(self, mock_connection):
        mock_conn_instance = MagicMock()
        mock_connection.return_value = mock_conn_instance
        fs = HopsworksFeatureStore('project', 'api_key')
        fs.connect()
        mock_connection.assert_called_once_with(project='project', api_key_value='api_key')
        self.assertEqual(fs.connection, mock_conn_instance)

    @patch('hopsworks.connection')
    def test_connect_failure(self, mock_connection):
        mock_connection.side_effect = Exception('Connection failed')
        fs = HopsworksFeatureStore('project', 'api_key')
        with self.assertRaises(Exception):
            fs.connect()

    @patch.object(HopsworksFeatureStore, 'connect')
    def test_get_feature_group(self, mock_connect):
        fs = HopsworksFeatureStore('project', 'api_key')
        fs.feature_store = MagicMock()
        fs.feature_store.get_feature_group.return_value = 'mock_fg'
        result = fs.get_feature_group('group_name')
        fs.feature_store.get_feature_group.assert_called_once()
        self.assertEqual(result, 'mock_fg')

    @patch.object(HopsworksFeatureStore, 'connect')
    def test_get_feature_view(self, mock_connect):
        fs = HopsworksFeatureStore('project', 'api_key')
        fs.feature_store = MagicMock()
        fs.feature_store.get_feature_view.return_value = 'mock_fv'
        result = fs.get_feature_view('view_name')
        fs.feature_store.get_feature_view.assert_called_once()
        self.assertEqual(result, 'mock_fv')

if __name__ == '__main__':
    unittest.main()
