accY = 0
accX = 0
x = 1
y = 1

def on_forever():
    global accX, accY, x, y
    led.plot(x, y)
    basic.pause(50)
    led.unplot(x, y)
    accX = input.acceleration(Dimension.X)
    accY = input.acceleration(Dimension.Y)
    if accX <= 150 and x > 0:
        x = x - 1
    elif accX > 150 and x < 4:
        x = x + 1
    elif accY <= 150 and y > 0:
        y = y - 1
    elif accY > 150 and y < 4:
        y = y + 1
basic.forever(on_forever)
