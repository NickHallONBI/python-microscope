from microscope.devices import device
from microscope.mirror.alpao import AlpaoDeformableMirror

DEVICES = [
  device(AlpaoDeformableMirror, '129.67.77.21', 8007, serial_number='BIL103'),
]