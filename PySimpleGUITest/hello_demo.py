import PySimpleGUIQt as sg

sg.Popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')


# event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).Read()


sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [	[sg.Text('Filename')],
          	[sg.Input(), sg.FileBrowse()],
	  		[sg.OK(), sg.Cancel()]]

window = sg.Window('Get filename example', layout)

event, values = window.Read()
window.close()