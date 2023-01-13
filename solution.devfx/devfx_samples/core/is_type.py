import devfx.core as core

class BaseTargetArgsX():
    def __init__(self):
        pass

class DerivedTargetArgsX(BaseTargetArgsX):
    def __init__(self):
        pass


if(__name__ == '__main__'):
    x = core.is_typeof(DerivedTargetArgsX, BaseTargetArgsX)
    print(x)
    x = core.is_typeof(DerivedTargetArgsX(), BaseTargetArgsX)
    print(x)
    # x = core.is_typeof(DerivedTargetArgsX, BaseTargetArgsX())
    # print(x)
    # x = core.is_typeof(DerivedTargetArgsX(), BaseTargetArgsX())
    # print(x)