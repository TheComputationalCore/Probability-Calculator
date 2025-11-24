import argparse
from .hat import Hat
from .experiment import experiment


def main():
    parser = argparse.ArgumentParser(
        description="Probability Calculator — Monte-Carlo simulation for drawing balls from a hat."
    )

    parser.add_argument(
        "--hat",
        nargs="+",
        help="Colors and counts, e.g. red=3 blue=2",
    )
    parser.add_argument(
        "--expect",
        nargs="+",
        help="Expected ball counts, e.g. red=2 blue=1",
    )
    parser.add_argument("--draw", type=int, help="Number of balls drawn")
    parser.add_argument("--experiments", type=int, help="Number of experiments")

    args = parser.parse_args()

    if not (args.hat and args.expect and args.draw and args.experiments):
        parser.print_help()
        return

    # Convert hat arguments
    hat_kwargs = {}
    for item in args.hat:
        color, count = item.split("=")
        hat_kwargs[color] = int(count)

    expected = {}
    for item in args.expect:
        color, count = item.split("=")
        expected[color] = int(count)

    h = Hat(**hat_kwargs)
    result = experiment(h, expected, args.draw, args.experiments)

    print(f"Estimated Probability: {result:.4f}")


if __name__ == "__main__":
    main()
