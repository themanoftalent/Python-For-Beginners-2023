from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "prime" in window and "for " in window and "primes" in window and " in " in window:
        passed()
    else:
        failed("Use for loop to iterate over 'primes'")


if __name__ == '__main__':
    run_common_tests()
    test_window()