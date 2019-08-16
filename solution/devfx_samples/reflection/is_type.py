import devfx.reflection as refl

class BaseTargetArgsX():
    def __init__(self):
        pass

class DerivedTargetArgsX(BaseTargetArgsX):
    def __init__(self):
        pass


if(__name__ == '__main__'):
    x = refl.is_typeof(DerivedTargetArgsX, BaseTargetArgsX)
    print(x)
    x = refl.is_typeof(DerivedTargetArgsX(), BaseTargetArgsX)
    print(x)
    # x = refl.is_typeof(DerivedTargetArgsX, BaseTargetArgsX())
    # print(x)
    # x = refl.is_typeof(DerivedTargetArgsX(), BaseTargetArgsX())
    # print(x)