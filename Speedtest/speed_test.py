from tkinter import *
import speedtest  # pip install speedtest-cli
import threading

root = Tk()
root.title("Internet Speed Test")
root.resizable(False, False)
root.configure(bg="#141527")

# Dimensions for the Window
w = 450
h = 700
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))


def test_speed():
    # Set initial text while loading
    ping.config(text="Testing...")
    upload.config(text="Testing...")
    download.config(text="Testing...")
    Download.config(text="Testing...")
    service.config(text="Testing...")
    ip.config(text="Testing...")

    # Initialize SpeedTest
    test = speedtest.Speedtest()

    # Select the best server
    best = test.get_best_server()

    # Perform the speed test
    download_speed = round(test.download() / (1024 * 1024), 2)  # Download in Mbps
    uploading = round(test.upload() / (1024 * 1024), 2)  # Upload in Mbps
    ping_value = test.results.ping

    # Update the labels with the test results
    ping.config(text=f"{ping_value} ms")
    upload.config(text=f"{uploading} Mbps")
    download.config(text=f"{download_speed} Mbps")
    Download.config(text=f"{download_speed} Mbps")

    # Update server and service details
    service.config(text=f"{best['sponsor']}")
    ip.config(text=f"{best['host']}")


def start_test():
    def run_speed_test():
        test_speed()
        
    threading.Thread(target=run_speed_test, daemon=True).start()


def Check():
    start_test()


def Reset():
    ping.config(text="--")
    upload.config(text="--")
    download.config(text="--")
    Download.config(text="--")
    service.config(text="- - -")
    ip.config(text="- - - - - - - -")


# Icon for window
image_icon = PhotoImage(file="D:/Cyber Study/Speed-Test-main/images/logo.png")
root.iconphoto(False, image_icon)

# Images for UI and buttons
Top = PhotoImage(file="D:/Cyber Study/Speed-Test-main/images/background.png")
Label(root, image=Top, bg="#141527").place(x=0, y=0)

Test_Image = PhotoImage(file="D:/Cyber Study/Speed-Test-main/images/button.png")
Test_Button = Button(
    root,
    image=Test_Image,
    bg="#141527",
    bd=0,
    activebackground="#141527",
    cursor="hand2",
    command=Check,
)
Test_Button.place(x=125, y=510)

Reset_Image = PhotoImage(file="D:/Cyber Study/Speed-Test-main/images/reset.png")
Reset_Button = Button(
    root,
    image=Reset_Image,
    bg="#141527",
    bd=0,
    activebackground="#141527",
    cursor="hand2",
    command=Reset,
)
Reset_Button.place(x=190, y=600)

# Labels to show values
ping = Label(root, text="--", font="arial 20", bg="#141527", fg="#e9b342")
ping.place(x=100, y=215, anchor="center")

download = Label(root, text="--", font="arial 20", bg="#141527", fg="#0cf107")
download.place(x=225, y=215, anchor="center")

upload = Label(root, text="--", font="arial 20", bg="#141527", fg="#e61c25")
upload.place(x=350, y=215, anchor="center")

Download = Label(root, text="--", font="arial 30", bg="#141527", fg="#00FFFF")
Download.place(x=225, y=430, anchor="center")

service = Label(root, text="- - -", font="arial 12", bg="#141527", fg="white")
service.place(x=55, y=590, anchor="center")

ip = Label(root, text="- - - - - - - -",
           font="arial 12", bg="#141527", fg="white")
ip.place(x=380, y=590, anchor="center")


root.mainloop()
