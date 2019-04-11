import sqlalchemy as sa

def cast(expression, type_):
    return sa.cast(expression, type_)


def or_(*args):
    return sa.or_(*args)

def and_(*args):
    return sa.and_(*args)