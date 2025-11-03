# 🎬 Surveillance AI System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-orange.svg)](https://www.tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Real-time video surveillance system with AI-powered person detection and action recognition. Features **hybrid mode** for instant camera access with optional AI monitoring. Supports multiple RTSP camera streams with YOLOv8 detection and MoViNet action recognition.

## ✨ Key Features

- 🚀 **Hybrid Mode** - Instant camera access with optional AI (0.2s page load)
- 👥 **Person Detection** - YOLOv8n real-time person tracking
- 🤖 **Action Recognition** - MoViNet for 600+ action classes
- 📹 **Multi-Camera Support** - 16 RTSP camera streams simultaneously
- 🌐 **Web Dashboard** - Real-time monitoring interface
- ⚡ **Fast Mode** - Instant streaming with zero AI overhead (9MB GPU)
- 🧠 **Smart Mode** - Full AI monitoring with event logging (3-4GB GPU)
- 🎛️ **API Control** - REST API for AI enable/disable
- 📊 **Memory Reports** - 12-hour surveillance summaries
- 💾 **Model Management** - Persistent storage for trained models

## 🎯 Quick Start

### Prerequisites

- Python 3.8+
- NVIDIA GPU with CUDA support (recommended)
- 16GB+ RAM
- RTSP camera streams or video files

### Installation

```bash
# Clone repository
git clone https://github.com/mooglemr30-cyber/surveillance-ai-system.git
cd surveillance-ai-system

# Install dependencies
pip install -r requirements.txt

# Download pre-trained models
python scripts/download_pretrained_model.py
```

### Launch Dashboard

```bash
# Start surveillance dashboard
python live_surveillance_dashboard.py

# Or use the optimized hybrid mode
python live_surveillance_with_actions.py
```

Access at: `http://localhost:8080`

## 📖 Documentation

- **[Hybrid Mode Guide](HYBRID_MODE_COMPLETE.md)** - Fast + Smart surveillance
- **[Memory Reporting](AI_MEMORY_REPORTING.md)** - Automated surveillance reports
- **[Quick Start Guide](QUICK_START.md)** - Get started in 5 minutes
- **[System Status](SYSTEM_STATUS.md)** - Complete system overview
- **[Training Guide](docs/TRAINING_GUIDE.md)** - Custom model training

## 🏗️ Architecture

### Hybrid Mode Operation

```
┌─────────────────────────────────────────┐
│         Web Dashboard (Flask)           │
│  http://localhost:8080                  │
└─────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
   Fast Mode              Smart Mode
   (Default)           (API Toggle)
        │                       │
   ┌────┴────┐          ┌──────┴──────┐
   │ RTSP    │          │ YOLOv8      │
   │ Streams │          │ Person      │
   │ Only    │          │ Detection   │
   │         │          └──────┬──────┘
   │ 9MB GPU │                 │
   └─────────┘          ┌──────┴──────┐
                        │ MoViNet     │
                        │ Action      │
                        │ Recognition │
                        └─────────────┘
                        │ 3-4GB GPU   │
```

### Performance Comparison

| Mode | Startup | Page Load | Video Feed | GPU Memory | Detection |
|------|---------|-----------|------------|------------|-----------|
| **Fast** | 1s | 0.2s | 2s | 9MB | ❌ None |
| **Smart** | 1s | 0.2s | 2-3s | 3-4GB | ✅ Real-time |

## 🎮 Usage

### Web Control Panel

1. Access dashboard: `http://localhost:8080`
2. Navigate to AI Control: `http://localhost:8080/ai-control`
3. Click "Enable AI Monitoring" for person detection
4. View events and statistics in real-time

### API Control

```bash
# Enable AI monitoring
curl -X POST http://localhost:8080/api/ai/enable

# Disable AI (fast mode)
curl -X POST http://localhost:8080/api/ai/disable

# Check AI status
curl http://localhost:8080/api/ai/status

# Get detection events
curl http://localhost:8080/api/events

# View statistics
curl http://localhost:8080/api/stats
```

### Memory Reports

```bash
# Generate 12-hour surveillance report
./get_surveillance_memory.sh

# View report
cat /home/admin1/aimemory/surveillance_memory_report.md
```

## 🛠️ Configuration

### Camera Setup

Edit camera configuration in `live_surveillance_with_actions.py`:

```python
CAMERAS = {
    "CH01": {"url": "rtsp://user:pass@ip:port/ch01/00", "name": "Channel 1"},
    "CH02": {"url": "rtsp://user:pass@ip:port/ch02/00", "name": "Channel 2"},
    # Add more cameras...
}
```

### GPU Memory Limit

```python
# Set TensorFlow GPU memory limit (16GB)
gpus = tf.config.list_physical_devices('GPU')
tf.config.set_logical_device_configuration(
    gpus[0],
    [tf.config.LogicalDeviceConfiguration(memory_limit=16384)]
)
```

## 🧪 Testing

```bash
# Run unit tests
pytest tests/

# Test person detection
python scripts/detect_and_recognize.py --source video.mp4

# Test surveillance system
python live_surveillance_dashboard.py
```

## 📊 System Requirements

### Minimum
- CPU: 4 cores
- RAM: 8GB
- GPU: 2GB VRAM
- Storage: 10GB

### Recommended
- CPU: 8+ cores
- RAM: 32GB
- GPU: NVIDIA RTX 3090 (24GB VRAM)
- Storage: 100GB SSD

## 🔧 Troubleshooting

**Issue**: Cameras not loading
```bash
# Check RTSP connectivity
ffplay rtsp://user:pass@ip:port/stream

# Verify network
ping camera-ip
```

**Issue**: High GPU memory usage
```bash
# Check GPU status
nvidia-smi

# Disable AI for fast mode
curl -X POST http://localhost:8080/api/ai/disable
```

**Issue**: Models not loading
```bash
# Re-download models
python scripts/download_pretrained_model.py

# Check model cache
ls -lh ~/.cache/tensorflow_hub/
```

## 📁 Project Structure

```
surveillance-ai-system/
├── live_surveillance_with_actions.py  # Main hybrid mode dashboard
├── live_surveillance_dashboard.py     # Standard surveillance dashboard
├── gui_app.py                         # GUI application
├── get_surveillance_memory.sh         # Memory report generator
├── requirements.txt                   # Python dependencies
├── config/
│   └── config.yaml                    # Configuration file
├── scripts/
│   ├── detect_and_recognize.py        # Detection script
│   ├── download_pretrained_model.py   # Model downloader
│   ├── fine_tune_model.py             # Training script
│   └── model_manager.py               # Model management
├── templates/
│   ├── page1.html                     # Main dashboard
│   ├── ai_control.html                # AI control panel
│   └── gpu_monitor.html               # GPU monitoring
├── models/                            # Model storage
├── docs/                              # Documentation
└── tests/                             # Unit tests
```

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **YOLOv8** by Ultralytics - Person detection
- **MoViNet** by TensorFlow - Action recognition
- **TensorFlow Hub** - Pre-trained models
- **Flask** - Web framework
- **OpenCV** - Video processing

## 📧 Contact

- GitHub: [@mooglemr30-cyber](https://github.com/mooglemr30-cyber)
- Repository: [surveillance-ai-system](https://github.com/mooglemr30-cyber/surveillance-ai-system)

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Built with ❤️ for real-time surveillance and AI monitoring**
