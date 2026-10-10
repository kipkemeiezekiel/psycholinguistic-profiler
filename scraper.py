import requests
from bs4 import BeautifulSoup
import re

class WebScraper:
    @staticmethod
    def extract_article_text(url):
        """
        Scrapes clean text pools from public URLs with robust error isolation
        and custom browser agent simulation to bypass immediate firewalls.
        """
        if not url or not isinstance(url, str):
            return "Error: Provided input target URL is structurally invalid."
            
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        try:
            # Set explicit request timeouts to prevent system freezes
            response = requests.get(url, headers=headers, timeout=8)
            
            # Explicitly catch non-200 HTTP statuses
            if response.status_code != 200:
                return f"Error: Target server returned an unhandled HTTP {response.status_code} status code."
                
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Decompose boilerplate structure to isolate real textual behavior
            for noise in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
                noise.decompose()
                
            paragraphs = soup.find_all("p")
            if not paragraphs:
                return "Error: Document parsing yielded zero textual body elements (<p>)."
                
            clean_text = " ".join([p.get_text() for p in paragraphs])
            
            # Normalize whitespace layout constraints
            clean_text = re.sub(r'\s+', ' ', clean_text).strip()
            
            if len(clean_text) < 10:
                return "Error: Extracted natural language payload density falls below processing threshold."
                
            return clean_text
            
        except requests.exceptions.Timeout:
            return "Error: The connection request timed out before web components could resolve."
        except requests.exceptions.ConnectionError:
            return "Error: Failed to establish a clean remote socket connection to the target host DNS."
        except Exception as e:
            return f"Unhandled Data Ingestion Failure: {str(e)}"

if __name__ == "__main__":
    # Test network isolation pipeline
    print(WebScraper.extract_article_text("https://invalid-dns-target-domain.xyz"))
