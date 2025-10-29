"""
FINCOUNT - Financial Accounting Software

Enterprise-grade financial accounting software built with Python.
"""

__version__ = "0.1.0"
__author__ = "FINCOUNT Development Team"
__license__ = "MIT"

from typing import Any, Dict


def init(config: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Initialize the FINCOUNT application.
    
    Args:
        config: Optional configuration dictionary
        
    Returns:
        Application instance configuration
        
    Example:
        >>> import fincount
        >>> app = fincount.init()
    """
    if config is None:
        config = {}
    
    return {
        "version": __version__,
        "status": "initialized",
        "config": config
    }


__all__ = ["init", "__version__"]
