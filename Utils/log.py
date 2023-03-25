from main.constant import isReleaseVersion, app_name


def d_print(string):
    if len(isReleaseVersion()) > 3:
        print(f"{app_name}-{isReleaseVersion()}-{string}")


def i_print(string):
    print(f"{app_name}-{isReleaseVersion()}-{string}")


def w_print(function, string):
    print(f"{app_name}-{function}-warn-{string}")
