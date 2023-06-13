# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
p0_L160 = FindSource('p0_L1-6.0')

# set active source
SetActiveSource(p0_L160)

# get active view
lineChartView1 = GetActiveViewOrCreate('XYChartView')

# get display properties
p0_L160Display = GetDisplayProperties(p0_L160, view=lineChartView1)

# create new layout object 'Layout #3'
layout3 = CreateLayout(name='Layout #3')

# set active view
SetActiveView(None)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
p0_L160Display_1 = Show(p0_L160, spreadSheetView1, 'SpreadSheetRepresentation')

# assign view to a particular cell in the layout
AssignViewToLayout(view=spreadSheetView1, layout=layout3, hint=0)

# Properties modified on p0_L160Display_1
p0_L160Display_1.Assembly = ''

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach', 'Points']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach', 'Points', 'Points_Magnitude']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach', 'Points', 'Points_Magnitude', 'U']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach', 'Points', 'Points_Magnitude', 'U', 'U_Magnitude']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Point ID', 'Mach', 'Points', 'Points_Magnitude', 'U', 'U_Magnitude', 'vtkValidPointMask']

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L1.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L2525 = FindSource('p0_L2-5.25')

# set active source
SetActiveSource(p0_L2525)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L2525)

# show data in view
p0_L2525Display = Show(p0_L2525, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L2525Display
p0_L2525Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L2.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L345 = FindSource('p0_L3-4.5')

# set active source
SetActiveSource(p0_L345)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L2525)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L345)

# show data in view
p0_L345Display = Show(p0_L345, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L345Display
p0_L345Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L3.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L4375 = FindSource('p0_L4-3.75')

# set active source
SetActiveSource(p0_L4375)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L345)

# show data in view
p0_L4375Display = Show(p0_L4375, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L4375Display
p0_L4375Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L4.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L530 = FindSource('p0_L5-3.0')

# set active source
SetActiveSource(p0_L530)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L530)

# set active source
SetActiveSource(p0_L530)

# show data in view
p0_L530Display = Show(p0_L530, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L530Display
p0_L530Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L5.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L6225 = FindSource('p0_L6-2.25')

# set active source
SetActiveSource(p0_L6225)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L530)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L6225)

# set active source
SetActiveSource(p0_L6225)

# show data in view
p0_L6225Display = Show(p0_L6225, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L6225Display
p0_L6225Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L6.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L795 = FindSource('p0_L7-1.5')

# set active source
SetActiveSource(p0_L795)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L6225)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L795)

# show data in view
p0_L795Display = Show(p0_L795, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L795Display
p0_L795Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L7.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L8075 = FindSource('p0_L8-0.75')

# set active source
SetActiveSource(p0_L8075)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L795)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L8075)

# show data in view
p0_L8075Display = Show(p0_L8075, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L8075Display
p0_L8075Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L8.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L900 = FindSource('p0_L9+0.0')

# set active source
SetActiveSource(p0_L900)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L8075)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L900)

# show data in view
p0_L900Display = Show(p0_L900, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L900Display
p0_L900Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L9.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L10075 = FindSource('p0_L10+0.75')

# set active source
SetActiveSource(p0_L10075)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L900)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L10075)

# show data in view
p0_L10075Display = Show(p0_L10075, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L10075Display
p0_L10075Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L10.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L1115 = FindSource('p0_L11+1.5')

# set active source
SetActiveSource(p0_L1115)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L10075)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L1115)

# show data in view
p0_L1115Display = Show(p0_L1115, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L1115Display
p0_L1115Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L11.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L12225 = FindSource('p0_L12+2.25')

# set active source
SetActiveSource(p0_L12225)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L1115)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L12225)

# show data in view
p0_L12225Display = Show(p0_L12225, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L12225Display
p0_L12225Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L12.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L1330 = FindSource('p0_L13+3.0')

# set active source
SetActiveSource(p0_L1330)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L12225)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L1330)

# show data in view
p0_L1330Display = Show(p0_L1330, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L1330Display
p0_L1330Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L13.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L14375 = FindSource('p0_L14+3.75')

# set active source
SetActiveSource(p0_L14375)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L1330)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L14375)

# show data in view
p0_L14375Display = Show(p0_L14375, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L14375Display
p0_L14375Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L14.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L1545 = FindSource('p0_L15+4.5')

# set active source
SetActiveSource(p0_L1545)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L14375)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L1545)

# show data in view
p0_L1545Display = Show(p0_L1545, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L1545Display
p0_L1545Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L15.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L16525 = FindSource('p0_L16+5.25')

# set active source
SetActiveSource(p0_L16525)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L1545)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L16525)

# show data in view
p0_L16525Display = Show(p0_L16525, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L16525Display
p0_L16525Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L16.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
p0_L1760 = FindSource('p0_L17+6.0')

# set active source
SetActiveSource(p0_L1760)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=p0_L16525)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=p0_L1760)

# show data in view
p0_L1760Display = Show(p0_L1760, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on p0_L1760Display
p0_L1760Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/inlet/inlet_795_L17.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout2 = GetLayoutByName("Layout #2")

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout2.SetSize(1314, 784)

# layout/tab size in pixels
layout3.SetSize(400, 400)

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
