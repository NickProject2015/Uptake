==============================================================
TC_01: Navigate URL ("http://uptake.com")
==============================================================
Keyword     | Function          | Description

navigate	| navigate	        | Open browser and navigate to the current website
click	    | elementClick      | Click on a UI component
wait	    | wait      	    | Wait for specified time
waitFor	    | waitforelement    | Wait for an web element
snapshot	| capturescreen     | Take screenshot
verify	    | verify            | Verify text
moveto	    | moveto            | Move mouse over a web element

==============================================================
Steps for running the Project
    1) Change the driver_path and the Screenshot_file locattion from Constants.py
            Path_TestData = "C:\\Users\\USER\Desktop\\Uptake\\Test_data.xlsx"
            Path_Snapshot = "C:\\Users\\USER\\Desktop\\Uptake\\Screenshots\\"
            Path_IE_driver = "C:\\Users\\USER\\Desktop\\Uptake\\\Web_Dr\\IEDriver_Win32\\IEDriverServer.exe"
            Path_Chrome_driver = "C:\\Users\\USER\\Desktop\\Uptake\\\Web_Dr\\chromedr_win32\\chromedriver.exe"
            Path_Firefox_driver = "C:\\Users\\USER\\Desktop\\Uptake\\\Web_Dr\\geckodriver-win32\\geckodriver.exe"

    2) From terminal, choose the main_tests.py directory (ex: for Windows OS - "cd Tests")
    3) From terminal, type the command "py.test -s -v main_tests.py --browser Firefox" (You can choose one of this
            Browser from the list: Chrome, Mozila(Firefox), InternetExplore(IE); or you can add others by adding into
            Constants.py, browser's drivers)
    4) All required packages you can find on "Uptake_Virt_Env"; or just import all the project files into IDE
    5) Python 3.+ (I used python 3.62)
