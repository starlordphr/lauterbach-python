from libraries.lauterbach import *

conn = Lauterbach()
T32 = conn.T32_Start()
conn.Connect()

conn.BatchCommands('libraries/bbb-linux-aware')
conn.Disconnect()