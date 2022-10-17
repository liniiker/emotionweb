from vpython import *
import math
import serial

def rotationInfo(ringPos, arrowOffset, angleName):

    rotRing = ring(pos = ringPos, axis = ringPos, radius=arrowOffset.mag,thickness=0.04)
    ringArrow = arrow(pos=ringPos+arrowOffset, axis=cross(ringPos,arrowOffset), radius=0.2, thickness=0.06, length=0.3, shaftwidth=0.05)
    ringText = text(pos=ringPos*(1+(0.4/ringPos.mag)), text=angleName, color=color.white, height = 0.2, depth = 0.05, align = 'center', up=vector(0,0,-1))
    return compound([rotRing, ringArrow, ringText])


def setScene():
    # Scene
    scene.range = 5
    # scene.forward=vector(-0.8,-1.2,-0.8) #uncomment to get a more 3d view angle
    scene.background = color.cyan
    scene.width = 1200
    scene.height = 1080

    title = text(pos=vec(0, 3, 0), text='MPU-6050', align='center', color=color.blue, height=0.4, depth=0.2)

    return title

def createRotatingObjects():
    #MPU6050 module
    mpu = box(length=4, width=2, height=.2,opacity=.3,pos=vector(0,0,0),color=color.blue)
    Yaxis = arrow(length=2, shaftwidth=0.1, axis=mpu.axis, color=color.white);
    Xaxis = arrow(length=0.7, shaftwidth=0.1, axis=vector(0,0,1), color=color.white);

    XaxisLabel = text(pos=vector(-0.6,0.1,0.7), text='X-axis', color=color.white, height = 0.2, depth = 0.05, align = 'center', up=vector(0,0,-1))
    YaxisLabel = text(pos=vector(1, 0.1, -0.1), text='Y-axis', color=color.white, height=0.2, depth=0.05,
                      align='center', up=vector(0, 0, -1))
    topSideLabel = text(pos=vector(-1.2, 0.1, -0.2), text='Top Side', color=color.white, height=0.2, depth=0.05,
                      align='center', up=vector(0, 0, -1))

    rotInfoY = rotationInfo(vector(2.4,0,0),vector(0,0,0.2), 'roll')
    rotInfoX = rotationInfo(vector(0,0,1.3), vector(0.2,0,0), 'pitch')
    rotInfoZ = rotationInfo(vector(0,-1,0), vector(-0.2,0,0), 'yaw')

    return compound ([mpu, Xaxis, Yaxis, XaxisLabel, YaxisLabel, topSideLabel, rotInfoY,rotInfoX, rotInfoZ])

def rodriguesRotation(v, k, angle):
    return v*cos(angle)+cross(k,v)*sin(angle)
title = setScene()
angles = label(pos=vector(-2.5,2,1), text='yaw: 0\npitch: 0\nroll: 0', align = 'center', color=color.black, height = 30, deph=0)
rotatingObjetcts = createRotatingObjects()

ArduinoSerial = serial.Serial('COM4',115200)

while (True):
    try:
        while (ArduinoSerial.inWaiting()==0):
            pass
        dataPacket=ArduinoSerial.readline()
        dataPacket=str(dataPacket,'utf-8')
        splitPacket=dataPacket.split("\t")
        yaw=float(splitPacket[0])
        pitch=float(splitPacket[1])
        roll=float(splitPacket[2])

        rate(50)

        angles.text=f'yaw: {round(yaw)}\npitch:{round(pitch)}\nroll: {round(roll)}'

        yaw=math.radians(yaw)
        pitch=math.radians(pitch)
        roll=math.radians(roll)

        x = vector(0,0,1)
        y = vector(1,0,0)

        x = rodriguesRotation(x, vector(0,-1,0),yaw)
        y = rodriguesRotation(y, vector(0, -1, 0), yaw)

        y = rodriguesRotation(y, x, pitch)
        x = rodriguesRotation(x, y, roll)

        rotatingObjetcts.axis = y
        rotatingObjetcts.up=cross(x,y)

    except:
        pass