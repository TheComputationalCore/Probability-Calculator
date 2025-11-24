import copy


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Perform a Monte-Carlo simulation to estimate the probability that
    drawing a number of balls will contain at least the expected counts.

    Args:
        hat (Hat): original hat
        expected_balls (dict): e.g. {"red": 2, "blue": 1}
        num_balls_drawn (int)
        num_experiments (int)

    Returns:
        float: probability between 0 and 1
    """
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count drawn colors
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        # Check success condition
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments
