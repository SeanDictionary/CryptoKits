import sys
import importlib.util

def is_sage():
    """检查当前环境是否为 SageMath"""
    try : 
        import sage.all
        return True
    except:
        raise ImportError("Error: the function is need to run on SageMath.")
