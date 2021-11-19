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


TODO

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

Plutto Ruby SDK is maintained by [plutto](https://https://plutto.cl/).

## License

Plutto Ruby SDK is © 2021 plutto, spa. It is free software and may be redistributed under the terms specified in the LICENSE file.