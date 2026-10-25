import argparse
from neurotribes.render.pygame_renderer import run_game


parser = argparse.ArgumentParser(description="NeuroTribes Evolution Arena")
parser.add_argument("--version", action="version", version="NeuroTribes 0.1.0")
subparsers = parser.add_subparsers(dest="command")
subparsers.add_parser("play")
args = parser.parse_args()

if args.command == "play":
    run_game()