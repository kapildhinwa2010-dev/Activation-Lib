# Activation-Lib

[![CI](https://github.com/kapildhinwa2010-dev/Activation-Lib/actions/workflows/ci.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/Activation-Lib/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kapildhinwa2010-dev/Activation-Lib/actions/workflows/codeql.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/Activation-Lib/actions/workflows/codeql.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.0+](https://img.shields.io/badge/pytorch-2.0+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

**Activation library**

Professional implementation of Activation-Lib for research and production use.

## Installation

```bash
pip install Activation-Lib
```

## Usage

```python
import torch
from activation_lib import ActivationLib

module = ActivationLib(dim=256, hidden_dim=512)
output = module(torch.randn(32, 256))
```

## License

MIT License
