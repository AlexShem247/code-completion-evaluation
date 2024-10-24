import torchvision

torchvision.disable_beta_transforms_warning()

from transformers import pipeline


class TextGenerator:
    def __init__(self, model_name="bigcode/tiny_starcoder_py", pad_token_id=50256):
        # Load the text generation pipeline with the specified model
        self.pipe = pipeline("text-generation", model=model_name, pad_token_id=pad_token_id)

    def predict_text(self, prompt, max_length=50):
        """Generate text based on the input prompt.

        Args:
            prompt (str): The input prompt for text generation.
            max_length (int): The maximum length of the generated text.

        Returns:
            str: The generated text.
        """
        generated = self.pipe(prompt, max_length=80, num_return_sequences=1, truncation=True)
        return generated[0]["generated_text"]  # Return the generated text
