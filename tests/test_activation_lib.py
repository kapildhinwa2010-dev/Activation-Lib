import pytest
import torch
from activation_lib import ActivationLib, create_activation_lib

class TestActivationLib:
    def test_init(self):
        m = ActivationLib(dim=256, hidden_dim=512)
        assert m.dim == 256
    
    def test_forward(self):
        m = ActivationLib(dim=256)
        x = torch.randn(32, 256)
        assert m(x).shape == (32, 256)
    
    def test_factory(self):
        m = create_activation_lib()
        assert isinstance(m, ActivationLib)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
