# gsmarena-response-extractor
 Tool for extracting phone frequency response data from GSMArena, and converting it into an AutoEQ-compatible CSV.

![GSMArena Speaker Test logo](https://fdn.gsmarena.com/vv/assets12/static/speakerphone/spk-test.png?v=3)

# Instructions for use

1. Open GSMArena in your browser, and find your phone. Head to the Review page, and then the third page of that (the lab tests section).

2. Scroll down. If you see a speaker test section, with the GSMArena Speaker Test logo at the top of this README, 7 songs, a graph and the ability to add and remove devices, your device is supported.

3. Head back to the specs page for your phone. Copy the ID from the end of the URL - for example https://www.gsmarena.com/samsung_galaxy_s23_ultra-12024.php yeilds an ID of `12024`.

4. Run `main.py` and input your ID when prompted.

5. A new file should be generated in the current working directory labelled `brand-model_gsm-raw-response.csv`. This is the output, and is ready to be uploaded to AutoEQ (you may need to reformat in other ways for other platforms/services).