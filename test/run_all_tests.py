"""
Test runner for HelmBot - runs all tests in sequence
"""
import os
import sys
import subprocess

def run_test(test_file):
    """Run a single test file"""
    print(f"\n{'='*60}")
    print(f"🧪 Running: {test_file}")
    print(f"{'='*60}")
    
    try:
        # Get the Python executable path
        python_exe = sys.executable
        test_path = os.path.join("test", test_file)
        
        # Run the test
        result = subprocess.run([python_exe, test_path], 
                              capture_output=False, 
                              text=True)
        
        if result.returncode == 0:
            print(f"✅ {test_file} - PASSED")
            return True
        else:
            print(f"❌ {test_file} - FAILED")
            return False
            
    except Exception as e:
        print(f"❌ {test_file} - ERROR: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 HelmBot Test Suite Runner")
    print("=" * 60)
    
    # List of test files to run
    test_files = [
        "demo_api_setup.py",
        "test_llm_claude.py",
        "test_service.py",
        "test_complete_flow.py",
        # "test_api_key_prompting.py",  # Skip this as it requires user input
    ]
    
    results = {}
    
    # Run each test
    for test_file in test_files:
        if os.path.exists(os.path.join("test", test_file)):
            results[test_file] = run_test(test_file)
        else:
            print(f"⚠️  Test file not found: {test_file}")
            results[test_file] = False
    
    # Summary
    print(f"\n{'='*60}")
    print("📊 Test Results Summary")
    print(f"{'='*60}")
    
    passed = sum(1 for result in results.values() if result)
    total = len(results)
    
    for test_file, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_file:<30} {status}")
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("⚠️  Some tests failed.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)