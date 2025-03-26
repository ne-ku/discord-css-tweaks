# neku's discord css tweaks
some css filters for the ublock origin browser extension that make discord look more like before the recent update (2025/03/25)

![preview of bigger server icons](media/screen.png)

## what they do
1. server icons are larger (can be adjusted in settings section)
2. the buttons for emojis, stickers, gifs, etc. are larger (can be adjusted in settings section)
3. dm buttons are centered
4. server icons are circular when you don't hover over them
5. the bar at the top is removed and the inbox button moved down

![preview of bigger chat button icons](media/chat-buttons.png)

## how to apply them
if you have uBlock installed, go to settings by clicking on the extension's icon and then opening the dashboard (the gears icon in the bottom right of the menu).

![where to find the settings](media/ublock-settings.png)

in the settings, click on "My filters" at the top. copy the filters from [ublock-filters.txt](ublock-filters.txt) into the text box and then click on "Apply changes". once you refresh or open a new tab with discord running, the changes should be visible.

### remove individual filters
apart from the settings, any of the other sections that start with `--SECTION NAME--` can be removed without side effects if there are tweaks you don't want to use.
