# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def MacroHotForging(radius, length, emissivity, meltingpoint, sampleTemperature, toolTemperature, sampleDeformation):
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    mdb.models.changeKey(fromName='Model-1', toName='Hot Forging')
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    s = mdb.models['Hot Forging'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(-25.0, 0.0))
    s.RadialDimension(curve=g[2], textPoint=(-43.6465950012207, 0.384616851806641), 
        radius=radius)
    p = mdb.models['Hot Forging'].Part(name='Cylinder', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Hot Forging'].parts['Cylinder']
    p.BaseSolidExtrude(sketch=s, depth=length)
    s.unsetPrimaryObject()
    p = mdb.models['Hot Forging'].parts['Cylinder']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Hot Forging'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=329.413, 
        farPlane=566.307, width=280.24, height=144.466, cameraPosition=(
        82.8109, -421.877, 200.499), cameraUpVector=(-0.0362335, 0.581685, 
        0.812607), cameraTarget=(1.09381, -6.01273, 79.9189))
    s1 = mdb.models['Hot Forging'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s1.FixedConstraint(entity=g[2])
    s1.Line(point1=(0.0, 0.0), point2=(35.0, 0.0))
    s1.HorizontalConstraint(entity=g[3], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(6.60147094726563, 
        -9.99999809265137), value=100.0)
    p = mdb.models['Hot Forging'].Part(name='Tool', dimensionality=THREE_D, 
        type=DISCRETE_RIGID_SURFACE)
    p = mdb.models['Hot Forging'].parts['Tool']
    p.BaseShellRevolve(sketch=s1, angle=360.0, flipRevolveDirection=OFF)
    s1.unsetPrimaryObject()
    p = mdb.models['Hot Forging'].parts['Tool']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Hot Forging'].sketches['__profile__']
    p = mdb.models['Hot Forging'].parts['Tool']
    v1, e, d1, n = p.vertices, p.edges, p.datums, p.nodes
    p.ReferencePoint(point=v1[0])
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Hot Forging'].Material(name='Steel')
    mdb.models['Hot Forging'].materials['Steel'].Density(temperatureDependency=ON, 
        table=((7.84981e-09, 0.0), (7.83042e-09, 100.0), (7.80103e-09, 200.0), 
        (7.76505e-09, 300.0), (7.7259e-09, 400.0), (7.68698e-09, 500.0), (
        7.65171e-09, 600.0), (7.62348e-09, 700.0), (7.60572e-09, 800.0), (
        7.54772e-09, 900.0), (7.49866e-09, 1000.0), (7.45157e-09, 1100.0), (
        7.40634e-09, 1200.0), (7.36287e-09, 1300.0)))
    mdb.models['Hot Forging'].materials['Steel'].Elastic(table=((210000.0, 0.3), ))
    mdb.models['Hot Forging'].materials['Steel'].Plastic(hardening=JOHNSON_COOK, 
        table=((5.0, 1080.0, 0.07, 0.32, meltingpoint, sampleTemperature), ))
    mdb.models['Hot Forging'].materials['Steel'].plastic.RateDependent(
        type=JOHNSON_COOK, table=((0.14, 0.967), ))
    mdb.models['Hot Forging'].materials['Steel'].Conductivity(
        temperatureDependency=ON, table=((50.2715314, 0.0), (48.26192651, 
        100.0), (45.72821119, 200.0), (42.79165378, 300.0), (39.57352261, 
        400.0), (36.195086, 500.0), (32.7776123, 600.0), (29.44236982, 700.0), 
        (26.3106269, 800.0), (25.38529083, 900.0), (26.81242111, 1000.0), (
        28.30627803, 1100.0), (29.97316801, 1200.0), (31.91939744, 1300.0)))
    mdb.models['Hot Forging'].materials['Steel'].SpecificHeat(
        temperatureDependency=ON, table=((472722070.1, 0.0), (502367823.6, 
        100.0), (534417883.3, 200.0), (571334430.4, 300.0), (615579645.8, 
        400.0), (669615710.5, 500.0), (735904805.6, 600.0), (816909112.0, 
        700.0), (587710708.7, 800.0), (602290464.9, 900.0), (621270010.2, 
        1000.0), (643465756.6, 1100.0), (667694116.1, 1200.0), (668800000.0, 
        1300.0)))
    mdb.models['Hot Forging'].materials['Steel'].InelasticHeatFraction()
    mdb.models['Hot Forging'].materials['Steel'].Expansion(table=((1.22e-05, 0.0), 
        (1.37e-05, 20.0), (1.46e-05, 150.0), (1.46e-05, 1315.555556)), 
        temperatureDependency=ON)
    mdb.models['Hot Forging'].HomogeneousSolidSection(name='Section-1', 
        material='Steel', thickness=None)
    a = mdb.models['Hot Forging'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Hot Forging'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Hot Forging'].parts['Cylinder']
    a.Instance(name='Cylinder-1', part=p, dependent=ON)
    p = mdb.models['Hot Forging'].parts['Tool']
    a.Instance(name='Tool-1', part=p, dependent=ON)
    a = mdb.models['Hot Forging'].rootAssembly
    a.rotate(instanceList=('Tool-1', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(
        100.0, 0.0, 0.0), angle=90.0)
    a = mdb.models['Hot Forging'].rootAssembly
    p = mdb.models['Hot Forging'].parts['Tool']
    a.Instance(name='Tool-2', part=p, dependent=ON)
    a = mdb.models['Hot Forging'].rootAssembly
    a.translate(instanceList=('Tool-2', ), vector=(0.0, 0.0, length))
    a = mdb.models['Hot Forging'].rootAssembly
    a.rotate(instanceList=('Tool-2', ), axisPoint=(0.0, 0.0, length), 
        axisDirection=(100.0, 0.0, 0.0), angle=90.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=575.815, 
        farPlane=1014.38, width=502.614, height=259.102, cameraPosition=(
        176.947, -745.014, 290.672), cameraUpVector=(-0.0294869, 0.602147, 
        0.797841), cameraTarget=(12.2005, 26.287, 47.3098))
    p1 = mdb.models['Hot Forging'].parts['Cylinder']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Hot Forging'].parts['Cylinder']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models['Hot Forging'].parts['Cylinder']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Hot Forging'].parts['Cylinder']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Set(cells=cells, name='CylinderAll')
    p = mdb.models['Hot Forging'].parts['Cylinder']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#2 ]', ), )
    p.Surface(side1Faces=side1Faces, name='TopSurfaceCylinder')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=302.882, 
        farPlane=579.732, width=246.583, height=127.116, cameraPosition=(
        118.158, -343.496, -175.736), cameraUpVector=(-0.0990199, -0.296555, 
        0.949868), cameraTarget=(-7.43507, -2.29918, 72.1091))
    p = mdb.models['Hot Forging'].parts['Cylinder']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Surface(side1Faces=side1Faces, name='LowerSurfaceCylinder')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=323.319, 
        farPlane=556.253, width=263.222, height=135.693, cameraPosition=(
        116.787, -410.917, 179.808), cameraUpVector=(-0.0618187, 0.556668, 
        0.828432), cameraTarget=(-7.43907, -2.49611, 73.1475))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=321.228, 
        farPlane=557.032, width=261.519, height=134.815, cameraPosition=(
        157.656, -401.371, 158.337), cameraUpVector=(-0.11577, 0.502736, 
        0.856653), cameraTarget=(-7.46067, -2.50115, 73.1588))
    a = mdb.models['Hot Forging'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Hot Forging'].TempDisplacementDynamicsStep(name='Step-1', 
        previous='Initial', improvedDtMethod=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    a = mdb.models['Hot Forging'].rootAssembly
    region = a.instances['Cylinder-1'].sets['CylinderAll']
    mdb.models['Hot Forging'].Temperature(name='Predefined Field-1', 
        createStepName='Initial', region=region, distributionType=UNIFORM, 
        crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(
        1200.0, ))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, interactions=ON, constraints=ON, 
        engineeringFeatures=ON)
    mdb.models['Hot Forging'].ContactProperty('IntProp-1')
    mdb.models['Hot Forging'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.3, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    a = mdb.models['Hot Forging'].rootAssembly
    s1 = a.instances['Tool-1'].faces
    side2Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region1=a.Surface(side2Faces=side2Faces1, name='m_Surf-1')
    a = mdb.models['Hot Forging'].rootAssembly
    region2=a.instances['Cylinder-1'].surfaces['LowerSurfaceCylinder']
    mdb.models['Hot Forging'].SurfaceToSurfaceContactExp(name ='Int-1', 
        createStepName='Step-1', master = region1, slave = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=599.037, 
        farPlane=1002.14, width=522.885, height=269.551, cameraPosition=(
        211.881, -772.212, 94.8963), cameraUpVector=(-0.0489186, 0.378209, 
        0.924427), cameraTarget=(10.8695, 27.3232, 54.7689))
    a = mdb.models['Hot Forging'].rootAssembly
    s1 = a.instances['Tool-2'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region1=a.Surface(side1Faces=side1Faces1, name='m_Surf-2')
    a = mdb.models['Hot Forging'].rootAssembly
    region2=a.instances['Cylinder-1'].surfaces['TopSurfaceCylinder']
    mdb.models['Hot Forging'].SurfaceToSurfaceContactExp(name ='Int-2', 
        createStepName='Step-1', master = region1, slave = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    a = mdb.models['Hot Forging'].rootAssembly
    r1 = a.instances['Tool-1'].referencePoints
    refPoints1=(r1[2], )
    region = a.Set(referencePoints=refPoints1, name='Set-1')
    mdb.models['Hot Forging'].DisplacementBC(name='BC-1', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    mdb.models['Hot Forging'].TabularAmplitude(name='Amp-1', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))
    a = mdb.models['Hot Forging'].rootAssembly
    r1 = a.instances['Tool-2'].referencePoints
    refPoints1=(r1[2], )
    region = a.Set(referencePoints=refPoints1, name='Set-2')
    mdb.models['Hot Forging'].DisplacementBC(name='BC-2', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=-sampleDeformation, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Hot Forging'].rootAssembly
    r1 = a.instances['Tool-1'].referencePoints
    refPoints1=(r1[2], )
    r2 = a.instances['Tool-2'].referencePoints
    refPoints2=(r2[2], )
    region = a.Set(referencePoints=(refPoints1, refPoints2, ), name='Set-3')
    mdb.models['Hot Forging'].TemperatureBC(name='BC-3', createStepName='Step-1', 
        region=region, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        magnitude=toolTemperature, amplitude=UNSET)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, interactions=ON, constraints=ON, 
        engineeringFeatures=ON)
    a = mdb.models['Hot Forging'].rootAssembly
    s1 = a.instances['Cylinder-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region=a.Surface(side1Faces=side1Faces1, name='Surf-3')
    mdb.models['Hot Forging'].FilmCondition(name='Int-3', createStepName='Step-1', 
        surface=region, definition=EMBEDDED_COEFF, filmCoeff=0.02, 
        filmCoeffAmplitude='', sinkTemperature=sampleTemperature, sinkAmplitude='', 
        sinkDistributionType=UNIFORM, sinkFieldName='')
    a = mdb.models['Hot Forging'].rootAssembly
    s1 = a.instances['Cylinder-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region=a.Surface(side1Faces=side1Faces1, name='Surf-4')
    mdb.models['Hot Forging'].RadiationToAmbient(name='Int-4', 
        createStepName='Step-1', surface=region, radiationType=AMBIENT, 
        distributionType=UNIFORM, field='', emissivity=emissivity, 
        ambientTemperature=sampleTemperature, ambientTemperatureAmp='')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
        constraints=OFF, connectors=OFF, engineeringFeatures=OFF, 
        adaptiveMeshConstraints=ON)
    mdb.models['Hot Forging'].fieldOutputRequests['F-Output-1'].setValues(
        variables=('S', 'SVAVG', 'PE', 'PEVAVG', 'PEEQ', 'PEEQVAVG', 'LE', 'U', 
        'V', 'A', 'RF', 'CSTRESS', 'NT', 'TEMP', 'HFL', 'RFL', 'EVF'))
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p1 = mdb.models['Hot Forging'].parts['Cylinder']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Hot Forging'].parts['Cylinder']
    p.seedPart(size=25.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Hot Forging'].parts['Cylinder']
    p.generateMesh()
    elemType1 = mesh.ElemType(elemCode=C3D8T, elemLibrary=EXPLICIT, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6T, elemLibrary=EXPLICIT)
    elemType3 = mesh.ElemType(elemCode=C3D4T, elemLibrary=EXPLICIT)
    p = mdb.models['Hot Forging'].parts['Cylinder']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p1 = mdb.models['Hot Forging'].parts['Tool']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Hot Forging'].parts['Tool']
    p.seedPart(size=40.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Hot Forging'].parts['Tool']
    p.generateMesh()
    mdb.models['Hot Forging'].setValues(absoluteZero=-273.15, 
        stefanBoltzmann=5.67E-11)
    a = mdb.models['Hot Forging'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    mdb.Job(name='HF', model='Hot Forging', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
        nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
        contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
        resultsFormat=ODB)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Hot Forging'].steps['Step-1'].setValues(massScaling=((
        SEMI_AUTOMATIC, MODEL, THROUGHOUT_STEP, 0.0, 1e-05, BELOW_MIN, 100, 0, 
        0.0, 0.0, 0, None), ), improvedDtMethod=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    mdb.jobs['HF'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='C:/temp/HF.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=476.448, 
        farPlane=876.288, width=442.918, height=228.328, cameraPosition=(
        442.178, -72.1969, 581.738), cameraUpVector=(-0.290143, 0.954595, 
        -0.0675658), cameraTarget=(4.98615, -6.38642, 76.4002))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=471.673, 
        farPlane=892.521, width=438.479, height=226.04, cameraPosition=(
        336.813, -589.144, 143.803), cameraUpVector=(-0.156965, 0.406149, 
        0.900225), cameraTarget=(4.21872, -10.1516, 73.2105))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
   


