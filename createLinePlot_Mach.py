# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
mach = FindSource('Mach')

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1.Point1 = [-56.299434661865234, -57.1494140625, -47.506736755371094]
plotOverLine1.Point2 = [178.26358032226562, 191.84307861328125, 186.38719177246094]

# rename source object
RenameSource('L', plotOverLine1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# assign view to a particular cell in the layout
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=2)

# find source
testfoam = FindSource('test.foam')

# find source
l160 = FindSource('L1-6.0')

# find source
l345 = FindSource('L3-4.5')

# find source
l2525 = FindSource('L2-5.25')

# find source
l4375 = FindSource('L4-3.75')

# find source
l530 = FindSource('L5-3.0')

# find source
l1115 = FindSource('L11+1.5')

# find source
l8075 = FindSource('L8-0.75')

# find source
l6225 = FindSource('L6-2.25')

# find source
l1545 = FindSource('L15+4.5')

# find source
l715 = FindSource('L7-1.5')

# find source
l12225 = FindSource('L12+2.25')

# find source
l900 = FindSource('L9-0.0')

# find source
l10075 = FindSource('L10+0.75')

# find source
l1760 = FindSource('L17+6.0')

# find source
l1330 = FindSource('L13+3.0')

# find source
l14375 = FindSource('L14+3.75')

# find source
l16525 = FindSource('L16+5.25')

# Properties modified on plotOverLine1
plotOverLine1.Resolution = 20
plotOverLine1.Point1 = [0.0, 0.0, 0.092]
plotOverLine1.Point2 = [1.0, 1.0, 0.092]

# show data in view
plotOverLine1Display = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.UseIndexForXAxis = 0
plotOverLine1Display.XArrayName = 'arc_length'
plotOverLine1Display.SeriesVisibility = ['epsilon', 'k', 'Mach', 'nut', 'p', 'U_Magnitude']
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'epsilon', 'epsilon', 'k', 'k', 'Mach', 'Mach', 'nut', 'nut', 'p', 'p', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'epsilon', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'k', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nut', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'U_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_Y', '0', '0', '0', 'U_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'vtkValidPointMask', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude', '0', '0', '0']
plotOverLine1Display.SeriesOpacity = ['arc_length', '1.0', 'epsilon', '1.0', 'k', '1.0', 'Mach', '1.0', 'nut', '1.0', 'p', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1Display.SeriesPlotCorner = ['arc_length', '0', 'epsilon', '0', 'k', '0', 'Mach', '0', 'nut', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display.SeriesLabelPrefix = ''
plotOverLine1Display.SeriesLineStyle = ['arc_length', '1', 'epsilon', '1', 'k', '1', 'Mach', '1', 'nut', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display.SeriesLineThickness = ['arc_length', '2', 'epsilon', '2', 'k', '2', 'Mach', '2', 'nut', '2', 'p', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display.SeriesMarkerStyle = ['arc_length', '0', 'epsilon', '0', 'k', '0', 'Mach', '0', 'nut', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display.SeriesMarkerSize = ['arc_length', '4', 'epsilon', '4', 'k', '4', 'Mach', '4', 'nut', '4', 'p', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesOpacity = ['arc_length', '1', 'epsilon', '1', 'k', '1', 'Mach', '1', 'nut', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display.SeriesPlotCorner = ['Mach', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesLineStyle = ['Mach', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'epsilon', '1', 'k', '1', 'nut', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1Display.SeriesLineThickness = ['Mach', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'epsilon', '2', 'k', '2', 'nut', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1Display.SeriesMarkerStyle = ['Mach', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'epsilon', '0', 'k', '0', 'nut', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesMarkerSize = ['Mach', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'epsilon', '4', 'k', '4', 'nut', '4', 'p', '4', 'vtkValidPointMask', '4']

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = ['epsilon', 'k', 'Mach', 'p', 'U_Magnitude']

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = ['epsilon', 'Mach', 'p', 'U_Magnitude']

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = ['Mach', 'p', 'U_Magnitude']

# Properties modified on plotOverLine1Display
plotOverLine1Display.AttributeType = 'Cell Data'

# Properties modified on plotOverLine1Display
plotOverLine1Display.UseIndexForXAxis = 1

# Properties modified on plotOverLine1Display
plotOverLine1Display.UseIndexForXAxis = 0

# set active source
SetActiveSource(mach)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=plotOverLine1)

# set active source
SetActiveSource(plotOverLine1)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(plotOverLine1)

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# trace defaults for the display properties.
plotOverLine1Display_1.Representation = 'Surface'
plotOverLine1Display_1.ColorArrayName = ['POINTS', 'p']
plotOverLine1Display_1.LookupTable = pLUT
plotOverLine1Display_1.SelectTCoordArray = 'None'
plotOverLine1Display_1.SelectNormalArray = 'None'
plotOverLine1Display_1.SelectTangentArray = 'None'
plotOverLine1Display_1.OSPRayScaleArray = 'p'
plotOverLine1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display_1.SelectOrientationVectors = 'U'
plotOverLine1Display_1.ScaleFactor = 0.1
plotOverLine1Display_1.SelectScaleArray = 'p'
plotOverLine1Display_1.GlyphType = 'Arrow'
plotOverLine1Display_1.GlyphTableIndexArray = 'p'
plotOverLine1Display_1.GaussianRadius = 0.005
plotOverLine1Display_1.SetScaleArray = ['POINTS', 'p']
plotOverLine1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display_1.OpacityArray = ['POINTS', 'p']
plotOverLine1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display_1.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display_1.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1Display_1.SelectInputVectors = ['POINTS', 'U']
plotOverLine1Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display_1.ScaleTransferFunction.Points = [25308.26171875, 0.0, 0.5, 0.0, 25312.26171875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display_1.OpacityTransferFunction.Points = [25308.26171875, 0.0, 0.5, 0.0, 25312.26171875, 1.0, 0.5, 0.0]

# show color bar/color legend
plotOverLine1Display_1.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

# set active view
SetActiveView(lineChartView1)

# set active source
SetActiveSource(testfoam)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1270, 784)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.25462926494597643, 0.0821339304369496, 0.21102796477352648]
renderView1.CameraFocalPoint = [0.25462926494597643, 0.0821339304369496, 0.08799999952316284]
renderView1.CameraParallelScale = 0.31648326602087123
renderView1.CameraParallelProjection = 1

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).