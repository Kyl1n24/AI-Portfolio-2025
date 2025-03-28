import sys
import os


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)

from utils.helper_functions import print_llm_response

print_llm_response("What is the capital of France?")  
