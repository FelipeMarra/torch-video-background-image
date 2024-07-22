import torch
import torchvision
import logging
from torchaudio.utils import ffmpeg_utils

torch._logging.set_logs(dynamo = logging.DEBUG)
torch._all.config.verbose = True

print("Library versions:")
print(ffmpeg_utils.get_versions())
print("\nBuild config:")
print(ffmpeg_utils.get_build_config())
print("\nDecoders:")
print([k for k in ffmpeg_utils.get_video_decoders().keys() if "cuvid" in k])
print("\nEncoders:")
print([k for k in ffmpeg_utils.get_video_encoders().keys() if "nvenc" in k])

torchvision.set_video_backend('cuda')