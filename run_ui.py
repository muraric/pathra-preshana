#!/usr/bin/env python3
"""
Run the Pathra Preshana web UI
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

from pathra_preshana.app import app

if __name__ == '__main__':
    print("=" * 60)
    print("Pathra Preshana - Web UI")
    print("=" * 60)
    print("\nStarting web server...")
    print("Access the UI at: http://localhost:5001")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5001)

