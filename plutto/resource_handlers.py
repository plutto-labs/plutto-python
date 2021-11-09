"""Module for the methods that handle the resources."""

from plutto.utils import objetize

def resource_all(client, path, klass, handlers, methods, resource, params):
    """Fetch all the instances of a resource."""
    # paginated = True does nothing for now
    # lazy does nothing for now
    lazy = params.pop("lazy", True)
    data = client.request(path, paginated=False, params=params)[resource]
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


def resource_get(client, path, id_, klass, handlers, methods, resource, params):
    """Fetch a specific instance of a resource."""
    data = client.request(f"{path}/{id_}", method="get", params=params)[resource]
    return objetize(
        klass,
        client,
        data,
        handlers=handlers,
        methods=methods,
        path=path,
    )


def resource_create(client, path, klass, handlers, methods, params):
    """Create a new instance of a resource."""
    data = client.request(path, method="post", json=params)
    return objetize(
        klass,
        client,
        data,
        handlers=handlers,
        methods=methods,
        path=path,
    )


