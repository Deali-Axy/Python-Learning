import PySimpleGUIQt as sg

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Some text on Row 1', font=('Ubuntu Mono', 20))],
          [sg.Text('Enter something on Row 2', font=('Microsoft YaHei', 18)), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
