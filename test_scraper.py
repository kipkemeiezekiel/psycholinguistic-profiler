import unittest
from unittest.mock import patch
import requests
from scraper import WebScraper

class TestWebScraperPipeline(unittest.TestCase):
    
    @patch('requests.get')
    def test_mock_successful_ingestion(self, mock_get):
        """Simulates a highly optimized 200 OK article harvest sequence."""
        # Setup simulated HTML payload structure
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "<html><body><p>Facing truth frees the mind from escapism.</p></body></html>"
        
        result = WebScraper.extract_article_text("https://sample-academic-target.org")
        self.assertEqual(result, "Facing truth frees the mind from escapism.")
        
    @patch('requests.get')
    def test_mock_http_404_not_found(self, mock_get):
        """Validates that a 404 response drops cleanly into handled flags."""
        mock_get.return_value.status_code = 404
        
        result = WebScraper.extract_article_text("https://sample-academic-target.org")
        self.assertIn("Error: Target server returned an unhandled HTTP 404", result)

    @patch('requests.get')
    def test_mock_network_timeout(self, mock_get):
        """Verifies that an open network hang forces a safe error exit."""
        mock_get.side_effect = requests.exceptions.Timeout()
        
        result = WebScraper.extract_article_text("https://hanging-server-target.com")
        self.assertEqual(result, "Error: The connection request timed out before web components could resolve.")

if __name__ == "__main__":
    unittest.main()
