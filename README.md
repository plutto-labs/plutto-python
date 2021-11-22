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
With this SDK we want to provide a wrapper to the [Plutto API](https://docs.getplutto.com/reference/get_customers) with a very intuitive way of use. All the methods were implemented as in the API documentation, reading it will enable you to use this SDK

### Quickstart
First of all, you will need a [Plutto] account. After creating it, you can get your API key, which will let you to use the `Plutto` object. Then, you're ready to use this awesome SDK!

```python
from plutto import Plutto

client = Plutto("your_api_key")
```

### Managers
How to manage the resources getted by the SDK? Easy, **managers** (_big brain time_). **Managers** are the python objects that will let you work with any resource, obviously, inside the Plutto API. All the existing **managers** are inside the `Plutto` object. These are:
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

Also, if you pass the `lazy=False` parameter, this will force the method of the SDK to return a list of the instances of the resource, instead of the generetors of them. **Disclaimer**: This could take very long if you have a lot of instances to be getted.

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
        "phone": "+56992680522"
    }
}

customer = client.customer.create(**payload)
```

_Note_: this method is only available in `customers` manager

_Note_: this method is only available in `customers` manager

## Testing

TODO

## Publishing

TODO

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Credits

Thank you [contributors](https://github.com/plutto-labs/plutto-python/graphs/contributors)!

Plutto Ruby SDK is maintained by [Plutto](https://plutto.cl/).

## License

Plutto Ruby SDK is © 2021 plutto, spa. It is free software and may be redistributed under the terms specified in the LICENSE file.