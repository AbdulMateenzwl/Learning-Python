"""
Decorators module for data processing functions.
Provides timing, logging, and performance monitoring decorators.
"""

import time
import logging
from functools import wraps
from typing import Callable, TypeVar, cast, Any
from datetime import datetime

# Type variable for generic decorator support
F = TypeVar('F', bound=Callable[..., Any])


def timing_decorator(func: F) -> F:
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        
        # Record start time with high precision
        start_time = time.perf_counter()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Calculate execution time
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            
            logger.info(
                f"{func.__name__}() completed in {execution_time:.4f}s"
            )
            
            return result
            
        except Exception as e:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            
            logger.error(
                f"{func.__name__}() failed after {execution_time:.4f}s"
            )
            logger.error(f"Error: {type(e).__name__}: {e}")
            raise

        finally:
            logger.debug(f"{func.__name__}() completed at {datetime.now().strftime('%H:%M:%S')}")
    
    return cast(F, wrapper)

