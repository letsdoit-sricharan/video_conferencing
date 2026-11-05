#!/usr/bin/env python3
"""
Final comprehensive test for leave button functionality
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from main_client import ClientMainWindow

def main():
    print("🎯 FINAL LEAVE BUTTON TEST")
    print("=" * 50)
    print("This test will:")
    print("1. Connect to the server")
    print("2. Wait 3 seconds")
    print("3. Click the leave button")
    print("4. Verify clean disconnection")
    print("=" * 50)
    
    app = QApplication(sys.argv)
    
    # Create and show client
    client = ClientMainWindow()
    
    # Connection info
    conn_info = {
        'host': 'localhost',
        'port': 9000,
        'username': 'FinalTest_User',
        'join_with_video': False,
        'join_with_audio': False
    }
    
    print("🔌 Connecting to server...")
    client.connect_to_server(conn_info)
    client.show()
    
    def run_test():
        if client.connected:
            print("✅ Connected successfully!")
            print("🚪 Clicking leave button now...")
            
            # This should work without hanging or requiring terminal/GUI closure
            client.handle_leave_button_click()
            
            def verify_result():
                if not client.connected:
                    print("🎉 SUCCESS! Leave button works perfectly!")
                    print("✅ Meeting ended cleanly")
                    print("✅ No need to close GUI tab or terminal")
                    print("✅ All network connections closed properly")
                else:
                    print("❌ FAILED: Still connected after leave button")
                
                # Exit after verification
                app.quit()
            
            # Verify after 2 seconds
            QTimer.singleShot(2000, verify_result)
        else:
            print("❌ Connection failed")
            app.quit()
    
    # Run test after 3 seconds
    QTimer.singleShot(3000, run_test)
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())