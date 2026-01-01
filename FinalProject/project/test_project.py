from project import normalize_text, detect_intent, should_exit


def test_normalize_text():
    assert normalize_text("Hello!!!") == "hello"
    assert normalize_text("How   are you?") == "how are you"
    assert normalize_text("Rock-Paper-Scissors") == "rockpaperscissors"


def test_detect_intent():
    assert detect_intent(["hello"]) == "greeting"
    assert detect_intent(["play"]) == "play"
    assert detect_intent(["bye"]) == "goodbye"
    assert detect_intent(["unknownword"]) == "unknown"


def test_should_exit():
    assert should_exit("goodbye") is True
    assert should_exit("greeting") is False
    assert should_exit("play") is False
