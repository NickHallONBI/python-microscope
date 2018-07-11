from microscope.devices import device
from microscope.mirror.alpao import AlpaoDeformableMirror
from microscope.cameras.pvcam import PVCamera

DEVICES = [
  device(PVCamera, '192.168.1.20', 8009),
  device(XimeaCamera, '192.168.1.20', 8008)
]
