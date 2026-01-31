import requests
import sys
from datetime import datetime
import json

class JRAurosAPITester:
    def __init__(self, base_url="https://jrautos-cars.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.results = []

    def run_test(self, name, method, endpoint, expected_status, data=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)

            success = response.status_code == expected_status
            
            result = {
                "test_name": name,
                "endpoint": endpoint,
                "method": method,
                "expected_status": expected_status,
                "actual_status": response.status_code,
                "success": success,
                "response_data": None
            }

            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    result["response_data"] = response.json()
                except:
                    result["response_data"] = response.text[:200]
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                try:
                    error_data = response.json()
                    print(f"   Error: {error_data}")
                    result["error_data"] = error_data
                except:
                    print(f"   Error: {response.text[:200]}")
                    result["error_data"] = response.text[:200]

            self.results.append(result)
            return success, response.json() if success and response.content else {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            result = {
                "test_name": name,
                "endpoint": endpoint,
                "method": method,
                "expected_status": expected_status,
                "actual_status": "ERROR",
                "success": False,
                "error_data": str(e)
            }
            self.results.append(result)
            return False, {}

    def test_health_endpoints(self):
        """Test basic health endpoints"""
        print("\n=== Testing Health Endpoints ===")
        
        # Test root endpoint
        self.run_test("Root API", "GET", "api/", 200)
        
        # Test health check
        self.run_test("Health Check", "GET", "api/health", 200)

    def test_contact_form(self):
        """Test contact form submission"""
        print("\n=== Testing Contact Form ===")
        
        # Test contact form submission
        contact_data = {
            "name": "Test User",
            "email": "test@example.com",
            "phone": "+52 448 000 0000",
            "message": "This is a test message from automated testing"
        }
        
        success, response = self.run_test(
            "Contact Form Submission",
            "POST",
            "api/contact",
            200,
            data=contact_data
        )
        
        if success:
            print(f"   Contact ID: {response.get('id', 'N/A')}")
            return response.get('id')
        return None

    def test_get_contacts(self):
        """Test getting contact messages"""
        print("\n=== Testing Contact Retrieval ===")
        
        self.run_test("Get Contact Messages", "GET", "api/contact", 200)

    def test_vehicles_endpoint(self):
        """Test vehicles endpoint"""
        print("\n=== Testing Vehicles Endpoint ===")
        
        self.run_test("Get Vehicles", "GET", "api/vehicles", 200)

    def test_status_endpoints(self):
        """Test status check endpoints"""
        print("\n=== Testing Status Endpoints ===")
        
        # Test creating status check
        status_data = {
            "client_name": "test_client_" + datetime.now().strftime('%H%M%S')
        }
        
        success, response = self.run_test(
            "Create Status Check",
            "POST",
            "api/status",
            200,
            data=status_data
        )
        
        if success:
            print(f"   Status ID: {response.get('id', 'N/A')}")
        
        # Test getting status checks
        self.run_test("Get Status Checks", "GET", "api/status", 200)

    def run_all_tests(self):
        """Run all API tests"""
        print("🚀 Starting J.R Autos API Tests")
        print(f"Base URL: {self.base_url}")
        
        self.test_health_endpoints()
        self.test_contact_form()
        self.test_get_contacts()
        self.test_vehicles_endpoint()
        self.test_status_endpoints()
        
        # Print summary
        print(f"\n📊 Test Summary")
        print(f"Tests run: {self.tests_run}")
        print(f"Tests passed: {self.tests_passed}")
        print(f"Success rate: {(self.tests_passed/self.tests_run)*100:.1f}%")
        
        # Print failed tests
        failed_tests = [r for r in self.results if not r['success']]
        if failed_tests:
            print(f"\n❌ Failed Tests ({len(failed_tests)}):")
            for test in failed_tests:
                print(f"   - {test['test_name']}: {test.get('error_data', 'Unknown error')}")
        
        return self.tests_passed == self.tests_run

def main():
    tester = JRAurosAPITester()
    success = tester.run_all_tests()
    
    # Save results to file
    with open('/app/backend_test_results.json', 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'total_tests': tester.tests_run,
            'passed_tests': tester.tests_passed,
            'success_rate': (tester.tests_passed/tester.tests_run)*100 if tester.tests_run > 0 else 0,
            'results': tester.results
        }, f, indent=2)
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())