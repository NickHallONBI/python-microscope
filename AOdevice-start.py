from microscope.devices import device
from microscope.mirror.alpao import AlpaoDeformableMirror
from microscope.cameras.ximeaCam import XimeaCamera
from microAO.aoDev import AdaptiveOpticsDevice

mirror_args = [AlpaoDeformableMirror, '192.168.1.20', 8007]
camera_args = [XimeaCamera, '192.168.1.20', 8008]

DEVICES = [
  device(*mirror_args, serial_number='BIL103'),
  device(*camera_args),
  device(AdaptiveOpticsDevice, '192.168.1.20', 8009, camera_uri=camera_args,
         mirror_uri=mirror_args)
]
