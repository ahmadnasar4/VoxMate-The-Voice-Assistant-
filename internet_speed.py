import speedtest

from core_utils import speak


def check_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    print(f"Download speed: {download_speed:.1f} Mbps")
    print(f"Upload speed: {upload_speed:.1f} Mbps")
    speak(f"Download speed: {download_speed:.1f} Mbps")
    speak(f"Upload speed: {upload_speed:.1f} Mbps")

