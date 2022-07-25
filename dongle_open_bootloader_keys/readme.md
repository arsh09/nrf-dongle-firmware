### Generate package: 

```bash
nrfutil pkg generate --hw-version 52 --sd-req 0x100 --sd-id 0x100  --key-file dongle_bootloader_private.pem --softdevice s140_nrf52_7.2.0_softdevice.hex --bootloader open_bootloader_usb_mbr_pca10059.hex --bootloader-version 1 bootloader_1_0_sd_140_nrf_52_dongle.zip
```


### Upload Package:

```bash
nrfutil dfu usb-serial -pkg bootloader_1_0_sd_140_nrf_52_dongle.zip -p COM8 
```


### Lookup Publich Key:

```bash
nrfutil keys display --key pk --format code dongle_bootloader_private.pem
```