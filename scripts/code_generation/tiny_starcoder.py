import torchvision

torchvision.disable_beta_transforms_warning()

from transformers import pipeline


class TextGenerator:
    def __init__(self, modelName="bigcode/tiny_starcoder_py", padTokenID=50256):
        # Load the text generation pipeline with the specified model
        self.pipe = pipeline("text-generation", model=modelName, pad_token_id=padTokenID)

    def predictText(self, prompt, maxLength=150):
        """Generate text based on the input prompt."""
        generated = self.pipe(prompt, max_length=maxLength, num_return_sequences=1, truncation=True)
        return generated[0]["generated_text"]
