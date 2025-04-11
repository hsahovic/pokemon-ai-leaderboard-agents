from poke_env import AccountConfiguration, ServerConfiguration
from poke_env.player import SimpleHeuristicsPlayer
import argparse
import asyncio

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, default="challenge")
    parser.add_argument("--opponent", type=str, default=None)
    parser.add_argument("--name", type=str)
    parser.add_argument("--n_battles", type=int, default=1)
    args = parser.parse_args()

    assert (args.opponent is not None) or (args.mode == "accept_challenge"), "Opponent must be provided if mode is challenge"
    assert args.name is not None, "Name must be provided"
    assert args.n_battles > 0, "Number of battles must be greater than 0"

    account_config = AccountConfiguration(
        username=args.name,
        password=None,
    )
    server_config = ServerConfiguration(
        websocket_url="ws://host.docker.internal:8000/showdown/websocket",
        authentication_url="https://play.pokemonshowdown.com/action.php?",
    )

    player = SimpleHeuristicsPlayer(account_configuration=account_config, server_configuration=server_config, log_level=20)
    
    if args.mode == "challenge":
        asyncio.run(player.send_challenges(args.opponent, args.n_battles))
    elif args.mode == "accept_challenge":
        asyncio.run(player.accept_challenges(args.opponent, args.n_battles))
    else:
        raise ValueError(f"Invalid mode: {args.mode}")
