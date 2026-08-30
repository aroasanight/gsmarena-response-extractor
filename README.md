# !! Important info surrounding GenAI !!
Some repositories on my profile, including this one, consist of predominantly or entirely AI-generated code.

I **_used_** to use AI to generate code when either I couldn't be bothered to do it myself, or wanted it in a much shorter timescale than I'd be able to write it myself.

I believe GenAI not only has negative effects on the individuals who make heavy use of it, but is also detrimental to society as a whole.

For code I still use, or have time to rewrite, I'm slowly working through my old repos deleting all the AI code and replacing it with my own code. It's likely worse quality but it's not AI slop and it's something I've written and can be proud of.

For code I don't still use or don't have time to rewrite, I'm leaving public for archival purposes but with this warning.

For this repo specifically, I will rewrite it as soon as I get the chance, which may be quite some time so please be patient. In the meantime, the old AI-generated code is here since it does still function.

### I do not endorse GenAI in any shape or form.

\- Ari (aroasanight)

---

# gsmarena-response-extractor
 tool for extracting phone frequency response data from GSMArena, and converting it into an AutoEQ-compatible CSV.

![GSMArena Speaker Test logo](https://fdn.gsmarena.com/vv/assets12/static/speakerphone/spk-test.png?v=3)

# instructions for use

1. open GSMArena in your browser, and find your phone. head to the review page, and then the third page of that (the lab tests section).

2. scroll down. if you see a speaker test section, with the GSMArena Speaker Test logo shown at the top of this README, 7 songs, a graph and the ability to add and remove devices, your device is supported.

3. head back to the specs page for your phone. copy the ID from the end of the URL - for example https://www.gsmarena.com/samsung_galaxy_s23_ultra-12024.php yeilds an ID of `12024`. if you can't see where that number comes from you should be seriously contemplating not only why you're on GitHub, but even why you're using any form of technology in the first place. I *would* say you should go back to writing letters, but you're probably not even capable of doing that.

4. run `main.py` and input your ID when prompted.

5. a new file should be generated in the current working directory labelled `brand-model_gsm-raw-response.csv`. this is the output, and is ready to be uploaded to [AutoEQ](https://autoeq.app/) (you may need to reformat in other ways for other platforms/services).
