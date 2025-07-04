from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from core_utils import speak

def get_volume_interface():
    """Retrieve the audio endpoint volume interface."""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

def increase_volume(step=10):
    """Increase the system volume by a specified step percentage."""
    volume = get_volume_interface()
    current_volume = volume.GetMasterVolumeLevelScalar() * 100
    new_volume = min(current_volume + step, 100)
    volume.SetMasterVolumeLevelScalar(new_volume / 100, None)
    speak(f"Volume increased to {int(new_volume)} percent.")
    print(f"Volume increased to {int(new_volume)} percent.")

def decrease_volume(step=10):
    """Decrease the system volume by a specified step percentage."""
    volume = get_volume_interface()
    current_volume = volume.GetMasterVolumeLevelScalar() * 100
    new_volume = max(current_volume - step, 0)
    volume.SetMasterVolumeLevelScalar(new_volume / 100, None)
    speak(f"Volume decreased to {int(new_volume)} percent.")
    print(f"Volume decreased to {int(new_volume)} percent.")