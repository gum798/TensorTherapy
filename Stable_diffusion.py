# !conda install -c conda-forge diffusers
# !conda install transformers
# !conda install scipy
# !pip install --upgrade diffusers transformers scipy

class Stable_diffusion:
    # make sure you're logged in with `huggingface-cli login`
    from diffusers import StableDiffusionPipeline

    def __init__(self):
        self.pipe = self.StableDiffusionPipeline.from_pretrained("./stable-diffusion-v1-5")
        self.pipe = self.pipe.to("mps")
        # Recommended if your computer has < 64 GB of RAM
        self.pipe.enable_attention_slicing()

    def txt2img(self,text):
        _ = self.pipe(text, num_inference_steps=1)
        # Results match those from the CPU device after the warmup pass.
        image = self.pipe(text).images[0]
        return image    