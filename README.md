<h1 align="center">Plutto Python Client</h1>

<p align="center">
  <a href="https://pypi.org/project/plutto" target="_blank">
      <img src="https://img.shields.io/pypi/v/plutto?label=version&logo=python&logoColor=%23fff&color=306998" alt="PyPI - Version">
  </a>

  <a href="https://github.com/plutto-labs/plutto-python/actions?query=workflow%3Atests" target="_blank">
      <img src="https://img.shields.io/github/workflow/status/plutto-labs/plutto-python/tests?label=tests&logo=python&logoColor=%23fff" alt="Tests">
  </a>

  <a href="https://codecov.io/gh/plutto-labs/plutto-python" target="_blank">
      <img src="https://img.shields.io/codecov/c/gh/plutto-labs/plutto-python?label=coverage&logo=codecov&logoColor=ffffff" alt="Coverage">
  </a>

  <a href="https://github.com/plutto-labs/plutto-python/actions?query=workflow%3Alinters" target="_blank">
      <img src="https://img.shields.io/github/workflow/status/plutto-labs/plutto-python/linters?label=linters&logo=github" alt="Linters">
  </a>
</p>

This library will help you easily integrate Plutto API to your software, making your developer life a little bit more enjoyable.


---

## Installation
Install using pip

```bash
$ pip3 install plutto
```
*Note:* This SDK requires [Python 3.7+](https://www.python.org/downloads/release/python-370/)

## Usage
With this SDK we want to provide a wrapper to the [Plutto API](https://docs.getplutto.com/reference) with a very intuitive way of use. All the methods were implemented as in the API documentation, we strongly recommend to read it before using this SDK

### Quickstart
First of all, you will need a [Plutto] account. After creating it, you can get your API key, which will let you to use the `Plutto` object. Then, you're ready to use this awesome SDK!

```python
from plutto import Plutto

client = Plutto("your_api_key")
```

### Managers
To manage the resources retrieved by the SDK we use managers. They are python objects that let you with any object inside Plutto API.. All the existing **managers** are inside the `Plutto` object. These are:
- `customers`
- `invoices`
- `meter_events`
- `permission_groups`
- `products`
- `subscriptions`

#### `all`
_Note_: this method is only available in `customers`, `invoices`, `permission_groups` and `products` managers

```python
customers = client.customers.all()
```

This method returns a **a generator** with all the instances of the customers resource. But, what if the API can recive more params? `kwargs` to the rescue! This way you can pass params like `q[status_eq]` and `q[customer_eq]` to filter the `Invoices`. If you want to get `invoices` with an specific _status_ and _customer_, you need to pass those params to the request
```python
params = {
    "q[status_eq]": "paid",
    "q[customer_eq]": "customer_id"
}
invoices = client.invoices.all(**params)
```

Also, if you pass the `lazy=False` parameter, this will force the method of the SDK to return a list of the instances of the resource, instead of the generetors of them. **Disclaimer**: This could take very long if you have a lot of instances to be retrieved.

```python3
customers = client.customers.all(lazy=False)
isinstance(customers, list) # True
```

#### `get`
_Note_: this method is only available in `customers` and `invoices` managers

This method returns an instance of a resource using it's identifier to find it

```python3
customer = client.customers.get("customer_id")
isinstance(customer, Customer) # True
```

#### `create`
_Note_: this method is only available in `customers`, `meter_events` and `subscriptions` managers

This method creates and returns a new instance of the resource. The attributes of the resource to be created must be passed as `kwargs`. This parameters are specified in the API documentation of the correspondant resource

```python3
payload = {
    "identifier": "your-id_12885305",
    "email": "donald@getplutto.com",
    "name": "Donald",
    "billing_information": {
        "city": "Santiago",
        "country_iso_code": "CL",
        "state": "Metropolitana",
        "address": "Av. Las Condes",
        "zip": "12345",
        "tax_id": "73245432-1",
        "legal_name": "Plutto Inc",
        "activity": "Software Development",
        "phone": "+56912345678"
    }
}

customer = client.customer.create(**payload)
```

#### `update`
_Note_: this method is only available in `customers` manager

```python3
customer = client.cuestomers.update(
    "user_id",
    email="goofy@getplutto.com",
    name="Goofy"
)
```
This is an example of how can be used the update method. The first parameter corresponds to the id of the customer, this way the manager can find the existing resource. Then, the attributes that want to be modified are passed as `kwargs`, this ones are specified in the API in the correspondant resource update method.
This manager method is making two calls to the Plutto API, the first, to get the resource, and the second to update it. Therefore, if you only want to make one API call and already got the reource python object, you can call update directly on the object

```python3
# Get the object
example_customer = client.customers.get("customer_id")

# Update the customer
example_customer.update(
    email="goofy@getplutto.com",
    name="Goofy"
)
```

This way, you can call `update` on the objects you are already working with, evitating to make an innescesary API call and saving some words


#### `delete`
_Note_: this method is only available in `customers` manager

```python3
deleted_customer_id = client.customers.delete("customer_id")
```
This method deletes an existing instance of a resource by it's identifier, and returns it. As in the `update` method, you can call `delete` on an resource object, for the same reasons explained in the previous method

```python3
# Get the resource
customer = client.customers.get("customer_id")

# Delete de resource
deleted_customer_id = customer.delete()
```


### How to use this SDK
The way to use is very similar to the API. For all the methods you need the `Plutto` object

#### `Plutto` object
Instantiate the object using your secret API key
```python3
from plutto import Plutto

client = Plutto("secret_api_key")
```
This client will give you access to all the managers that are available in this SDK. That means you can work with any [manager](#managers) you want from this object

#### `customers` manager

_Available methods_: `all`, `get`, `create`, `update` and `delete`

From the `Plutto` object you can manage your `customers` easily. You can get all the customers that have been created

```python3
customers = client.customers.all()
for customer in customers:
    print(customer.name)
```

Also, if you have the id, you can get a singular customer

```python3
customer = client.customers.get("id_of_the_customer")
```

Need a new customer? Creating it is very intuitive, just pass the [parameters specified in the docs](https://docs.getplutto.com/reference/post_customers) as kwargs

```python3
payload = {
    "email": "donald@getplutto.com",
    "name": "donald",
    "billing_information": {
        "city": "Santiago",
        "country_iso_code": "CL",
        "legal_name": "Plutto",
        "activity": "Software Development"
    }
}

new_customer = client.customers.create(**payload)
```

If any customers need to be updated, you can do it with it's id and pass the params you want to update as kwargs

```python3
update_params = {
    "name": "Goofy",
    "email": "goofy@getplutto.com"
}

updated_customer = client.customers.update("update_customer_id", **update_params)

# It can also be done this way
update_params = {
    "name": "Goofy",
    "email": "goofy@getplutto.com"
}

customer = client.customers.get("update_customer_id")
updated_customer = customer.update(**update_params)
```

Delete a customer can be done by passing it's id to the `delete` method

```python3
deleted_customer_id = client.customers.delete("delete_customer_id")

# It can also be done this way
customer = client.customers.get("delete_customer_id")
deleted_customer_id = customer.delete()
```


#### `invoices` manager

_Available methods_: `all`, `get` and `mark_as`

To get all the existing invoices you can do the following

```python3
invoices = client.invoices.all()

for invoice in invoices:
    print(invoice.id)

# If filtering by params is needed
params = {
    "q[status_eq]": "paid",
    "q[customer_eq]": "customer_id"
}
invoices = client.invoices.all(**params)
```

To get a specific invoice, you can use it's id

```python3
inovice = client.invoices.get("invoice_id")
```

It's possible to change an invoice status through the manager. The possible status are [specified in the docs](https://docs.getplutto.com/reference/patch_invoices-id-mark-as)

```python3
invoice = client.invoices.mark_as("invoice_id", status="paid")
```

#### `meter_events` manager
_Available methods_: Only `create`

It's possible to create a meter event this way

```python3
payload = {
    "customer_id": "example_customer_id",
    "meter_id": "example_meter_id",
    "amout": 100,
    "action": "set"
}
meter_event = client.meter_events.create(**payload)
```


#### `permission_groups` manager
_Available methods_: Only `all`

You can get all the permission groups as follows

```python3
permission_groups = client.permission_groups.all()
for permission_group in permission_groups:
    print(permission_group.name)
```


#### `products` manager
_Available methods_: Only `all`

You can get all the products as follows

```python3
products = client.products.all()
for product in products:
    print(product.name)
```


#### `subscriptions` manager

To create a new subscription through the manager you can do the following. The attributes must be passed as kwargs. Required and optional ones are [specified in the docs](https://docs.getplutto.com/reference/post_subscriptions)

```python3
payload = {
    "customer_id": "example_customer_id",
    "pricing_ids": ["example_pricing_id_1", "example_pricing_id_2"]
    "bills_at": "start",
    "billing_period_duration": "P0Y1M0DT0H0M0S"
}
subscription = client.subscriptions.create(**payload)
```

To end a subscription you only need the id

```python3
subscription = client.subscriptions.end("subscription_id")
```

Adding a product pricing to a subscription

```python3
# pricing_ids can have only one item, but it must be a list
payload = {
    "pricing_ids": ["pricing_id_1", "pricing_id_2", "pricing_id_3"]
}

subscription = client.subscriptions.add_pricings("subscription_id", **payload)
```

To remove a pricing, you can do the following

```python3
# pricing_ids can have only one item, but it must be a list
payload = {
    "pricings_id": ["pricing_id_1", "pricing_id_2", "pricing_id_3"]
}

subscription = client.subscriptions.remove_pricings("subscription_id", **payload)
```


## Serialization
Any resource retrieved by the SDK can be serialize, and it's super easy to do it. You just need to call the `serialize` method, and it's available in any resource

```python3
customer = client.customers.get("customer_id")
serialized_customer = customer.serialize()
```

`serialized_customer` corresponds to a dictionary with only the attributes of the retrieved resource. It can be JSON-serialized


## Testing
All the tests must be added in the `tests/` directory. To run the tests you nedd to execute the following command on the root path of the plutto library

```bash
pytest .
```


Every piece of code modified or added must be tested. The coverage always have to be increased or maintained, this will be checked in all PR

## Publishing

On master/main branch...

1. Change `VERSION` in `plutto//version.py`.
2. Change `Unreleased` title to current version in `CHANGELOG.md`.
3. Commit new release. For example: `Releasing v0.1.0`.
4. Create tag. For example: `git tag v0.1.0`.
5. Push tag. For example: `git push origin v0.1.0`.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Credits

Thank you [contributors](https://github.com/plutto-labs/plutto-python/graphs/contributors)!

Plutto Ruby SDK is maintained by [Plutto](https://getplutto.com).


## Acknowledgments

This SDK was strongly based on the [Fintoc python's SDK](https://github.com/fintoc-com/fintoc-python), designed by [Daniel Leal](https://github.com/daleal)
## License

Plutto Python SDK is © 2021 plutto, spa. It is free software and may be redistributed under the terms specified in the LICENSE file.