import sys
import os
# Add the parent directory to the path to import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.data_utils import DataUtils
from utils.wikipedia_actions import WikipediaActions

# Main test execution
def main():
    # Set up Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Read test data from CSV using DataUtils
        keywords = DataUtils.read_test_data_from_csv('test_data.csv')
        print(f"Loaded {len(keywords)} test keywords from CSV: {keywords}")
        
        # Initialize Wikipedia actions
        wiki_actions = WikipediaActions(driver)
        
        # Run complete tests for each keyword
        test_results = []
        for keyword in keywords:
            result = wiki_actions.perform_search(keyword)
            test_results.append(result)
        
        # Print summary
        print(f"\n🎉 === All tests completed! ===")
        print(f"📊 Tested {len(keywords)} keywords: {', '.join(keywords)}")
        
        # Print detailed results
        successful_tests = [r for r in test_results if r['search_successful']]
        print(f"✅ Successful searches: {len(successful_tests)}/{len(test_results)}")
        
        for result in test_results:
            status = "✅" if result['search_successful'] else "❌"
            print(f"  {status} {result['keyword']}")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
    finally:
        # Close the browser
        driver.quit()
        print("🔒 Browser closed.")

# Run the main function
if __name__ == "__main__":
    main()
