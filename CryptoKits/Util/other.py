import sys
import importlib.util
import inspect

def is_sage():
    """检查当前环境是否为 SageMath"""
    try : 
        import sage.all
        return True
    except:
        return False
        