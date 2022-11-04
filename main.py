#!/usr/bin/env python3

import reservation as rs
import schedule
import time


def runreservation():
    rs.studyroom("s289847", "Dalghak03955754@")


schedule.every().saturday.at("08:30").do(runreservation)
schedule.every().sunday.at("08:30").do(runreservation)
schedule.every().monday.at("08:30").do(runreservation)
schedule.every().tuesday.at("08:30").do(runreservation)
schedule.every().wednesday.at("08:30").do(runreservation)


schedule.every().saturday.at("14:00").do(runreservation)
schedule.every().sunday.at("14:00").do(runreservation)
schedule.every().monday.at("14:00").do(runreservation)
schedule.every().tuesday.at("14:00").do(runreservation)
schedule.every().wednesday.at("14:00").do(runreservation)

while True:
    schedule.run_pending()
    time.sleep(1)
