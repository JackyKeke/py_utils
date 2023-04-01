from py_utils.Utils import constant


def d_print(string):
    if len(constant.constant.is_release_version()) > 3:
        print(f"{constant.constant.get_app_name()}-{constant.constant.is_release_version()}-{string}")


def i_print(string):
    print(f"{constant.constant.get_app_name()}-{constant.constant.is_release_version()}-{string}")


def w_print(function, string):
    print(f"{constant.constant.get_app_name()}-{function}-warn-{string}")
