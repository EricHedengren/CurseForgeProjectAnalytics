# CurseForgeModAnalytics
Simple Matplotlib program that plots data from Curseforge analytics

The Analytics.py file, by default, names the new graph after the current date. If you want to change that, you can find it [here](/Mod%20Name/Analytics.py#L40).

You may have to "pip install" some [python packages](Mod%20Name/Analytics.py#L1-L4) before you are able to run the python file.

By default, the ["DebugGraphGenerator.bat"](/Mod%20Name/DebugGraphGenerator.bat) file looks for your folder in your desktop. If you didn't move these downloaded files there, follow these instructions if you would like to debug your [Analytics.py](/Mod%20Name/Analytics.py) file. In order to use the "DebugGraphGenerator.bat" file, after your files have downloaded, edit the text file of that .bat (Change the file from .bat to a .txt, it should look like this "DebugGraphGenerator.txt") and [change your directory](https://github.com/EricHedengren/CurseForgeModAnalytics/blob/master/Mod%20Name/DebugGraphGenerator.bat#L1) to match where you put your files. After you finish, change your extension name back from a .txt to .bat so it can execute.

The files in [Mod Name/Graphs](https://github.com/EricHedengren/CurseForgeModAnalytics/tree/master/Mod%20Name/Graphs "Graphs Folder") and [Mod Name/Data](https://github.com/EricHedengren/CurseForgeModAnalytics/tree/master/Mod%20Name/Graphs "Data Folder") are just example files from my personal curseforge mod. To customize for your own data, go to the [Curseforge Analytics](https://authors.curseforge.com/dashboard/projects) site, and download the stats of the project you would like to analyze. Put the downloaded file in the "Data Folder" on your desktop. If you're adding new analytics, from a new day for example, the Analytics program [automatically finds the "latest" file](https://github.com/EricHedengren/CurseForgeModAnalytics/blob/master/Mod%20Name/Analytics.py#L11), or the most recent one by date. Then double click the "Analytics.py" file, and if you have python installed, it should execute. If it doesn't excute, try the DebugGraphGenerator.bat and it will run the python file through the command prompt (This still requires python).

I hope this helps! Here's the [Example Mod(Standard Materials)](https://www.curseforge.com/minecraft/mc-mods/standardmaterials "Standard Materials CurseForge") that I used for example stats.
