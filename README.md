# Python-key_logger

Overview
This project demonstrates a simple keylogger built using the Python pynput library. A keylogger is a program that captures and logs keystrokes made by a user on a keyboard. It has practical use in controlled environments, such as ethical hacking labs or monitoring systems, but must not be used maliciously.

Features : 
Logs all keystrokes, including:
Printable keys: Letters, numbers, and symbols.
Special keys: Keys like Enter, Space, and Esc.
Saves logged keystrokes to a file (key_log.txt).
Stops the logging process when the Esc key is pressed.

Code Explanation

Logging Printable Keys:
Uses key.char to capture normal characters (e.g., a, 1, #).
Logging Special Keys:
Captures special keys (e.g., Key.space, Key.enter) using AttributeError handling.
Stopping the Listener:
Pressing the Esc key stops the keylogger.

                                                               
____________________________________________________________________________________________________________________________________________________________________
                                                                    Disclaimer!!
                                                                    
This project is strictly for educational purposes. Unauthorized use of keylogging software to monitor or record keystrokes without consent is illegal and violates privacy laws. Please ensure you have explicit permission before deploying this program. If you'r testing on your device make sure any anti-virus is turned off or short time.
____________________________________________________________________________________________________________________________________________________________________
License
This project is licensed under the MIT License. 
