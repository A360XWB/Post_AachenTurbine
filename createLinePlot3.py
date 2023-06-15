# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
testfoam = FindSource('test.foam')

# set active source
SetActiveSource(testfoam)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
testfoamDisplay = GetDisplayProperties(testfoam, view=renderView1)

# find source
mach = FindSource('Mach')

# set active source
SetActiveSource(mach)

# get display properties
machDisplay = GetDisplayProperties(mach, view=renderView1)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=mach)
plotOverLine1.Point1 = [-0.30000001192092896, -0.30000001192092896, -0.009999999776482582]
plotOverLine1.Point2 = [0.30000001192092896, 0.30000001192092896, 0.3824999928474426]

# rename source object
RenameSource('p2_L', plotOverLine1)

# find source
p2_L2525 = FindSource('p2_L2-5.25')

# find source
p2_L160 = FindSource('p2_L1-6.0')

# find source
slice1 = FindSource('Slice1')

# find source
p0_L2525 = FindSource('p0_L2-5.25')

# find source
p0_L160 = FindSource('p0_L1-6.0')

# find source
p0_L715 = FindSource('p0_L7-1.5')

# find source
p0_L900 = FindSource('p0_L9+0.0')

# find source
p0_L8075 = FindSource('p0_L8-0.75')

# find source
p0_L345 = FindSource('p0_L3-4.5')

# find source
p0_L4375 = FindSource('p0_L4-3.75')

# find source
p0_L1115 = FindSource('p0_L11+1.5')

# find source
p0_L530 = FindSource('p0_L5-3.0')

# find source
p0_L14375 = FindSource('p0_L14+3.75')

# find source
p0_L6225 = FindSource('p0_L6-2.25')

# find source
p0_L10075 = FindSource('p0_L10+0.75')

# find source
p0_L12225 = FindSource('p0_L12+2.25')

# find source
p0_L1545 = FindSource('p0_L15+4.5')

# find source
p0_L1330 = FindSource('p0_L13+3.0')

# find source
p1_L900 = FindSource('p1_L9+0.0')

# find source
p1_L1760 = FindSource('p1_L17+6.0')

# find source
p1_L2525 = FindSource('p1_L2-5.25')

# find source
p0_L16525 = FindSource('p0_L16+5.25')

# find source
p0_L1760 = FindSource('p0_L17+6.0')

# find source
p1_L160 = FindSource('p1_L1-6.0')

# find source
p1_L16525 = FindSource('p1_L16+5.25')

# find source
p1_L4375 = FindSource('p1_L4-3.75')

# find source
p1_L345 = FindSource('p1_L3-4.5')

# find source
p1_L530 = FindSource('p1_L5-3.0')

# find source
p1_L6225 = FindSource('p1_L6-2.25')

# find source
p1_L715 = FindSource('p1_L7-1.5')

# find source
p1_L12225 = FindSource('p1_L12+2.25')

# find source
p1_L10075 = FindSource('p1_L10+0.75')

# find source
p1_L8075 = FindSource('p1_L8-0.75')

# find source
p1_L1545 = FindSource('p1_L15+4.5')

# find source
p1_L1115 = FindSource('p1_L11+1.5')

# find source
p1_L1330 = FindSource('p1_L13+3.0')

# find source
p1_L14375 = FindSource('p1_L14+3.75')

# find source
p2_L4375 = FindSource('p2_L4-3.75')

# find source
p2_L345 = FindSource('p2_L3-4.5')

# find source
p2_L530 = FindSource('p2_L5-3.0')

# Properties modified on plotOverLine1
plotOverLine1.Resolution = 50
plotOverLine1.Point1 = [0.233335961803972, 0.074694905642992, 0.171]
plotOverLine1.Point2 = [0.285717504249761, 0.091463149766928, 0.171]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'p']
plotOverLine1Display.LookupTable = pLUT
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'p'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'U'
plotOverLine1Display.ScaleFactor = 0.005238156020641327
plotOverLine1Display.SelectScaleArray = 'p'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'p'
plotOverLine1Display.GaussianRadius = 0.00026190780103206633
plotOverLine1Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'p']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1Display.WriteLog = ''

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['Mach_Magnitude', 'p', 'U_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Mach_X', 'Mach_X', 'Mach_Y', 'Mach_Y', 'Mach_Z', 'Mach_Z', 'Mach_Magnitude', 'Mach_Magnitude', 'p', 'p', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Mach_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Mach_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Mach_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Mach_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'p', '1', '0.5000076295109483', '0', 'U_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U_Y', '0', '0', '0', 'U_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'vtkValidPointMask', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude', '0', '0', '0']
plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1.0', 'Mach_X', '1.0', 'Mach_Y', '1.0', 'Mach_Z', '1.0', 'Mach_Magnitude', '1.0', 'p', '1.0', 'U_X', '1.0', 'U_Y', '1.0', 'U_Z', '1.0', 'U_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Mach_Magnitude', '2', 'p', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Mach_Magnitude', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Mach_Magnitude', '4', 'p', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout2 = GetLayoutByName("Layout #2")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout2, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout2.Collapse(2)

# set active view
SetActiveView(renderView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout2.SetSize(1314, 784)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [1.0275513950438382, 1.3941204716299354, 0.7419332971362931]
renderView1.CameraFocalPoint = [0.1861355369736869, -0.07240447721649623, 0.10683767141288161]
renderView1.CameraViewUp = [0.8349001396474371, -0.27174058507306004, -0.47864267595027626]
renderView1.CameraParallelScale = 0.05742495121790837
renderView1.CameraParallelProjection = 1

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).