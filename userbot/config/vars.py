import os
if os.path.exists("config.py"):
    from config import Development as Config
else:
    from .ubconfig import Config
