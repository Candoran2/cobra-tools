# cobra-tools
"~~Life~~ Modding finds a way."

A simple GUI for extracting OVL and OVS archives and modifying their contents, as well as editors for the associated in-house file formats. Also includes a model plugin for blender.

<img src="https://i.imgur.com/ndYhbQS.png" width="75%" height="75%">

### Installation

**Read the instructions steps carefuly and do not jump ahead and start downloading everything or you will miss important steps**.

Get the latest source code [here](https://github.com/OpenNaja/cobra-tools/archive/master.zip) and unzip to a folder of your choice. 

You need to have installed:
- [Python 3.7 x64 bit](https://www.python.org/downloads/windows/) (**make sure you add it to the system path during installation;** 32 bit versions of python will hit their memory limit trying to read large OVLs, so 64b is recommended.)
- [Microsoft Visual C++ Redistributable 2017 x64](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) (needed for texture conversion - you will likely have this installed already)
- [Microsoft Visual C++ Redistributable 2013 x86](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) (needed for lua decompile - x86 version for now)
#### Install python dependencies
- open a command shell and execute the following line: 
```
pip install pyqt5 imageio
```  
In case this commands tells you upgrade pip, follow the instructions and then try again until all the requirements are met.

### Blender Plugin Installation
- [Blender Plugin - How to Use](https://github.com/OpenNaja/cobra-tools/wiki/Blender-Plugin---How-to-Use)


### How to use
- [OVL Tool - How to Use](https://github.com/OpenNaja/cobra-tools/wiki/OVL-Tool---How-to-Use)
- [List of supported file formats and recommended tools for editing them](https://github.com/OpenNaja/cobra-tools/wiki/Supported-Archive-Content-File-Formats)

### Basic Tutorials
- [Tutorial: Jurassic World Evolution New Species Mod](https://www.youtube.com/watch?v=8qMIBo-7n1A)
- [Tutorial: Planet Zoo New Species Mod](https://www.youtube.com/watch?v=cBauGq4Y1ao)


### Disclaimer
- Remember to backup all mod files and stock files. Any patches will reset or break the mods and will need to be redone and re-released. 
- Not all model files are supported at this time. Some may crash on import or export. Even if they (seemingly) import and export fine, the result is not guaranteed to work ingame.


### Legal Notice and Terms Of Conduct
This software is developed under 'fair use' by enthusiasts and is not affiliated with Universal© or Frontier® in any form.

By downloading and using this software, you agree to the following conditions:
- **Use this software at your own risk.** It may cause damage to you, your equipment or your data. The authors are not responsible for your actions.
- **Do not use this software to circumvent copy protections.** Especially, do not try to unlock downloadable content for free, share official artwork or intellectual property or engage in so-called data mining to announce game content before an official announcement.
- **Do not seek monetary compensation for mods made with this software.** Do not charge money or ask for donations in order to download the mods. Do not accept payment in exchange for exclusive rights (even if temporary) to commissioners of mods.
- **Secure permission to use other parties' work in your mods.** This includes but is not limited to using IP, artwork, skin designs and 3D models (eg. porting models from another game). If you don't have the approval of the copyright holder(s), be prepared to face the consequences.
- **DO NOT AFECT ONLINE** modes of the game drastically, or to gain any advantage above other players using this software. Online gameplay and modifications should be restricted as much as possible and not encouraged.


### Credits
- Planet Zoo, Cobra, Frontier and the Frontier Developments logo are trademarks or registered trademarks of Frontier Developments, plc.
- Jurassic World, Jurassic World Fallen Kingdom, Jurassic World Evolution, Jurassic World Evolution 2 and their respective logos are trademarks of Universal Studios and Amblin Entertainment, Inc.
- Daemon1, DennisNedry1993 and Inaki for initial modding attempts and documentation.
- `texconv` from [DirectXTex](https://github.com/microsoft/DirectXTex) is used internally to convert to and from DDS textures.

### Get in touch
Some Discords where modding progress is discussed can be found here:

- [Frontier Modding Club](https://discord.gg/Su4jXKk)
