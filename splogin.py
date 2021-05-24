#!/usr/bin/env python3

import time
import sys
import getopt
from spiceapi import connection

try:
    import spiceapi
except ModuleNotFoundError:
    raise RuntimeError("spiceapi module not installed")


class AutoApp():
    """The main application frame."""

    def login(self, connection, unit: int, cardId: str):
        spiceapi.card_insert(connection, unit, cardId)
        time.sleep(3)

        for x in range(5):
            print("Press num 00")
            spiceapi.keypads_write(connection, 0, "00")

        time.sleep(5)

        # Warning
        self.repeat(connection, "Button 5", 5)
        time.sleep(1)

        # insert paseli
        self.repeat(connection, "Button 4", 1)
        self.repeat(connection, "Button 5", 2)
        time.sleep(10)

        # mode select
        print('mode select')
        self.repeat(connection, "Button 5", 15)
        time.sleep(1)

        # char select
        print('char select')
        self.repeat(connection, "Button 5", 1)

        # print('Restarting in 10 seconds')
        # time.sleep(10)
        # spiceapi.control_restart(connection)

    def repeat(self, conn, button: str, times: int):
        for x in range(times):
            print("Press " + button)
            spiceapi.buttons_write(conn, [[button, True]])
            time.sleep(.1)
            spiceapi.buttons_write_reset(conn)
            time.sleep(.1)

def debug(variable):
    print (variable, '=', repr(eval(variable)))

if __name__ == "__main__":
    unit = 0
    cardId = ""

    host = "localhost"
    port = 1337
    password = ""

    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:c:p", [
            "unit=",
            "cardId=",
            "password="
        ])
    except getopt.GetoptError:
        print('splogin.py -u <unit> -c <cardId> --password <api-password>')
        sys.exit(2)
  
    for opt, arg in opts:
        if opt in ("-u", "--unit"):
            unit = int(arg)
        elif opt in ("-c", "--cardId"):
            cardId = str(arg)
        elif opt in ("-p", "--password"):
            print(arg)
            password = str(arg)

    try:
        connection = spiceapi.Connection(
            host=host, port=port, password=password)
    except OSError as e:
        print("Connection Error", "Failed to connect: " + str(e))
        print("Using " + str(host) + ":" + str(port) + ":" + str(password))
        sys.exit(2)

    # print success
    print("Success", "Connected.")

    AutoApp().login(connection, unit, cardId)
