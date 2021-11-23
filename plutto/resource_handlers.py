"""Module for the methods that handle the resources."""

from plutto.utils import objetize, objetize_generator


def resource_all(client, path, klass, handlers, methods, resource, params):
    """Fetch all the instances of a resource."""
    lazy = params.pop("lazy", True)
    data = client.request(path, paginated=True, params=params, resource=resource)

    if lazy:
        return objetize_generator(
            data,
            klass,
            client,
            handlers=handlers,
            methods=methods,
            path=path,
        )

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


def resource_create(client, path, klass, handlers, methods, resource, params):
    """Create a new instance of a resource."""
    data = client.request(path, method="post", json=params)[resource]
    return objetize(
        klass,
        client,
        data,
        handlers=handlers,
        methods=methods,
        path=path,
    )


def resource_update(client, path, id_, klass, handlers, methods, resource, params):
    """Update a specific instance of a resource."""
    data = client.request(f"{path}/{id_}", method="patch", json=params)[resource]
    return objetize(
        klass,
        client,
        data,
        handlers=handlers,
        methods=methods,
        path=path,
    )


def resource_delete(client, path, id_, params):
    """Delete a specific instance of a resource."""
    return client.request(f"{path}/{id_}", method="delete", params=params)


def resource_permission(client, path, id_, permission_name, klass, resource, params):
    """Fetch the permissions of a specific instance of a resource."""
    data = client.request(
        f"{path}/{id_}/has_permission/{permission_name}", method="get", params=params
    )[resource]

    return objetize(
        klass,
        client,
        data,
        path=path,
    )


def resource_patch(
    client, path, id_, action, klass, handlers, methods, resource, params
):
    """Patch to a specific endpoint of a resource"""
    data = client.request(f"{path}/{id_}/{action}", method="patch", json=params)[
        resource
    ]
    return objetize(
        klass,
        client,
        data,
        handlers=handlers,
        methods=methods,
        path=path,
    )
