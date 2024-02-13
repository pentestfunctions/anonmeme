

1. `git clone https://github.com/pentestfunctions/anonmeme.git`
2. `cd anonmeme`
3. `pip install -r requirements.txt`
4. `python anonmeme.py`

To make ext
`pyinstaller --onefile --noconsole --add-data "gif_frames;gif_frames" --add-data "audio_jungle.mp3;." .\anonmeme.py`
