"""Pytorch Iterate Fast-Gradient attack runner.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
from attacks.attack_random_noise import AttackRandom
from attack_CUB import run_attack

parser = argparse.ArgumentParser(description='Defence')
parser.add_argument('--input_dir', default='/home/sgulshad/sadaf/CUB_experiments/test_split',metavar='DIR',
                    help='Input directory with images.')
parser.add_argument('--output_dir', default='/home/sgulshad/sadaf/CUB_experiments/pytorch-nips2017-attack-example/random_outputep8', metavar='FILE',
                    help='Output directory to save images.')
parser.add_argument('--checkpoint_path', default='/home/sgulshad/sadaf/CUB_experiments/transfer_learn_CUB_Stephan.pth',
                    help='Path to network checkpoint.')
parser.add_argument('--img_size', type=int, default=224, metavar='N',
                    help='Image patch size (default: 224)')
parser.add_argument('--batch_size', type=int, default=16, metavar='N',
                    help='Batch size (default: 32)')
parser.add_argument('--max_epsilon', type=int, default=8, metavar='N',
                    help='Maximum size of adversarial perturbation. (default: 16.0)')
parser.add_argument('--steps', type=int, default=10, metavar='N',
                    help='Number of steps to run attack for')
parser.add_argument('--step_alpha', type=float, default=0.0,
                    help='Per step scaling constant, defaults to epsilon/steps')
parser.add_argument('--norm', default='inf', type=float,
                    help='Gradient norm.')
parser.add_argument('--targeted', action='store_true', default=False,
                    help='Targeted attack')
parser.add_argument('--no_gpu', action='store_true', default=False,
                    help='Disable GPU training')
parser.add_argument('--debug', action='store_true', default=False,
                    help='Enable verbose debug output')


def main():
    args = parser.parse_args()
    attack = AttackRandom(
        targeted=args.targeted,
        max_epsilon=args.max_epsilon,
        norm=args.norm,
        step_alpha=args.step_alpha,
        num_steps=args.steps,
        cuda=not args.no_gpu,
        debug=args.debug)

    run_attack(args, attack)

if __name__ == '__main__':
    main()
