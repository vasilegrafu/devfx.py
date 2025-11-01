"""
BaseEntityView for FastAPI entities
Provides standard Pydantic configuration and JSON schema customization
"""

from pydantic import BaseModel, ConfigDict


class BaseEntityView(BaseModel):
    """
    Base model for all FastAPI entity views.
    
    Provides:
    - Standard Pydantic configuration (validation, ORM support, etc.)
    - Clean JSON schema generation (removes titles, cleans up Decimal patterns)
    - Consistent behavior across all entities
    
    Usage:
        class MyEntityView(BaseEntityView):
            id: int | None = Field(default=None)
            name: str | None = Field(default=None)
    """
    
    model_config = ConfigDict(
        # Allow construction from ORM objects or dataclass instances
        from_attributes=True,
        # Use enum values instead of enum objects in serialization
        use_enum_values=True,
        # Validate data on assignment (not just construction)
        validate_assignment=True,
        # Validate default values
        validate_defaults=True,
        # Extra fields are forbidden
        extra="forbid",
    )
    
    @classmethod
    def model_json_schema(cls, **kwargs):
        """
        Override to remove 'title' from all field definitions and clean up Decimal patterns.
        
        This produces cleaner OpenAPI/JSON Schema output:
        - No redundant 'title' fields (they just duplicate the property name)
        - No complex regex patterns for Decimal fields (keeps simple type definitions)
        """
        schema = super().model_json_schema(**kwargs)
        
        # Remove title from each property and clean up Decimal regex patterns
        if 'properties' in schema:
            for field_name, field_schema in schema['properties'].items():
                field_schema.pop('title', None)
                
                # Remove the auto-generated regex pattern from Decimal fields
                # Keep only the simple type definitions
                if 'anyOf' in field_schema:
                    field_schema['anyOf'] = [
                        item for item in field_schema['anyOf'] 
                        if 'pattern' not in item  # Remove items with regex patterns
                    ]
        
        return schema
