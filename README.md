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


## Testing
To run the tests you nedd to execute the following command on the root path of the plutto library

```bash
pytest .
```


Every piece of code modified or added must be tested. The coverage always have to be increased or maintained, this will be checked in all PR

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