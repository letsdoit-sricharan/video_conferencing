#!/usr/bin/env python3
"""
Easy startup script for LAN Collaboration Client
Handles dependencies and provides connection help
"""

import sys
import os
import subprocess

def check_dependencies():
    """Check if required dependencies are available."""
    print("🔍 Checking dependencies...")
    
    missing = []
    
    # Check PyQt6
    try:
        import PyQt6
        print("✅ PyQt6: OK")
    except ImportError:
        print("❌ PyQt6: Missing")
        missing.append("PyQt6")
    
    # Check OpenCV
    try:
        import cv2
        print("✅ OpenCV: OK")
    except ImportError:
        print("⚠️  OpenCV: Missing (video features disabled)")
    
    # Check NumPy
    try:
        import numpy
        print("✅ NumPy: OK")
    except ImportError:
        print("❌ NumPy: Missing")
        missing.append("numpy")
    
    # Check Pillow
    try:
        import PIL
        print("✅ Pillow: OK")
    except ImportError:
        print("❌ Pillow: Missing")
        missing.append("Pillow")
    
    # Check PyAudio (optional)
    try:
        import pyaudio
        print("✅ PyAudio: OK")
    except ImportError:
        print("⚠️  PyAudio: Missing (audio features disabled)")
    
    # Check MSS (optional)
    try:
        import mss
        print("✅ MSS: OK")
    except ImportError:
        print("⚠️  MSS: Missing (screen capture disabled)")
    
    if missing:
        print(f"\n❌ Missing required packages: {', '.join(missing)}")
        return False
    
    print("✅ All required dependencies available")
    return True

def show_connection_help():
    """Show connection help information."""
    print("\n" + "=" * 60)
    print("🔗 CONNECTION HELP")
    print("=" * 60)
    print()
    print("1️⃣ Start the server first:")
    print("   python main_server.py")
    print("   # OR")
    print("   python start_server.py")
    print()
    print("2️⃣ Find server IP:")
    print("   • Same machine: use 'localhost'")
    print("   • Different machine: check server startup output")
    print()
    print("3️⃣ Connect with client:")
    print("   • Host: localhost (or server IP)")
    print("   • Port: 9000")
    print("   • Username: Your display name")
    print()
    print("🔧 Troubleshooting:")
    print("   • Ensure server is running first")
    print("   • Check firewall settings")
    print("   • Verify you're on the same network")
    print("   • Try 'localhost' if on same machine")
    print()

def main():
    """Main startup function."""
    print("🚀 LAN Collaboration Client Startup")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Cannot start client due to missing dependencies")
        print("💡 Install missing packages:")
        print("   python install.py")
        print("   # OR")
        print("   pip install -r requirements.txt")
        return 1
    
    # Show connection help
    show_connection_help()
    
    # Check if main_client.py exists
    if not os.path.exists('main_client.py'):
        print("❌ main_client.py not found in current directory")
        print("💡 Make sure you're in the gui/ directory")
        return 1
    
    # Start the client
    print("🎯 Starting client...")
    print("=" * 60)
    
    try:
        # Import and run the client
        from main_client import ClientMainWindow
        from PyQt6.QtWidgets import QApplication
        
        app = QApplication(sys.argv)
        client = ClientMainWindow()
        client.show()
        
        return app.exec()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Check that all dependencies are installed")
        return 1
    except Exception as e:
        print(f"❌ Error starting client: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())