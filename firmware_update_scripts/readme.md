### Installl

```bash
$ pip install nrfutil
```

### Create DFU zip 

```bash
# Generate DFU package
$ nrfutil pkg generate --hw-version 52 --debug-mode --sd-req 0x0100 --sd-id 0x0100 --application <APPLICATION-FILE.hex> --softdevice <SOFTDEVICE-FILE.hex> <OUTPUT.zip>

# Check sd-req value
$ nrfutil pkg generate --help
```

For SD140 v7.2, --sd-req is 0x0100. See [Reference Link](https://devzone.nordicsemi.com/f/nordic-q-a/67731/sd-req-for-soft-device-s140-v7-2-0)


### To Program
```bash
$ nrfutil dfu usb-serial -pkg <DFU ZIP> -p <VIRTUAL SERIAL PORT> -b 115200
```