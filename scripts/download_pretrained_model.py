#!/usr/bin/env python3
"""
Download and setup pre-trained action recognition models
"""

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

def download_movinet_model():
    """
    Download MoViNet model from TensorFlow Hub
    This is a lightweight, efficient model for action recognition
    Trained on Kinetics-600 dataset (600 action classes)
    """
    print("Downloading MoViNet A0 model from TensorFlow Hub...")
    print("This may take a few minutes...")
    
    # Load pre-trained MoViNet model
    model_url = "https://tfhub.dev/tensorflow/movinet/a0/base/kinetics-600/classification/3"
    
    try:
        model = hub.load(model_url)
        print("✓ Model downloaded successfully!")
        print(f"Model loaded from: {model_url}")
        return model
    except Exception as e:
        print(f"Error downloading model: {e}")
        return None

def download_i3d_model():
    """
    Download I3D model from TensorFlow Hub
    More accurate but slower than MoViNet
    Trained on Kinetics-400 dataset
    """
    print("Downloading I3D model from TensorFlow Hub...")
    
    model_url = "https://tfhub.dev/deepmind/i3d-kinetics-400/1"
    
    try:
        model = hub.load(model_url)
        print("✓ Model downloaded successfully!")
        return model
    except Exception as e:
        print(f"Error downloading model: {e}")
        return None

def list_kinetics_classes():
    """
    Returns list of Kinetics-600 action classes
    These are the actions the pre-trained model can recognize
    """
    # Sample of common actions from Kinetics-600
    common_actions = [
        "walking", "running", "jumping", "sitting", "standing",
        "waving", "clapping", "dancing", "eating", "drinking",
        "cooking", "driving", "reading", "writing", "typing",
        "playing basketball", "playing guitar", "swimming", "cycling",
        "exercising", "talking", "laughing", "hugging", "kissing",
        "shaking hands", "opening door", "closing door", "pushing",
        "pulling", "climbing", "falling", "sleeping", "yoga"
    ]
    return common_actions

if __name__ == "__main__":
    print("=" * 60)
    print("Pre-trained Action Recognition Model Downloader")
    print("=" * 60)
    
    print("\nAvailable models:")
    print("1. MoViNet A0 - Fast, efficient (recommended for real-time)")
    print("2. I3D - More accurate, slower")
    
    choice = input("\nSelect model (1 or 2): ").strip()
    
    if choice == "1":
        model = download_movinet_model()
    elif choice == "2":
        model = download_i3d_model()
    else:
        print("Invalid choice")
        exit(1)
    
    if model:
        print("\n✓ Setup complete!")
        print("\nSample actions the model can recognize:")
        for action in list_kinetics_classes()[:10]:
            print(f"  - {action}")
        print("  ... and 590+ more actions!")