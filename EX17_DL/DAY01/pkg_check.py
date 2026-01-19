import torch

if torch.cuda.is_available():
    print(f'Current Device : {torch.cuda.current_device()}')
    print(f'Device Name : {torch.cuda.get_device_name()}')
    print(f'Device Capabilty : {torch.cuda.get_device_capability()}')

else:
    print("No GPU")          