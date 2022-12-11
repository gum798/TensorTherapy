from Stable_diffusion import *

sd = Stable_diffusion()

# img = sd.txt2img("a photo of an astronaut riding a horse on mars")
img = sd.txt2img("Gogh-style painting of a yellow fox hiding in a green oak forest")
img.save("test.png")
img.show()
