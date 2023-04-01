class constant(object):
    __release_ding_url = ""
    __release_ding_secret = ""
    __dev_ding_url = ""
    __dev_ding_secret = ""
    __app_name = ""
    __release = False

    # def isRelease():
    #     return len(isReleaseVersion()) < 3
    #
    #
    # def isReleaseVersion():
    #     re = None
    #     i = -1
    #     # i = 1
    #     if i > 0:
    #         re = ""
    #     else:
    #         re = "debug -- "
    #     return re

    @staticmethod
    def set_release_ding_url(url):
        constant.__release_ding_url = url

    @staticmethod
    def get_release_ding_url():
        return constant.__release_ding_url

    @staticmethod
    def set_release_ding_secret(secret):
        constant.__release_ding_secret = secret

    @staticmethod
    def get_release_ding_secret():
        return constant.__release_ding_secret

    @staticmethod
    def set_dev_ding_url(url):
        constant.__dev_ding_url = url

    @staticmethod
    def get_dev_ding_url():
        return constant.__dev_ding_url

    @staticmethod
    def set_dev_ding_secret(secret):
        constant.__dev_ding_secret = secret

    @staticmethod
    def get_dev_ding_secret():
        return constant.__dev_ding_secret

    @staticmethod
    def set_app_name(app_name):
        constant.__app_name = app_name

    @staticmethod
    def get_app_name():
        return constant.__app_name

    @staticmethod
    def set_release(release):
        constant.__release = release

    @staticmethod
    def is_release():
        return constant.__release

    @staticmethod
    def is_release_version():
        if constant.__release:
            return ""
        else:
            return "debug $$ -"


