from neurotribes.utils import clamp

def test_clamp_below():
    assert clamp(-10, 0, 100) == 0
def test_clamp_above():
    assert clamp(150, 0, 100) == 100
def test_clamp_inside():
    assert clamp(50, 0, 100) == 50
def test_clamp_different_bounds():
    assert clamp(10, 20, 80) == 20