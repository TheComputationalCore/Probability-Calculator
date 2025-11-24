import random
from probability_calculator import Hat, experiment


def test_experiment_probability_range():
    hat = Hat(red=3, blue=2)
    prob = experiment(hat, {"red": 1}, num_balls_drawn=2, num_experiments=200)
    assert 0 <= prob <= 1


def test_experiment_reproducibility():
    random.seed(123)

    hat = Hat(red=5, blue=1)
    prob1 = experiment(hat, {"red": 2}, 3, 100)

    random.seed(123)
    hat = Hat(red=5, blue=1)
    prob2 = experiment(hat, {"red": 2}, 3, 100)

    assert prob1 == prob2  # deterministic


def test_experiment_success_condition():
    hat = Hat(red=5, blue=5)

    prob = experiment(
        hat,
        expected_balls={"red": 1},
        num_balls_drawn=1,
        num_experiments=500,
    )

    # Probability of drawing at least 1 red ball from 10 balls with 5 red = 0.5
    assert 0.3 < prob < 0.7
