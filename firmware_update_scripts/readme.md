### Installl

```bash
$ pip install nrfutil
```

### Create DFU zip 

```bash
# Generate DFU package
$ nrfutil pkg generate --hw-version 52 --debug-mode --sd-req 0x0100 --sd-id 0x000 --application <APPLICATION-FILE.hex> --softdevice <SOFTDEVICE-FILE.hex> <OUTPUT.zip>

 nrfutil.exe pkg generate --hw-version 52  --sd-req 0x0100 --sd-id 0x000 --application ./universal_dongle_app_code_v_2_0_1.hex --softdevice ./s140_nrf52_7.2.0_softdevice.hex ./output.zip

# Check sd-req value
$ nrfutil pkg generate --help
```

For SD140 v7.2, --sd-req is 0x0100. See [Reference Link](https://devzone.nordicsemi.com/f/nordic-q-a/67731/sd-req-for-soft-device-s140-v7-2-0)


### To Program
```bash
$ nrfutil dfu usb-serial -pkg <DFU ZIP> -p <VIRTUAL SERIAL PORT> -b 115200
```