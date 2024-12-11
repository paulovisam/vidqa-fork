# VIDQA

Quality assurance for audiovisual collections
Documentation: https://vidqa.readthedocs.io.

### Ensures:

File paths less than 250 characters

File names be less than 150 chars

Videos are in mp4 format and h264/aac codecs

### TODO
- Suport h265 codec
- Choose audio track

### Usage
To use vidqa in CLI mode

Unique mode to apply to a folder, generating one log file
```bash
vidqa -i "paste_a_folder_path" -m unique
```

batch mode to apply to a parent folder generating a different log file for each subfolder
```bash
$ vidqa -i "paste_a_folder_path" -m batch
```

Use by defining folder destination of the Metadata Report and Temporary Folder of Converted Videos
```bash
$ vidqa -i "paste_a_folder_path" -m unique -fd "c://my_temp_folder"
```

#### To show or change encode video flags in CLI mode

Show actual flags


```bash
$ vidqa flags
```
CRF - Constante Rate Frame. Stable quality. Default 20 for minimal loss.
```bash
$ vidqa flags --crf 23
```

maxrate - maximum bitrate peak in a second. Default 2 (MiB) to flow in slow connection stream.
```bash
$ vidqa flags --maxrate 3
```

folder_destination - Default folder where converted temporary reports and videos should be stored
```bash
$ vidqa flags -fd "c://my_temp_folder"
```

default_destination - Activates the default folder
```bash
$ vidqa flags -dd 1 # 0 to deactivate
```
