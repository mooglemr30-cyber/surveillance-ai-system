# 🚀 Quick Start Guide

**Get started with Surveillance AI System in 5 minutes!**

---

## Prerequisites

- Python 3.8+
- NVIDIA GPU with CUDA (recommended)
- Camera streams or video files

---

## Installation

```bash
# Clone repository
git clone https://github.com/mooglemr30-cyber/surveillance-ai-system.git
cd surveillance-ai-system

# Install dependencies
pip install -r requirements.txt

# Download models
python scripts/download_pretrained_model.py
```

---

## Quick Test

### 1. Test with Webcam
```bash
python scripts/detect_and_recognize.py --input 0
```
Press 'q' to quit.

### 2. Process Video File
```bash
python scripts/detect_and_recognize.py --input video.mp4 --output result.mp4
```

### 3. Launch Web Dashboard
```bash
python live_surveillance_dashboard.py
```
Access at: http://localhost:8080

### 4. Launch GUI
```bash
./launch_gui.sh
```

---

## Key Commands

### Person Detection + Action Recognition
```bash
# Webcam
python scripts/detect_and_recognize.py --input 0

# Video file
python scripts/detect_and_recognize.py --input video.mp4

# RTSP stream
python scripts/detect_and_recognize.py --input rtsp://camera_url
```

### Train Custom Model
```bash
python scripts/train_terminal.py \
  --dataset training/example_dataset \
  --name my_model \
  --epochs 20
```

### Memory Reports
```bash
# Get 12-hour surveillance report
./get_surveillance_memory.sh
```

---

## Model Options

### Person Detection (YOLOv8)
- `yolov8n.pt` - Fastest (default)
- `yolov8s.pt` - Fast
- `yolov8m.pt` - Balanced
- `yolov8l.pt` - High accuracy
- `yolov8x.pt` - Highest accuracy

### Action Recognition (MoViNet)
- `movinet_a0` - Fastest (72% accuracy)
- `movinet_a3` - Recommended (81% accuracy)
- `movinet_a5` - Highest (85% accuracy)

---

## Configuration

### Camera Setup

Edit `live_surveillance_with_actions.py`:

```python
CAMERAS = {
    "CH01": {"url": "rtsp://user:pass@ip:port/stream", "name": "Camera 1"},
    "CH02": {"url": "rtsp://user:pass@ip:port/stream", "name": "Camera 2"},
}
```

### GPU Memory Limit

```python
import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
tf.config.set_logical_device_configuration(
    gpus[0],
    [tf.config.LogicalDeviceConfiguration(memory_limit=16384)]
)
```

---

## Troubleshooting

**Issue**: Module not found
```bash
pip install -r requirements.txt
```

**Issue**: CUDA out of memory
- Use smaller model: `--yolo yolov8n.pt`
- Reduce batch size
- Lower video resolution

**Issue**: Slow processing
- Use GPU
- Use faster models (yolov8n, movinet_a0)
- Process every Nth frame

---

## Next Steps

1. 📚 Read [Full Documentation](README.md)
2. 🎬 Try [Hybrid Mode](HYBRID_MODE_COMPLETE.md)
3. 📊 Setup [Memory Reports](AI_MEMORY_REPORTING.md)
4. 🎯 Train [Custom Models](docs/TRAINING_GUIDE.md)

---

**You're ready to go! 🎉**

Start with: `python scripts/detect_and_recognize.py --input 0`