from enum import Enum
from dataclasses import dataclass
from typing import List
from sqlalchemy import select, delete, func, text, and_
import devfx.core as core

class StatementKind(Enum):
    NONE = 0
    SAVE = 1
    SELECT = 2
    DELETE = 3

class StandardDbCtrl:
    def __init__(self, session):
        self.__session = session
        self.__statement = None
        self.__statement_kind = StatementKind.NONE

    # ----------------------------------------------------------------
    def save(self, instance, check_columns=None):
        if(self.__statement_kind is not StatementKind.NONE):
            raise Exception(f'You are trying to save an instance while the statement is a not NONE statement kind: {self.__statement_kind}')
        self.__statement_kind = StatementKind.SAVE

        pk_column_names = [column.name for column in instance.__mapper__.primary_key]
        if(check_columns is None):
            match_column_names = pk_column_names
        else:
            match_column_names = [check_column if(isinstance(check_column, str)) else check_column.name for check_column in check_columns]    
        match_column_key_value_pairs = {match_column_name: getattr(instance, match_column_name) for match_column_name in match_column_names}
        match_condition = and_(*[getattr(instance.__class__, key) == value for (key, value) in match_column_key_value_pairs.items()])
        matched_instance = self.__session.query(instance.__class__).filter(match_condition).one_or_none()
        if (matched_instance is not None):
            for attr in instance.__mapper__.attrs.keys():
                if(check_columns is None):
                    if(attr in pk_column_names):
                        continue
                else:
                    if((attr in pk_column_names) or (attr in match_column_names)):
                        continue
                setattr(matched_instance, attr, getattr(instance, attr))
            self.__session.commit()
            return {pk_column_name: getattr(matched_instance, pk_column_name) for pk_column_name in pk_column_names}
        else:
            self.__session.add(instance)
            self.__session.commit()
            return {pk_column_name: getattr(instance, pk_column_name) for pk_column_name in pk_column_names}

    # ----------------------------------------------------------------  
    def insert(self, __class__, **assigns):
        if(self.__statement_kind is not StatementKind.NONE):
            raise Exception(f'You are trying to save an instance while the statement is a not NONE statement kind: {self.__statement_kind}')
        self.__statement_kind = StatementKind.SAVE

        instance = __class__()
        for (assign_name, assign_value) in assigns.items():
            setattr(instance, assign_name, assign_value)
        self.__session.add(instance)
        self.__session.commit()
        return instance
        
    def update(self, __class__, criteria, **assigns):
        if(self.__statement_kind is not StatementKind.NONE):
            raise Exception(f'You are trying to update an instance while the statement is a not NONE statement kind: {self.__statement_kind}')
        self.__statement_kind = StatementKind.SAVE

        if(isinstance(criteria, list)):
            criteria = and_(*criteria)
        else:
            criteria = criteria
        matched_instances = self.__session.query(__class__).filter(criteria).all()
        for matched_instance in matched_instances:
            for (assign_name, assign_value) in assigns.items():
                setattr(matched_instance, assign_name, assign_value)
        self.__session.commit()
        return matched_instances
    
    def iu(self, __class__, criteria, **assigns):
        if(self.__statement_kind is not StatementKind.NONE):
            raise Exception(f'You are trying to update an instance while the statement is a not NONE statement kind: {self.__statement_kind}')
        self.__statement_kind = StatementKind.SAVE

        if(isinstance(criteria, list)):
            criteria = and_(*criteria)
        else:
            criteria = criteria
        matched_instance = self.__session.query(__class__).filter(criteria).one_or_none()
        if(matched_instance is not None):
            attr_names = __class__.__mapper__.attrs.keys()
            for (assign_name, assign_value) in assigns.items():
                if(assign_name not in attr_names):
                    raise Exception(f'You are trying to update an instance {__class__} with an attribute that does not exist: {assign_name}')
                setattr(matched_instance, assign_name, assign_value)
            self.__session.commit()
            return matched_instance
        else:
            instance = __class__()
            attr_names = __class__.__mapper__.attrs.keys()
            for (assign_name, assign_value) in assigns.items():
                if(assign_name not in attr_names):
                    raise Exception(f'You are trying to update an instance {__class__} with an attribute that does not exist: {assign_name}')
                setattr(instance, assign_name, assign_value)
            self.__session.add(instance)
            self.__session.commit()
            return instance        
                   
    # ----------------------------------------------------------------          
    def select(self, *expressions):
        if(self.__statement_kind is not StatementKind.NONE):
            raise Exception(f'You are trying to save an instance while the statement is a not NONE statement kind: {self.__statement_kind}')
        self.__statement_kind = StatementKind.SELECT
        
        self.__statement = select(*expressions)
        return self   
    
    def select_max(self, *expressions):
        if(self.__statement_kind is not StatementKind.NONE):
            raise Exception(f'You are trying to save an instance while the statement is a not NONE statement kind: {self.__statement_kind}')
        self.__statement_kind = StatementKind.SELECT
        
        self.__statement = select(func.max(*expressions))
        return self  

    def select_min(self, *expressions):
        if(self.__statement_kind is not StatementKind.NONE):
            raise Exception(f'You are trying to save an instance while the statement is a not NONE statement kind: {self.__statement_kind}')
        self.__statement_kind = StatementKind.SELECT
        
        self.__statement = select(func.min(*expressions))
        return self  
               
    def distinct(self, *expressions):
        self.__statement = self.__statement.distinct(*expressions)
        return self
                  
    def join(self, *expressions):
        self.__statement = self.__statement.join(*expressions)
        return self
    
    def where(self, *expressions):
        for expression in expressions:
            if(expression is None):
                pass
            else:
                if(isinstance(expression, list)):
                    criteria = expression
                    for criterion in criteria:
                        self.__statement = self.__statement.where(criterion)
                else:
                    criterion = expression
                    self.__statement = self.__statement.where(criterion)
        return self
    
    def order_by(self, *expressions):
        for expression in expressions:
            if(expression is None):
                pass
            else:
                if(isinstance(expression, str)):
                    self.__statement = self.__statement.order_by(text(expression))
                else:
                    self.__statement = self.__statement.order_by(expression)
        return self

    def limit(self, limit):
        self.__statement = self.__statement.limit(limit)
        return self
    
    def offset(self, offset):
        self.__statement = self.__statement.offset(offset)
        return self
    
    def group_by(self, *expressions):
        self.__statement = self.__statement.group_by(*expressions)
        return self
    
    def having(self, *expressions):
        for expression in expressions:
            if(expression is None):
                pass
            else:
                if(isinstance(expression, list)):
                    criteria = expression
                    for criterion in criteria:
                        self.__statement = self.__statement.having(criterion)
                else:
                    criterion = expression
                    self.__statement = self.__statement.having(criterion)
        return self

    # ---------------------------------------------------------------- 
    def execute(self):
        result = self.__session.execute(self.__statement)
        return result
        
    # ---------------------------------------------------------------- 
    def all(self):
        if(self.__statement_kind is not StatementKind.SELECT):
            raise Exception(f'You are trying to get all elements while the statement is not a SELECT statement kind: {self.__statement_kind}')
        
        return self.__session.execute(self.__statement).scalars().all()
        
    def count(self):
        if(self.__statement_kind is not StatementKind.SELECT):
            raise Exception(f'You are trying to get the count while the statement is not a SELECT statement kind: {self.__statement_kind}')
        
        return self.__session.execute(select(func.count()).select_from(self.__statement)).scalar()
    
    def exists(self):
        if(self.__statement_kind is not StatementKind.SELECT):
            raise Exception(f'You are trying to check if exists while the statement is not a SELECT statement kind: {self.__statement_kind}')
        
        return  self.__session.execute(select(func.count()).select_from(self.__statement)).scalar() > 0

    
    def page(self, page_size, page_number):
        if(self.__statement_kind is not StatementKind.SELECT):
            raise Exception(f'You are trying to get a page while the statement is not a SELECT statement kind: {self.__statement_kind}')
        
        instances = self.__session.execute(self.__statement.limit(page_size).offset((page_number-1)*page_size)).scalars().all()
        instance_count = self.__session.execute(select(func.count()).select_from(self.__statement)).scalar()
        @dataclass
        class Page:
            instances: List = None
            instance_count: int = None
        return Page(instances, instance_count)
    

    def scalar(self):
        if(self.__statement_kind is not StatementKind.SELECT):
            raise Exception(f'You are trying to get a scalar while the statement is not a SELECT statement kind: {self.__statement_kind}')
        
        return self.__session.execute(self.__statement).scalar()
    
    def scalar_one(self):
        if(self.__statement_kind is not StatementKind.SELECT):
            raise Exception(f'You are trying to get a scalar while the statement is not a SELECT statement kind: {self.__statement_kind}')
        
        return self.__session.execute(self.__statement).scalar_one()
    
    def scalar_one_or_none(self):
        if(self.__statement_kind is not StatementKind.SELECT):
            raise Exception(f'You are trying to get a scalar while the statement is not a SELECT statement kind: {self.__statement_kind}')
        
        return self.__session.execute(self.__statement).scalar_one_or_none()

    
    def first(self):
        if(self.__statement_kind is not StatementKind.SELECT):      
            raise Exception(f'You are trying to get the first element while the statement is not a SELECT statement kind: {self.__statement_kind}')
        
        return self.__session.execute(self.__statement.limit(1)).scalars().first()
       
    
    def one(self):
        if(self.__statement_kind is not StatementKind.SELECT):
            raise Exception(f'You are trying to get the one element while the statement is not a SELECT statement kind: {self.__statement_kind}')
        
        return self.__session.execute(self.__statement).scalars().one()
    
    def one_or_none(self):
        if(self.__statement_kind is not StatementKind.SELECT):
            raise Exception(f'You are trying to get the one element while the statement is not a SELECT statement kind: {self.__statement_kind}')
        
        return self.__session.execute(self.__statement).scalars().one_or_none()
    
    def delete(self):
        if(self.__statement_kind is not StatementKind.SELECT):
            raise Exception(f'You are trying to get the one element while the statement is not a SELECT statement kind: {self.__statement_kind}')
        self.__statement_kind = StatementKind.DELETE
        
        primary__class__ = self.__statement.froms[0] 
        if(self.__statement.whereclause is None):
            self.__statement = delete(primary__class__)
        else:
            self.__statement = delete(primary__class__).where(self.__statement.whereclause)
        self.__session.execute(self.__statement)
        self.__session.commit()

    # ---------------------------------------------------------------- 
    def query(self):
        return self.__session.query(self.__statement)
    
    

    

    
    

    
    


    

    


    



