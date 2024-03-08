import argparse

from imitater.service.app import launch_server

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", type=str, required=True, help="Path to config file.")
    args = parser.parse_args()
    launch_server(getattr(args, "config"))
