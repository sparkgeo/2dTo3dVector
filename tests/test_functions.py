import functions
import pytest

@pytest.mark.parametrize('x, y, result', 
[
    (7, 'Test', 10),
    ('Hello ', 'World', 'Hello World'),
    (10.5, 25.5, 36)
]
)
                         
def test_add(x, y, result, mock_data):
    print(mock_data)
    assert functions.add(x, y) == result
    
    
# def test_product():
    # assert functions.product(7,3) == 21