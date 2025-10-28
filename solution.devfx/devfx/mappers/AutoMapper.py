import devfx.exceptions as exp
from dataclasses import dataclass, is_dataclass
import sqlalchemy as sa
import inspect as inspect


class AutoMapper(object):
    EXCLUDE = object()

    @staticmethod
    def map(destination, source, **assigns):
        if(destination is None):
            raise exp.ArgumentError('destination')
        if(isinstance(destination, type)):
            destination = destination()
    
        if(source is None):
           raise exp.ArgumentError('source')
        if(isinstance(source, type)):
            raise exp.ArgumentError('source')

        if(is_dataclass(destination)):
            destination_attr_names = destination.__dataclass_fields__.keys()
        elif(sa.inspect(destination, False) is not None):
            destination_attr_names = destination.__mapper__.attrs.keys()
        else:
            raise exp.ArgumentError('destination')

        if(is_dataclass(source)):
            source_attr_names = source.__dataclass_fields__.keys()
        elif(sa.inspect(source, False) is not None):
            source_attr_names = source.__mapper__.attrs.keys()
        else:
            raise exp.ArgumentError('source')

        for destination_attr_name in destination_attr_names:
            if((assigns is not None) and (destination_attr_name in assigns)):
                if(callable(assigns[destination_attr_name])):
                    signature = inspect.signature(assigns[destination_attr_name])
                    if(len(signature.parameters) == 1):
                        source_attr_value = assigns[destination_attr_name](source)
                    elif(len(signature.parameters) == 2):
                        source_attr_value = assigns[destination_attr_name](destination, source)
                    else:
                        raise exp.ArgumentError(f'Invalid callable for assign: {destination_attr_name}')
                else:
                    source_attr_value = assigns[destination_attr_name]
                if(source_attr_value is AutoMapper.EXCLUDE):
                    continue
                setattr(destination, destination_attr_name, source_attr_value)
            elif(destination_attr_name in source_attr_names):
                source_attr_value = getattr(source, destination_attr_name)
                setattr(destination, destination_attr_name, source_attr_value)
            else:
                pass

        return destination
            
"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    @dataclass
    class A:
        property1: int = None
        property2: str = None
        property3: float = None
        property4: bool = None

    @dataclass
    class B:
        property1: int = None
        property2: str = None
        property3: float = None
        property4: bool = None
        property5: int = None
        property6: int = None

    print('----1----')
    a = A(1, '2', 3.0, True)
    b = B(0, '', 0.0, False, None, None)
    print('Before mapping:')
    print(a)
    print(b)
    AutoMapper.map(b, a)
    print('After mapping:')
    print(a)
    print(b)

    print('----2----')
    a = A(1, '2', 3.0, True)
    b = B(0, '', 0.0, False, None, None)
    print('Before mapping:')
    print(a)
    print(b)
    AutoMapper.map(b, a, property1=lambda s: AutoMapper.EXCLUDE,
                         property2=AutoMapper.EXCLUDE,
                         property5=lambda s: 2,
                         property6=lambda d, s: s.property1 + s.property3)
    print('After mapping:')
    print(a)
    print(b)

    print('----3----')
    a = A(1, '2', 3.0, True)
    print('Before mapping:')
    print(a)
    b = AutoMapper.map(B, a)
    print('After mapping:')
    print(a)
    print(b)


    

            


        
