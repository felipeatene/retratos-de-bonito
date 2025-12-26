#!/usr/bin/env python
import sys
sys.path.insert(0, 'src')

try:
    from app.main import app
    print("✅ FastAPI app loaded successfully")
    print("✅ Backend is ready to run")
except Exception as e:
    print(f"❌ Error loading app: {e}")
    sys.exit(1)
