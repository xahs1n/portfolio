import sys
import os

# Add your project directory to the sys.path
path = '/home/YOUR_PYTHONANYWHERE_USERNAME/YOUR_PROJECT_FOLDER'
if path not in sys.path:
    sys.path.append(path)

from ai import app as application
