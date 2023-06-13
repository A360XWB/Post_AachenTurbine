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
RenameSource('p_L', plotOverLine1)

# find source
p_L1330 = FindSource('p_L13+3.0')

# find source
p_L160 = FindSource('p_L1-6.0')

# find source
p_L10075 = FindSource('p_L10+0.75')

# find source
p_L12225 = FindSource('p_L12+2.25')

# find source
p_L530 = FindSource('p_L5-3.0')

# find source
p_L900 = FindSource('p_L9+0.0')

# find source
p_L1115 = FindSource('p_L11+1.5')

# find source
p_L8075 = FindSource('p_L8-0.75')

# find source
p_L6225 = FindSource('p_L6-2.25')

# find source
p_L4375 = FindSource('p_L4-3.75')

# find source
testfoam = FindSource('test.foam')

# find source
ma_L2525 = FindSource('Ma_L2-5.25')

# find source
ma_L1330 = FindSource('Ma_L13+3.0')

# find source
ma_L8075 = FindSource('Ma_L8-0.75')

# find source
ma_L10075 = FindSource('Ma_L10+0.75')

# find source
ma_L345 = FindSource('Ma_L3-4.5')

# find source
ma_L1760 = FindSource('Ma_L17+6.0')

# find source
ma_L160 = FindSource('Ma_L1-6.0')

# find source
ma_L16525 = FindSource('Ma_L16+5.25')

# find source
ma_L1545 = FindSource('Ma_L15+4.5')

# find source
ma_L4375 = FindSource('Ma_L4-3.75')

# find source
ma_L900 = FindSource('Ma_L9+0.0')

# find source
ma_L530 = FindSource('Ma_L5-3.0')

# find source
ma_L715 = FindSource('Ma_L7-1.5')

# find source
ma_L6225 = FindSource('Ma_L6-2.25')

# find source
ma_L1115 = FindSource('Ma_L11+1.5')

# find source
ma_L12225 = FindSource('Ma_L12+2.25')

# find source
ma_L14375 = FindSource('Ma_L14+3.75')

# find source
p_L1760 = FindSource('p_L17+6.0')

# find source
p_L16525 = FindSource('p_L16+5.25')

# Properties modified on plotOverLine1
plotOverLine1.Resolution = 50
plotOverLine1.Point1 = [0.233663102528687, 0.073665151304183, 0.01475]
plotOverLine1.Point2 = [0.286118084729005, 0.090202226086755, 0.01475]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

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
plotOverLine1Display.ScaleFactor = 0.005245499312877655
plotOverLine1Display.SelectScaleArray = 'p'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'p'
plotOverLine1Display.GaussianRadius = 0.0002622749656438828
plotOverLine1Display.SetScaleArray = ['POINTS', 'p']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'p']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1Display.SelectInputVectors = ['POINTS', 'U']
plotOverLine1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [41553.8046875, 0.0, 0.5, 0.0, 41698.66015625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [41553.8046875, 0.0, 0.5, 0.0, 41698.66015625, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView2, 'XYChartRepresentation')

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
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView2, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Mach_Magnitude', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesPlotCorner = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Mach_Magnitude', '1', 'Mach_X', '1', 'Mach_Y', '1', 'Mach_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Mach_Magnitude', '2', 'Mach_X', '2', 'Mach_Y', '2', 'Mach_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Mach_Magnitude', '0', 'Mach_X', '0', 'Mach_Y', '0', 'Mach_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Mach_Magnitude', '4', 'Mach_X', '4', 'Mach_Y', '4', 'Mach_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# find source
p_L14375 = FindSource('p_L14+3.75')

# find source
p_L345 = FindSource('p_L3-4.5')

# find source
p_L1545 = FindSource('p_L15+4.5')

# find source
p_L2525 = FindSource('p_L2-5.25')

# find source
p_L715 = FindSource('p_L7-1.5')

# update the view to ensure updated data information
lineChartView2.Update()

# resize frame
layout1.SetSplitFraction(0, 0.5280303030303031)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=plotOverLine1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=plotOverLine1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=plotOverLine1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=plotOverLine1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1305, 784)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.0741498581683173, 1.745459805570402, -0.2950882800337215]
renderView1.CameraFocalPoint = [-0.07992969271536865, 0.041358654686156744, 0.3032664531146692]
renderView1.CameraViewUp = [0.9434084830627152, 0.10701587458400624, 0.3138917594845826]
renderView1.CameraParallelScale = 0.5656204184176898
renderView1.CameraParallelProjection = 1

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).