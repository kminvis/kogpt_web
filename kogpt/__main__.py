import sys
import argparse
import logging

from .inference import KoGPTInference


def cli(flags: argparse.Namespace):
    model = KoGPTInference(flags.model, flags.revision, device=flags.device)

    while True:
        prompt = input('prompt> ')
        if not prompt:
            continue
        temperature = float(input('temperature(0.8)> ') or '0.8')
        max_length = int(input('max_length(128)> ') or '128')
        generated = model.generate(prompt, temperature, max_length)
        print(f'{generated}')
        print('')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='KoGPT inference',
        description='KakaoBrain Korean(hangul) Generative Pre-Training Model'
    )
    parser.add_argument('--model', type=str, default='kakaobrain/kogpt', help='huggingface repo (default:kakaobrain/kogpt)')
    parser.add_argument('--revision', type=str, default='KoGPT6B-ryan1.5b', choices=['KoGPT6B-ryan1.5b'])
    parser.add_argument('--device', type=str, default='cuda', choices=['cpu', 'cuda'], help='(default:cuda)')

    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args()

    log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
    level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=level, format=log_format, stream=sys.stderr)

    try:
        cli(args)
    except KeyboardInterrupt:
        print('terminate KakaoBrain Korean(hangul) Generative Pre-Training Model')
