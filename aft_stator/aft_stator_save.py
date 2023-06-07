# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
ma_L160 = FindSource('Ma_L1-6.0')

# get active view
spreadSheetView1 = GetActiveViewOrCreate('SpreadSheetView')

# show data in view
ma_L160Display = Show(ma_L160, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L1.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L2525 = FindSource('Ma_L2-5.25')

# show data in view
ma_L2525Display = Show(ma_L2525, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L2.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L345 = FindSource('Ma_L3-4.5')

# show data in view
ma_L345Display = Show(ma_L345, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
ma_L345Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L3.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L4375 = FindSource('Ma_L4-3.75')

# show data in view
ma_L4375Display = Show(ma_L4375, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L4.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L530 = FindSource('Ma_L5-3.0')

# show data in view
ma_L530Display = Show(ma_L530, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L5.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L6225 = FindSource('Ma_L6-2.25')

# show data in view
ma_L6225Display = Show(ma_L6225, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L6.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L795 = FindSource('Ma_L7-1.5')

# show data in view
ma_L795Display = Show(ma_L795, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L7.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L8075 = FindSource('Ma_L8-0.75')

# show data in view
ma_L8075Display = Show(ma_L8075, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L8.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L900 = FindSource('Ma_L9+0.0')

# show data in view
ma_L900Display = Show(ma_L900, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
ma_L900Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L9.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L10075 = FindSource('Ma_L10+0.75')

# show data in view
ma_L10075Display = Show(ma_L10075, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L10.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L1115 = FindSource('Ma_L11+1.5')

# show data in view
ma_L1115Display = Show(ma_L1115, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L11.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L12225 = FindSource('Ma_L12+2.25')

# show data in view
ma_L12225Display = Show(ma_L12225, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
ma_L12225Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L12.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L1330 = FindSource('Ma_L13+3.0')

# show data in view
ma_L1330Display = Show(ma_L1330, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L13.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L14375 = FindSource('Ma_L14+3.75')

# show data in view
ma_L14375Display = Show(ma_L14375, spreadSheetView1, 'SpreadSheetRepresentation')
	
# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L14.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L1545 = FindSource('Ma_L15+4.5')

# show data in view
ma_L1545Display = Show(ma_L1545, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L15.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L16525 = FindSource('Ma_L16+5.25')

# show data in view
ma_L16525Display = Show(ma_L16525, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
ma_L16525Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L16.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

# find source
ma_L1760 = FindSource('Ma_L17+6.0')

# show data in view
ma_L1760Display = Show(ma_L1760, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
ma_L1760Display.Assembly = ''

# export view
ExportView('/home/cfd5906/paraview_build/bin/Post_AachenTurbine_1p5/aft_stator/aft_stator_795_L17.csv', view=spreadSheetView1, RealNumberNotation='Fixed',
    RealNumberPrecision=8)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout3 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout3.SetSize(400, 400)

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
