import pytest
import os
from unittest.mock import patch, MagicMock
from PHIreader import PhiModel, PromptProcessor  



@pytest.fixture
def phi_model():
    return PhiModel(model_name="phi3.5")


@pytest.fixture
def mock_response():
    # Return a mock response to simulate PHI model output
    return "Positive"


@patch('ollama.chat')  # Mocking the Ollama chat function
def test_generate_response(mock_chat, phi_model, mock_response):
    # Mock the stream to return a simulated response
    mock_chat.return_value = [{"message": {"content": mock_response}}]

    
    prompt = "The product was excellent!"
    response = phi_model.generate_response(prompt)

    # Test that the response contains the expected output
    assert "Positive" in response.strip()


# Test the PromptProcessor class
@pytest.fixture
def mock_file_data():
    # Return a string representing the content of a review file
    return """
    Review ID: 123
    Review Content: The product was excellent!
    """


@pytest.fixture
def prompt_processor(mock_file_data, phi_model):
    # Create a temporary file with mock review data
    with open("test_reviews.txt", "w", encoding="utf-8") as f:
        f.write(mock_file_data)

    # Initialize PromptProcessor with mock data
    return PromptProcessor(output_file="test_output.txt", model=phi_model, additional_directory=".")


@patch('PHIreader.PromptProcessor.generate_master_chart')
@patch('ollama.chat')
def test_process_prompts(mock_chat, mock_generate_chart, prompt_processor, mock_response):
    # Mock the chat response
    mock_chat.return_value = [{"message": {"content": mock_response}}]

    # Run the processing method
    prompt_processor.process_prompts()

    # Verify that the output file contains the expected sentiment response
    with open("test_output.txt", "r", encoding="utf-8") as f:
        output = f.read()

    assert "Positive" in output

    # Verify that the master chart generation was called
    mock_generate_chart.assert_called_once()


# Test sentiment counts
@pytest.fixture
def sentiment_processor(phi_model):
    return PromptProcessor(output_file="test_output_sentiment.txt", model=phi_model, additional_directory=".")


@patch('ollama.chat')
def test_sentiment_counts(mock_chat, sentiment_processor, mock_response):
    # Simulating a set of responses with different sentiments
    mock_chat.return_value = [{"message": {"content": "Positive"}}]

    sentiment_processor.process_prompts()

    # Verify the sentiment data in the file
    assert sentiment_processor.file_sentiment_data[0]['positive'] == 1  # Direct comparison



# Cleanup after tests
def teardown_module(module):
    # Remove temporary files after testing
    if os.path.exists("test_reviews.txt"):
        os.remove("test_reviews.txt")
    if os.path.exists("test_output.txt"):
        os.remove("test_output.txt")
    if os.path.exists("test_output_sentiment.txt"):
        os.remove("test_output_sentiment.txt")
    if os.path.exists("sentiment_analysis_master_chart.png"):
        os.remove("sentiment_analysis_master_chart.png")


if __name__ == "__main__":
    pytest.main()
