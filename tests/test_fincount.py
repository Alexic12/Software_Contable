"""Tests for FINCOUNT initialization and core functionality."""

import sys
from pathlib import Path

# Add src directory to path for imports
# Note: For production, install package in editable mode: pip install -e .
src_path = str(Path(__file__).parent.parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import fincount


def test_version():
    """Test that version is defined."""
    assert hasattr(fincount, "__version__")
    assert isinstance(fincount.__version__, str)
    assert fincount.__version__ == "0.1.0"


def test_init_no_config():
    """Test initialization without configuration."""
    app = fincount.init()
    assert app["version"] == "0.1.0"
    assert app["status"] == "initialized"
    assert app["config"] == {}


def test_init_with_config():
    """Test initialization with configuration."""
    config = {"debug": True, "database": "sqlite"}
    app = fincount.init(config)
    assert app["version"] == "0.1.0"
    assert app["status"] == "initialized"
    assert app["config"] == config
