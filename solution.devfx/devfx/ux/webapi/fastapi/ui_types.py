"""
UI Type Enumerations
All enum types for UI metadata and field configuration
"""

from enum import Enum


class DataType(str, Enum):
    """Data type values for field metadata"""
    String = "string"
    Number = "number"
    Integer = "integer"
    Boolean = "boolean"
    Date = "date"
    DateTime = "datetime"
    Time = "time"
    Array = "array"
    Object = "object"
    Null = "null"


class SemanticType(str, Enum):
    """Semantic type indicating the meaning/purpose of data"""
    Email = "email"
    Phone = "phone"
    Url = "url"
    Currency = "currency"
    Percentage = "percentage"
    Color = "color"
    Image = "image"
    File = "file"
    Password = "password"
    IpAddress = "ipAddress"
    CreditCard = "creditCard"
    PostalCode = "postalCode"
    Country = "country"
    Language = "language"
    Timezone = "timezone"


class InputType(str, Enum):
    """Input control types for form fields"""
    Text = "text"
    Number = "number"
    Email = "email"
    Password = "password"
    Tel = "tel"
    Url = "url"
    Search = "search"
    Textarea = "textarea"
    Select = "select"
    Multiselect = "multiselect"
    Checkbox = "checkbox"
    Radio = "radio"
    Switch = "switch"
    Date = "date"
    Time = "time"
    DateTime = "datetime"
    DateRange = "dateRange"
    Color = "color"
    File = "file"
    Image = "image"
    Range = "range"
    Slider = "slider"
    Rating = "rating"
    Hidden = "hidden"


class DisplayType(str, Enum):
    """Display rendering types for read-only or table view"""
    Text = "text"
    Badge = "badge"
    Tag = "tag"
    Label = "label"
    Link = "link"
    Image = "image"
    Icon = "icon"
    Avatar = "avatar"
    Progress = "progress"
    Chart = "chart"
    Code = "code"
    Html = "html"
    Markdown = "markdown"
    Json = "json"
    Boolean = "boolean"
    Date = "date"
    DateTime = "datetime"
    Time = "time"
    Currency = "currency"
    Percentage = "percentage"
    List = "list"
    Chip = "chip"


class FormatType(str, Enum):
    """Format types for data display"""
    Currency = "currency"
    Percentage = "percentage"
    Decimal = "decimal"
    Integer = "integer"
    Date = "date"
    Time = "time"
    DateTime = "datetime"
    Email = "email"
    Phone = "phone"
    Url = "url"
    Uppercase = "uppercase"
    Lowercase = "lowercase"
    Capitalize = "capitalize"
    Truncate = "truncate"
    Ellipsis = "ellipsis"
    Custom = "custom"


class AlignType(str, Enum):
    """Alignment types for text and content"""
    Left = "left"
    Center = "center"
    Right = "right"
    Justify = "justify"
    Start = "start"
    End = "end"


class UiHint(str, Enum):
    """UI Hint property keys for field metadata"""
    # Core
    Root = "uiHints"
    Label = "label"
    Order = "order"
    
    # Display & Layout
    Width = "width"
    Height = "height"
    Visible = "visible"
    Hidden = "hidden"
    
    # Input Control
    Placeholder = "placeholder"
    DefaultValue = "defaultValue"
    ReadOnly = "readOnly"
    Disabled = "disabled"
    Required = "required"
    Tooltip = "tooltip"
    
    # Formatting & Type
    DataType = "dataType"
    SemanticType = "semanticType"
    InputType = "inputType"
    DisplayType = "displayType"
    Format = "format"
          
    # Styling & CSS
    Style = "style"
    
    # Table/Grid specific
    Sortable = "sortable"
    Filterable = "filterable"
    Searchable = "searchable"
    Align = "align"
