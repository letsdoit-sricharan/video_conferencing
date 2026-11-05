# Libraries & Components Mapping - LAN Collaboration System

## 📚 Complete Library-to-Component Breakdown

This document provides a detailed mapping of every library used in the project and its specific role in each component.

---

## 🎯 Core Python Libraries (Built-in)

### **1. asyncio**
**Purpose:** Asynchronous I/O operations
**Components:**
- ✅ **Server TCP Handler** - Manages multiple client connections concurrently
- ✅ **Network Thread** - Handles async client-server communication
- ✅ **Media Servers** - Coordinates UDP video/audio streaming
- ✅ **File Transfer** - Manages concurrent upload/download operations

**Specific Usage:**
```python
# Server: Async TCP server
self.server = await asyncio.start_server(self.handle_client, host, port)

# Client: Async connection
self.reader, self.writer = await asyncio.open_connection(host, port)
```

---

### **2. socket**
**Purpose:** Low-level network communication
**Components:**
- ✅ **TCP Control Channel** - Main client-server communication (Port 9000)
- ✅ **UDP Video Streaming** - Real-time video transmission (Port 10000)
- ✅ **UDP Audio Streaming** - Real-time audio transmission (Port 11000)
- ✅ **Screen Share Server** - TCP-based screen sharing (Port 12000)
- ✅ **File Upload Server** - File upload handling (Port 13000)
- ✅ **File Download Server** - File download handling (Port 14000)

**Specific Usage:**
```python
# TCP Socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# UDP Socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

---

### **3. threading**
**Purpose:** Multi-threading for concurrent operations
**Components:**
- ✅ **Video Capture Thread** - Continuous camera frame capture
- ✅ **Audio Capture Thread** - Continuous microphone audio capture
- ✅ **Network Communication Thread** - Background TCP communication
- ✅ **File Transfer Threads** - Parallel upload/download operations
- ✅ **Screen Capture Thread** - Continuous screen capture for sharing

**Specific Usage:**
```python
# Creating threads for concurrent operations
video_thread = threading.Thread(target=self.capture_video)
audio_thread = threading.Thread(target=self.capture_audio)
```

---

### **4. json**
**Purpose:** Data serialization and message protocol
**Components:**
- ✅ **Message Protocol** - All TCP messages use JSON format
- ✅ **Chat Messages** - Text message encoding/decoding
- ✅ **Control Commands** - Login, logout, participant updates
- ✅ **File Metadata** - File information exchange
- ✅ **Configuration** - Settings and preferences storage

**Specific Usage:**
```python
# Encoding messages
message = json.dumps({"type": "chat", "content": "Hello"})

# Decoding messages
data = json.loads(message_data.decode())
```

---

### **5. struct**
**Purpose:** Binary data packing/unpacking
**Components:**
- ✅ **UDP Packet Headers** - Video/audio packet structure
- ✅ **Message Length Prefix** - TCP message framing
- ✅ **File Transfer Protocol** - File size and chunk headers
- ✅ **Media Frame Headers** - Frame sequence and metadata

**Specific Usage:**
```python
# Pack message length (4 bytes, big-endian)
length_header = struct.pack('!I', message_length)

# Pack UDP video header (UID, SEQ, FID, SIZE)
header = struct.pack('!IIII', uid, sequence, frame_id, data_size)
```

---

### **6. time**
**Purpose:** Timing and synchronization
**Components:**
- ✅ **Heartbeat Mechanism** - Keep-alive messages every 10 seconds
- ✅ **Timestamp Generation** - Message and event timestamps
- ✅ **Performance Monitoring** - Frame rate calculation
- ✅ **Timeout Handling** - Connection timeout detection
- ✅ **Rate Limiting** - Frame rate control for video/audio

**Specific Usage:**
```python
# Heartbeat timing
last_heartbeat = time.time()

# Frame rate control
time.sleep(1.0 / fps)
```

---

### **7. datetime**
**Purpose:** Date and time handling
**Components:**
- ✅ **Chat Timestamps** - Message time display
- ✅ **Participant Join Time** - User session tracking
- ✅ **File Upload Time** - File metadata timestamps
- ✅ **Log Entries** - Server/client logging with timestamps
- ✅ **Session Statistics** - Uptime and duration tracking

**Specific Usage:**
```python
# ISO format timestamps
timestamp = datetime.now().isoformat()

# Display format
display_time = datetime.now().strftime("%H:%M:%S")
```

---

### **8. pathlib (Path)**
**Purpose:** File system path operations
**Components:**
- ✅ **File Upload Storage** - Managing upload directory
- ✅ **File Download Storage** - Managing download directory
- ✅ **Configuration Files** - Settings file paths
- ✅ **Log Files** - Log file path management
- ✅ **Resource Loading** - Asset and resource paths

**Specific Usage:**
```python
# Create upload directory
upload_dir = Path("uploads")
upload_dir.mkdir(exist_ok=True)

# File path operations
file_path = upload_dir / f"{file_id}_{filename}"
```

---

### **9. uuid**
**Purpose:** Unique identifier generation
**Components:**
- ✅ **File Transfer** - Unique file IDs for uploads
- ✅ **Session Management** - Unique session identifiers
- ✅ **Message IDs** - Unique message tracking (optional)

**Specific Usage:**
```python
# Generate unique file ID
file_id = str(uuid.uuid4())
```

---

### **10. collections (deque)**
**Purpose:** Efficient queue operations
**Components:**
- ✅ **Chat History Buffer** - Fixed-size message history (500 messages)
- ✅ **Frame Buffer** - Video frame buffering for smooth playback
- ✅ **Audio Buffer** - Audio packet buffering
- ✅ **Message Queue** - Outbound message queuing

**Specific Usage:**
```python
# Chat history with max size
self.chat_history = deque(maxlen=MAX_CHAT_HISTORY)
```

---

### **11. sys**
**Purpose:** System-specific parameters and functions
**Components:**
- ✅ **Application Initialization** - Command-line arguments
- ✅ **Exit Handling** - Graceful application shutdown
- ✅ **Error Handling** - Exception information
- ✅ **Platform Detection** - OS-specific behavior

**Specific Usage:**
```python
# Application initialization
app = QApplication(sys.argv)
sys.exit(app.exec())
```

---

### **12. os**
**Purpose:** Operating system interface
**Components:**
- ✅ **File Operations** - File existence checks, size queries
- ✅ **Directory Management** - Creating upload/download folders
- ✅ **Path Operations** - File path manipulation
- ✅ **Environment Variables** - Configuration from environment

**Specific Usage:**
```python
# Check file size
file_size = os.path.getsize(file_path)

# Check file existence
if os.path.exists(file_path):
```

---

### **13. traceback**
**Purpose:** Exception traceback formatting
**Components:**
- ✅ **Error Logging** - Detailed error information
- ✅ **Debug Mode** - Development debugging
- ✅ **Crash Reports** - Error reporting to users

**Specific Usage:**
```python
# Print detailed error
except Exception as e:
    traceback.print_exc()
```

---

### **14. hashlib**
**Purpose:** Cryptographic hashing
**Components:**
- ✅ **File Integrity** - MD5 checksums for file transfers
- ✅ **Data Verification** - Ensuring data integrity

**Specific Usage:**
```python
# Calculate file checksum
hash_md5 = hashlib.md5()
with open(file_path, 'rb') as f:
    for chunk in iter(lambda: f.read(4096), b""):
        hash_md5.update(chunk)
checksum = hash_md5.hexdigest()
```

---

### **15. argparse**
**Purpose:** Command-line argument parsing
**Components:**
- ✅ **Server Configuration** - Command-line server options
- ✅ **Client Configuration** - Command-line client options
- ✅ **Debug Mode** - Enable/disable debug features

**Specific Usage:**
```python
# Parse command-line arguments
parser = argparse.ArgumentParser(description='LAN Collaboration Server')
parser.add_argument('--host', default='0.0.0.0')
parser.add_argument('--port', type=int, default=9000)
```

---

## 🎨 PyQt6 Libraries (GUI Framework)

### **16. PyQt6.QtWidgets**
**Purpose:** GUI widgets and layouts
**Components:**
- ✅ **Main Window** - QMainWindow for application window
- ✅ **Video Grid** - QGridLayout for video frame arrangement
- ✅ **Chat Widget** - QTextBrowser, QLineEdit for messaging
- ✅ **Participants List** - QListWidget for user list
- ✅ **Media Controls** - QPushButton for video/audio/screen controls
- ✅ **File Dialogs** - QFileDialog for file selection
- ✅ **Message Boxes** - QMessageBox for alerts
- ✅ **Progress Bars** - QProgressBar for file transfer progress
- ✅ **Layouts** - QVBoxLayout, QHBoxLayout, QGridLayout
- ✅ **Containers** - QWidget, QFrame, QGroupBox

**Specific Widgets Used:**
```python
QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
QGridLayout, QLabel, QPushButton, QTextEdit, QTextBrowser, 
QLineEdit, QListWidget, QProgressBar, QFileDialog, QMessageBox,
QSplitter, QFrame, QScrollArea, QStatusBar, QMenuBar, QToolBar
```

---

### **17. PyQt6.QtCore**
**Purpose:** Core non-GUI functionality
**Components:**
- ✅ **Threading** - QThread for background operations
- ✅ **Signals/Slots** - pyqtSignal for inter-thread communication
- ✅ **Timers** - QTimer for periodic tasks (heartbeat)
- ✅ **Event Loop** - Qt event processing
- ✅ **Data Types** - Qt-specific data types
- ✅ **Thread Safety** - QMutex for synchronization

**Specific Classes Used:**
```python
Qt, QThread, pyqtSignal, QSize, QTimer, QMutex, QUrl, 
QObject, QPropertyAnimation, QEasingCurve, QRect, QPoint
```

**Usage in Components:**
- **NetworkThread** - QThread for async network operations
- **VideoClient** - QThread for video capture
- **AudioClient** - QThread for audio capture
- **Signals** - message_received, connection_status_changed, etc.

---

### **18. PyQt6.QtGui**
**Purpose:** GUI-related classes (graphics, fonts, colors)
**Components:**
- ✅ **Image Display** - QImage, QPixmap for video frames
- ✅ **Styling** - QPalette, QColor for theming
- ✅ **Fonts** - QFont for text styling
- ✅ **Graphics** - QPainter for custom drawing
- ✅ **Icons** - QIcon for button icons
- ✅ **Drag & Drop** - QDrag, QMimeData for file drag-drop

**Specific Classes Used:**
```python
QImage, QPixmap, QFont, QPalette, QColor, QIcon, QPainter,
QBrush, QPen, QLinearGradient, QDrag, QCursor, QAction
```

**Usage in Components:**
- **Video Frame Display** - Converting NumPy arrays to QPixmap
- **Dark Theme** - QPalette and QColor for styling
- **File Drag-Drop** - QDrag and QMimeData for file uploads

---

## 📹 Video Processing Libraries

### **19. OpenCV (cv2)**
**Purpose:** Computer vision and video processing
**Components:**
- ✅ **Video Capture** - Camera access and frame capture
- ✅ **Video Encoding** - JPEG compression for network transmission
- ✅ **Video Decoding** - JPEG decompression for display
- ✅ **Frame Resizing** - Scaling frames for bandwidth optimization
- ✅ **Color Conversion** - BGR to RGB conversion for Qt display
- ✅ **Image Processing** - Frame manipulation and effects

**Specific Functions Used:**
```python
cv2.VideoCapture()      # Camera access
cv2.imencode()          # JPEG encoding
cv2.imdecode()          # JPEG decoding
cv2.resize()            # Frame resizing
cv2.cvtColor()          # Color space conversion
cv2.flip()              # Mirror video
```

**Usage in Components:**
- **VideoClient** - Captures frames from webcam
- **Video Encoding** - Compresses frames to JPEG
- **Video Decoding** - Decompresses received frames
- **VideoFrame Widget** - Displays frames in GUI

---

### **20. NumPy (numpy)**
**Purpose:** Numerical array operations
**Components:**
- ✅ **Video Frame Storage** - Frames stored as NumPy arrays
- ✅ **Audio Buffer** - Audio data as NumPy arrays
- ✅ **Image Processing** - Array operations on frames
- ✅ **Data Conversion** - Converting between formats
- ✅ **Mathematical Operations** - Frame calculations

**Specific Functions Used:**
```python
np.frombuffer()         # Convert bytes to array
np.array()              # Create array from data
np.uint8                # 8-bit unsigned integer type
np.reshape()            # Reshape arrays
```

**Usage in Components:**
- **Video Processing** - Frame data manipulation
- **Audio Processing** - Audio sample arrays
- **Image Conversion** - Converting between OpenCV and Qt formats

---

## 🎤 Audio Processing Libraries

### **21. PyAudio**
**Purpose:** Audio input/output
**Components:**
- ✅ **Audio Capture** - Microphone input capture
- ✅ **Audio Playback** - Speaker output playback
- ✅ **Audio Streaming** - Real-time audio streaming
- ✅ **Device Management** - Audio device enumeration
- ✅ **Format Configuration** - Sample rate, channels, format

**Specific Functions Used:**
```python
pyaudio.PyAudio()                    # Initialize PyAudio
audio.open()                         # Open audio stream
stream.read()                        # Read audio data
stream.write()                       # Write audio data
audio.get_device_info_by_index()    # Device information
```

**Configuration:**
```python
FORMAT = pyaudio.paInt16            # 16-bit PCM
CHANNELS = 1                        # Mono
RATE = 16000                        # 16kHz sample rate
CHUNK = 1600                        # Buffer size
```

**Usage in Components:**
- **AudioClient** - Captures microphone input
- **Audio Receiver** - Plays received audio
- **Audio Streaming** - UDP audio transmission

---

## 🖥️ Screen Capture Libraries

### **22. MSS (Multi-Screen Shot)**
**Purpose:** Fast screen capture
**Components:**
- ✅ **Screen Sharing** - Full screen capture
- ✅ **Monitor Selection** - Multi-monitor support
- ✅ **Region Capture** - Specific area capture
- ✅ **Performance** - Fast screenshot capture

**Specific Functions Used:**
```python
mss.mss()                           # Initialize MSS
sct.grab()                          # Capture screen
sct.monitors                        # List monitors
```

**Usage in Components:**
- **ScreenCaptureClient** - Captures screen for sharing
- **Screen Share Presenter** - Continuous screen capture
- **Multi-monitor Support** - Select specific monitor

---

### **23. Pillow (PIL)**
**Purpose:** Image processing and format conversion
**Components:**
- ✅ **Image Format Conversion** - Converting between formats
- ✅ **Screen Capture Processing** - MSS output to bytes
- ✅ **Image Resizing** - Scaling screen captures
- ✅ **Image Compression** - Reducing image size
- ✅ **Format Support** - JPEG, PNG, BMP support

**Specific Functions Used:**
```python
Image.frombytes()                   # Create image from bytes
Image.open()                        # Open image file
image.save()                        # Save image
image.resize()                      # Resize image
image.convert()                     # Convert color mode
```

**Usage in Components:**
- **Screen Sharing** - Converting MSS screenshots
- **File Transfer** - Image file handling
- **Image Processing** - Format conversions

---

## 🔧 Optional/Enhancement Libraries

### **24. opuslib (Optional)**
**Purpose:** Opus audio codec for better compression
**Components:**
- ✅ **Audio Encoding** - Compress audio for transmission
- ✅ **Audio Decoding** - Decompress received audio
- ✅ **Bandwidth Optimization** - Better compression than raw PCM

**Note:** Currently optional, system works with raw PCM audio

---

### **25. pydub (Optional)**
**Purpose:** Audio manipulation and effects
**Components:**
- ✅ **Audio Effects** - Noise reduction, normalization
- ✅ **Format Conversion** - Audio format conversion
- ✅ **Audio Mixing** - Combining audio streams

**Note:** Listed in requirements but not currently used in core functionality

---

### **26. psutil (Optional)**
**Purpose:** System and process utilities
**Components:**
- ✅ **Performance Monitoring** - CPU, memory usage
- ✅ **Network Statistics** - Bandwidth monitoring
- ✅ **Process Management** - Process information

**Note:** Listed in requirements for potential monitoring features

---

## 📊 Library Usage Summary by Component

### **Server Components:**

| Component | Primary Libraries |
|-----------|------------------|
| **TCP Server** | asyncio, socket, json, struct |
| **UDP Video Server** | socket, struct, numpy, cv2 |
| **UDP Audio Server** | socket, struct, pyaudio |
| **Screen Share Server** | socket, asyncio, struct |
| **File Upload Server** | asyncio, socket, pathlib, hashlib |
| **File Download Server** | asyncio, socket, pathlib |
| **Participant Management** | collections (deque), datetime, uuid |

### **Client Components:**

| Component | Primary Libraries |
|-----------|------------------|
| **Main Window** | PyQt6.QtWidgets, PyQt6.QtCore, PyQt6.QtGui |
| **Network Thread** | asyncio, socket, json, struct, PyQt6.QtCore |
| **Video Capture** | cv2, numpy, socket, PyQt6.QtCore |
| **Audio Capture** | pyaudio, socket, PyQt6.QtCore |
| **Video Display** | PyQt6.QtGui (QImage, QPixmap), numpy, cv2 |
| **Chat Widget** | PyQt6.QtWidgets, json, datetime |
| **File Transfer** | socket, pathlib, hashlib, PyQt6.QtCore |
| **Screen Capture** | mss, PIL, socket, PyQt6.QtCore |

---

## 🎯 Quick Reference: Library → Purpose

```
asyncio     → Async I/O, concurrent connections
socket      → Network communication (TCP/UDP)
threading   → Multi-threading, concurrent operations
json        → Message protocol, data serialization
struct      → Binary data packing/unpacking
time        → Timing, synchronization, rate limiting
datetime    → Timestamps, time formatting
pathlib     → File system operations
uuid        → Unique identifier generation
collections → Efficient data structures (deque)
sys         → System operations, app lifecycle
os          → OS interface, file operations
traceback   → Error debugging
hashlib     → File integrity checks
argparse    → Command-line arguments

PyQt6.QtWidgets → GUI widgets and layouts
PyQt6.QtCore    → Threading, signals, timers
PyQt6.QtGui     → Graphics, images, styling

cv2         → Video capture, encoding, processing
numpy       → Array operations, data manipulation
pyaudio     → Audio capture and playback
mss         → Screen capture
PIL         → Image processing, format conversion
```

---

## 💡 Interview Talking Points

**"For the networking layer, I used Python's socket and asyncio libraries to implement a multi-port TCP/UDP architecture. OpenCV and NumPy handle video processing, while PyAudio manages audio streaming. The GUI is built with PyQt6, leveraging its signal/slot mechanism for thread-safe communication. MSS and Pillow enable screen capture functionality, and I used struct for efficient binary protocol implementation."**

---

*This comprehensive mapping demonstrates deep understanding of library selection and integration for building a complex real-time collaboration system.*
