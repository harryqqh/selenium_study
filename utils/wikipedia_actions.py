"""
Wikipedia actions module for test automation framework.
Contains a class with various Wikipedia operations and interactions.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class WikipediaActions:
    """Class containing various Wikipedia actions and operations."""
    
    def __init__(self, driver, base_url="https://www.wikipedia.org/"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to_homepage(self):
        """Navigate to Wikipedia homepage."""
        print(f"Navigating to Wikipedia homepage: {self.base_url}")
        self.driver.get(self.base_url)
        return self.driver.current_url
    
    def get_page_info(self):
        return {
            'url': self.driver.current_url,
            'title': self.driver.title
        }
    
    def search_keyword(self, keyword):
        """
        Search for a keyword on Wikipedia.
        
        Args:
            keyword (str): The keyword to search for
            
        Returns:
            bool: True if search was successful, False otherwise
        """
        try:
            print(f"\n--- Searching Wikipedia for: '{keyword}' ---")
            
            # Navigate to homepage first
            self.navigate_to_homepage()
            
            # Get initial page info
            page_info = self.get_page_info()
            print(f"Page URL: {page_info['url']}")
            print(f"Page title: {page_info['title']}")
            
            # Find and interact with search box
            search_box = self.wait.until(
                EC.presence_of_element_located((By.ID, "searchInput"))
            )
            search_box.clear()
            search_box.send_keys(keyword)
            search_box.submit()
            
            # Wait for results page to load
            self.wait.until(EC.url_changes(self.base_url))
            
            # Get results page info
            results_info = self.get_page_info()
            print(f"Search results URL: {results_info['url']}")
            
            return True
            
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error during search for '{keyword}': {e}")
            return False
    
    def verify_page_heading(self, expected_keyword=None):
        try:
            heading = self.wait.until(
                EC.presence_of_element_located((By.ID, "firstHeading"))
            )
            
            if heading.is_displayed():
                heading_text = heading.text
                print(f"✅ Heading check passed: '{heading_text}'")
                
                # Check if expected keyword matches (case-insensitive)
                keyword_match = True
                if expected_keyword:
                    keyword_match = expected_keyword.lower() in heading_text.lower()
                    if keyword_match:
                        print(f"✅ Keyword '{expected_keyword}' found in heading")
                    else:
                        print(f"⚠️ Keyword '{expected_keyword}' not found in heading '{heading_text}'")
                
                return {
                    'success': True,
                    'heading_text': heading_text,
                    'keyword_match': keyword_match
                }
            else:
                print("❌ Heading element found but not displayed")
                return {'success': False, 'heading_text': None, 'keyword_match': False}
                
        except (TimeoutException, NoSuchElementException) as e:
            print(f"❌ Could not find or verify heading: {e}")
            return {'success': False, 'heading_text': None, 'keyword_match': False}
    
    def navigate_back(self):
        """Navigate back to previous page."""
        self.driver.back()
        current_url = self.driver.current_url
        print(f"⬅️ Navigated back to: {current_url}")
        return current_url
    
    def navigate_forward(self):
        """Navigate forward to next page."""
        self.driver.forward()
        current_url = self.driver.current_url
        print(f"➡️ Navigated forward to: {current_url}")
        return current_url
    
    def get_page_summary(self):
        """
        Get the first paragraph of the Wikipedia article as summary.
        
        Returns:
            str: First paragraph text or None if not found
        """
        try:
            # Look for the first paragraph in the main content
            summary_selectors = [
                "div.mw-parser-output > p:first-of-type",
                ".mw-parser-output p",
                "#mw-content-text p"
            ]
            
            for selector in summary_selectors:
                try:
                    summary_element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if summary_element.text.strip():
                        summary = summary_element.text.strip()
                        print(f"📄 Page summary: {summary[:100]}...")
                        return summary
                except NoSuchElementException:
                    continue
            
            print("⚠️ No summary found on this page")
            return None
            
        except Exception as e:
            print(f"❌ Error getting page summary: {e}")
            return None
    
    def check_page_exists(self):
        """
        Check if the current page is a valid Wikipedia article (not a disambiguation or error page).
        
        Returns:
            dict: Dictionary with page status information
        """
        try:
            current_url = self.driver.current_url
            page_title = self.driver.title
            # Check for common indicators
            is_disambiguation = bool(self.driver.find_elements(By.ID, "disambigbox"))
            is_search_results = "search results" in page_title.lower()
            is_error_page = "does not exist" in self.driver.page_source.lower()
            
            # Check if we're on a valid article page
            has_content = bool(self.driver.find_elements(By.ID, "mw-content-text"))
            
            page_status = {
                'url': current_url,
                'title': page_title,
                'is_valid_article': has_content and not is_disambiguation and not is_search_results and not is_error_page,
                'is_disambiguation': is_disambiguation,
                'is_search_results': is_search_results,
                'is_error_page': is_error_page
            }
            
            if page_status['is_valid_article']:
                print("✅ Valid Wikipedia article page")
            elif page_status['is_disambiguation']:
                print("📋 Disambiguation page detected")
            elif page_status['is_search_results']:
                print("🔍 Search results page detected")
            elif page_status['is_error_page']:
                print("❌ Error/non-existent page detected")
            else:
                print("❓ Unknown page type")
            
            return page_status
            
        except Exception as e:
            print(f"❌ Error checking page status: {e}")
            return {
                'url': self.driver.current_url,
                'title': self.driver.title,
                'is_valid_article': False,
                'is_disambiguation': False,
                'is_search_results': False,
                'is_error_page': True
            }
    
    def perform_search(self, keyword):
        """
        Perform a complete search test including search, verification, and navigation.
        
        Args:
            keyword (str): The keyword to search for
            
        Returns:
            dict: Complete test results
        """
        print(f"\n🚀 Starting complete search test for: '{keyword}'")
        
        results = {
            'keyword': keyword,
            'search_successful': False,
            'heading_verification': None,
            'page_status': None,
            'summary': None,
            'navigation_test': {'back': False, 'forward': False}
        }
        
        try:
            # Step 1: Search
            results['search_successful'] = self.search_keyword(keyword)
            
            if results['search_successful']:
                # Step 2: Verify heading
                results['heading_verification'] = self.verify_page_heading(keyword)
                
                # Step 3: Check page status
                results['page_status'] = self.check_page_exists()
                
                # Step 4: Get summary (if valid article)
                if results['page_status']['is_valid_article']:
                    results['summary'] = self.get_page_summary()
                
                # Step 5: Test navigation
                back_url = self.navigate_back()
                results['navigation_test']['back'] = self.base_url in back_url
                
                forward_url = self.navigate_forward()
                results['navigation_test']['forward'] = keyword.lower() in forward_url.lower()
            
            # Final navigation back to homepage
            self.navigate_to_homepage()
            
            print(f"✅ Complete test finished for '{keyword}'")
            return results
            
        except Exception as e:
            print(f"❌ Complete test failed for '{keyword}': {e}")
            results['error'] = str(e)
            return results
