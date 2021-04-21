import os
from dotenv import load_dotenv

load_dotenv()

class WindowConfig():
	WINDOW_DURATION = int(os.getenv("WINDOW_DURATION"))
	SLIDE_DURATION = int(os.getenv("SLIDE_DURATION"))