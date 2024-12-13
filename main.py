import webbrowser
import screeninfo

MONITOR_INFO = []

GOON_CHOICE = input('Input your favorite gooning material: jav, ebony, or gfur (type exactly as it appears\n')
if GOON_CHOICE not in ['jav', 'ebony', 'gfur']:
    print('yeah im closing the program hoe')
# print(GOON_CHOICE)

for monitor in screeninfo.get_monitors():
    print(monitor)
    dimensions = monitor.width, monitor.height
    MONITOR_INFO.append(dimensions)

    webbrowser.open_new_tab(f'https://reddit.com/r/{GOON_CHOICE}')

print(MONITOR_INFO)