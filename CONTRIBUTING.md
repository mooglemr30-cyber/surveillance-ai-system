# Contributing to Surveillance AI System

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please be respectful and constructive in all interactions.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/mooglemr30-cyber/surveillance-ai-system/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version, GPU details)
   - Error messages and logs

### Suggesting Enhancements

1. Check existing issues and discussions
2. Create an issue with:
   - Clear use case
   - Benefits of the enhancement
   - Possible implementation approach

### Contributing Code

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Update documentation
6. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- NVIDIA GPU with CUDA (for testing GPU features)

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/surveillance-ai-system.git
cd surveillance-ai-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies

# Install pre-commit hooks
pre-commit install
```

### Development Dependencies

Create `requirements-dev.txt`:
```
pytest>=7.4.0
pytest-cov>=4.1.0
black>=23.7.0
flake8>=6.1.0
mypy>=1.5.0
pre-commit>=3.3.0
```

## Coding Standards

### Python Style Guide

- Follow PEP 8
- Use Black for formatting: `black .`
- Use flake8 for linting: `flake8 .`
- Use type hints where possible
- Maximum line length: 100 characters

### Code Organization

```python
# Import order: standard library, third-party, local
import os
import sys

import numpy as np
import tensorflow as tf

from src.models import ActionDetector
```

### Documentation

- Add docstrings to all functions and classes
- Use Google-style docstrings
- Update README.md for new features
- Add examples for new functionality

Example docstring:
```python
def detect_actions(video_path: str, confidence: float = 0.5) -> list:
    """Detect actions in a video file.
    
    Args:
        video_path: Path to the video file
        confidence: Minimum confidence threshold (0-1)
        
    Returns:
        List of detected actions with timestamps
        
    Raises:
        FileNotFoundError: If video file doesn't exist
        ValueError: If confidence is not in valid range
    """
    pass
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_detector.py

# Run with verbose output
pytest -v
```

### Writing Tests

- Add tests for all new features
- Maintain >80% code coverage
- Use descriptive test names
- Test edge cases and error conditions

Example test:
```python
import pytest
from src.detector import ActionDetector

def test_detector_initialization():
    """Test detector initializes correctly."""
    detector = ActionDetector(model_path="yolov8n.pt")
    assert detector.model is not None
    assert detector.confidence_threshold == 0.5

def test_invalid_confidence_raises_error():
    """Test that invalid confidence values raise ValueError."""
    with pytest.raises(ValueError):
        detector = ActionDetector(confidence=-0.1)
```

## Pull Request Process

### Before Submitting

1. **Update your fork**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests**:
   ```bash
   pytest
   black --check .
   flake8 .
   ```

3. **Update documentation**:
   - README.md (if adding features)
   - Docstrings
   - CHANGELOG.md

### PR Guidelines

1. **Create descriptive PR title**:
   - ✅ "Add multi-camera support for RTSP streams"
   - ❌ "Update code"

2. **PR Description should include**:
   - What: Brief description of changes
   - Why: Reason for the changes
   - How: Implementation approach
   - Testing: How you tested the changes
   - Screenshots: If UI changes

3. **Keep PRs focused**:
   - One feature/fix per PR
   - Small, reviewable changes
   - Break large features into multiple PRs

4. **Commit messages**:
   ```
   feat: add RTSP stream support
   fix: resolve memory leak in video processor
   docs: update installation instructions
   test: add tests for action detector
   refactor: simplify camera configuration
   ```

### Review Process

1. Maintainers will review within 3-5 days
2. Address review comments
3. Keep discussion constructive
4. Once approved, maintainer will merge

## Areas for Contribution

### High Priority

- [ ] Add more action recognition models
- [ ] Improve multi-camera performance
- [ ] Add REST API documentation
- [ ] Create Docker deployment guide
- [ ] Add automated testing for GPU code

### Good First Issues

- [ ] Add more example videos
- [ ] Improve error messages
- [ ] Add configuration validation
- [ ] Create setup wizard
- [ ] Add logging improvements

### Documentation

- [ ] Add video tutorials
- [ ] Create troubleshooting guide
- [ ] Add architecture diagrams
- [ ] Write deployment guides
- [ ] Create API reference

## Questions?

Feel free to:
- Open an issue for discussion
- Join our community discussions
- Contact maintainers

Thank you for contributing! 🎉