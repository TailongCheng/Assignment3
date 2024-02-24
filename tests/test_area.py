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

def test_calculate_area_square_negative_input():
    # Choose a negative number as input
    input_value = -5

    # Calculate the area of a square using the negative input
    result = calculate_area_square(input_value)

    # This assertion will fail because the function should raise a TypeError for negative input
    assert result == input_value * input_value
