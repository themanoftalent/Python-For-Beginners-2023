from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "[" in window and "0" in window and "]" in window:
        passed()
    else:
        failed("Use indexing")

def test_value():
    file = import_task_file()
    if hasattr(file, "p_letter") and file.p_letter == "P":
        passed()
    else:
        failed("String index starts at 0.")


if __name__ == '__main__':
    run_common_tests()

    test_value()
    test_window()
