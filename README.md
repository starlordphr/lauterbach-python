# Lauterbach Python Library

## Overview
This is a python library that I built for Lauterbach Trace32. Have fun. :)

## Instructions
#### Configuring Lauterbach helper library
  * In libraries/lauterbach-config:
    - Change **T32_PATH** to point to t32marm-qt binary
    - Change **T32_CONFIG_PATH** to the configuration file inside the Lauterbach directory (config.t32)
  * In libraries/bbb-linux-aware:
    - Change kernel binary path (Line 18: Data.LOAD.Elf)
    - Change TASK.CONFIG path (Line 26)
    - Change MENU.ReProgram path (Line 27)
