import functools
import sys
import os
from typing import List, Optional

def ghost(
    export_html: bool = False,
    depth: int = 1,
    suppress: bool = False,
    mask_vars: Optional[List[str]] = None,
    log_memory: bool = False,
    report_type: str = "terminal"
):
    """
    The Flight Recorder decorator. 
    Stays silent until an exception occurs, then generates a forensic report.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Placeholder for forensic report logic
                print(f"\nCHAOS REPORT: {func.__name__} failed!")
                print(f"Error: {type(e).__name__}(\"{e}\")")
                
                if not suppress:
                    raise
        return wrapper
    return decorator
