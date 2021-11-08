from importlib import import_module

def singularize(string):
    """Remove the last 's' from a string if exists."""
    return string.rstrip("s")

def pluralize(string):
    """Add an 's' to a string if it doesn't already end with 's'."""
    if string.endswith("s"):
        return string
    return string + "s"

def snake_to_pascal(snake_string):
    """Convert a snake_case string to PascalCase."""
    return ''.join(word.title() for word in snake_string.split('_'))

def get_resource_class(snake_resource_name, value={}):
    """
    Get the class that corresponds to a resource using its
    name (in snake case) and it's value.
    """
    if isinstance(value, dict):
        module = import_module("plutto.resources")
        try:
            return getattr(module, snake_to_pascal(snake_resource_name))
        except AttributeError:
            return getattr(module, "GenericPluttoResource")
    return type(value)

def objetize(klass, client, data, handlers={}, methods=[], path=None):
    """Transform the :data: object into an object with class :klass:"""
    if data is None:
        return None
    if klass in [str, int, dict, float, bool]:
        return klass(data)
    return klass(client, handlers, methods, path, **data)
