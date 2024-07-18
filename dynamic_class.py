# Create a class dynamically

def create_class(class_name:str) -> object:
    """
    Creates a new class dynamically with the given `class_name` and returns it.

    Args:
        class_name (str): The name of the class to be created.

    Returns:
        object: A new class object with the given `class_name` and the attributes defined in `class_attributes`.

    Example:
        >>> create_class('MyClass')
        <class '__main__.MyClass'>
    """
    # Define your attributes
    class_attributes = {
        'attribute1': 'value1',
        'attribute2': 'value2'
    }
    
    # Create a class dynamically
    NewClass = type(class_name, (), class_attributes)
    return NewClass

# Create the class dynamically
DynamicClass = create_class(class_name='Example1')

# Now you can use DynamicClass
instance = DynamicClass()

# Access attributes
print(DynamicClass.__name__)  # Output: Example
print(instance.attribute1)  # Output: value1
print(instance.attribute2)  # Output: value2