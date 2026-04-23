import requests
import sys

URL = "http://localhost:5000/health"

try:
    response = requests.get(URL, timeout=5)
    if response.status_code == 200:
        print("✅ App is healthy")
        sys.exit(0)
    else:
        print(f"❌ Bad status: {response.status_code}")
        sys.exit(1)
except Exception as e:
    print(f"❌ App is down: {e}")
    sys.exit(1)