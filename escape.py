ESC = "\x1b"
CSI = f"{ESC}["

BOLD = f"{CSI}1m"

RESET = f"{CSI}0m" 
import sys

sys.stdout.write(BOLD)

sys.stdout.write("hello world")
sys.stdout.write(RESET)