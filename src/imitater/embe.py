import argparse

from imitater.model.embed_model import EmbedConfig
from imitater.service.embed import launch_server

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    EmbedConfig.add_cli_args(parser)
    args = parser.parse_args()
    config = EmbedConfig.from_cli_args(args)
    launch_server(config)
