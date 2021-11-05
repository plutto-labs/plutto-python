"""Module for the methods that handle the resources."""

from plutto.utils import objetize

def resource_all(client, path, klass, handlers, methods, resource, params):
    """Fetch all the instances of a resource."""
    # paginated = True does nothing for now
    # lazy does nothing for now
    lazy = params.pop("lazy", True)
    data = client.request(path, paginated=True, params=params)[resource]
    if lazy:
        pass

    return [
        objetize(
            klass,
            client,
            element,
            handlers=handlers,
            methods=methods,
            path=path,
        )
        for element in data
    ]
