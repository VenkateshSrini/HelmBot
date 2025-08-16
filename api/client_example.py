"""
Example client to test HelmBot API endpoints
"""
import requests
import json
from typing import List, Dict


class HelmBotClient:
    """Client for interacting with HelmBot API"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
    
    def get_questions(self) -> List[str]:
        """Get list of questions from the API"""
        response = requests.get(f"{self.base_url}/questions")
        response.raise_for_status()
        data = response.json()
        return data["questions"]
    
    def generate_yaml(self, qa_pairs: List[Dict[str, str]]) -> Dict:
        """Generate YAML from question-answer pairs"""
        payload = {"qa_pairs": qa_pairs}
        response = requests.post(
            f"{self.base_url}/generate-yaml",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json()


def main():
    """Example usage of HelmBot API client"""
    client = HelmBotClient()
    
    try:
        # Get questions
        print("🔍 Fetching questions from API...")
        questions = client.get_questions()
        print(f"✅ Retrieved {len(questions)} questions")
        
        for i, question in enumerate(questions[:3], 1):  # Show first 3 questions
            print(f"  {i}. {question}")
        
        # Example answers (you would collect these from users)
        example_qa_pairs = [
            {
                "question": questions[0] if questions else "What is your app name?",
                "answer": "my-web-app"
            },
            {
                "question": questions[1] if len(questions) > 1 else "How many replicas?",
                "answer": "3"
            }
        ]
        
        # Generate YAML
        print("\n🚀 Generating YAML with example answers...")
        result = client.generate_yaml(example_qa_pairs)
        print("✅ YAML generated successfully!")
        print(f"📁 Saved to: {result['file_path']}")
        print("\n--- Generated YAML Preview ---")
        print(result['yaml_content'][:500] + "..." if len(result['yaml_content']) > 500 else result['yaml_content'])
        
    except requests.exceptions.ConnectionError:
        print("❌ Failed to connect to API. Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
