import pytest
from probability_calculator import Hat


def test_hat_initialization():
    hat = Hat(red=3, blue=2)
    assert hat.contents.count("red") == 3
    assert hat.contents.count("blue") == 2


def test_hat_draw_less_than_contents():
    hat = Hat(red=3, blue=2)
    drawn = hat.draw(2)
    assert len(drawn) == 2
    assert len(hat.contents) == 3  # remaining balls


def test_hat_draw_all():
    hat = Hat(red=2, blue=1)
    drawn = hat.draw(10)  # draw more than available
    assert len(drawn) == 3
    assert hat.contents == []


def test_hat_randomness_and_removal():
    hat = Hat(red=2, blue=2)
    drawn = hat.draw(3)
    assert len(drawn) == 3
    # ensure no ball appears more times than originally present
    for ball in set(drawn):
        assert drawn.count(ball) <= 2
    assert len(hat.contents) == 1
