from test_helper import run_common_tests, failed, passed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if not file.is_equal:
        passed()
    else:
        failed("Use == operator")


def test_window():
    window = get_answer_placeholders()[0]
    if "==" in window:
        passed()
    else:
        failed("Use == operator")



if __name__ == '__main__':
    run_common_tests("You should modify the file")

    test_value()
    test_window()