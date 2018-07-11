from microscope.devices import device
from microscope.mirror.alpao import AlpaoDeformableMirror
from microscope.cameras.ximeaCam import XimeaCamera
from microscope.cameras.pvcam import PVCamera

DEVICES = [
  device(AlpaoDeformableMirror, '192.168.1.20', 8007, serial_number='BIL103'),
  device(XimeaCamera, '192.168.1.20', 8008 )
  #device(PVCamera, '192.168.1.20', 8009 )
]
