import pytest  
from src.area import calculate_area_square  
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])

def test_calculate_area_square_custom_output():
    # Use the last two digits of your student ID (100898513) as the expected output
    expected_output = 13

    # Calculate the area of a square using the last two digits of your student ID as the length
    result = calculate_area_square(expected_output)

    # Validate that the result matches the expected output
    assert result == expected_output * expected_output
