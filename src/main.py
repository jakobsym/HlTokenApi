from util.config import config_logging
from pathlib import Path

def main():
    config_logging()
    #config_path = Path(__file__).parent.parent / "src" / "util" / "logging.yaml"
    #print(config_path)

if __name__ == "__main__":
    main()