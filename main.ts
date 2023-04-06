input.onPinPressed(TouchPin.P0, function () {
    // Welcome! is threaded, a smile is shown when pin 0 is pressed
    basic.showString("Welcome!")
    basic.clearScreen()
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    basic.pause(5000)
    basic.clearScreen()
})
// A butterfly is shown when A is pressed
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Butterfly)
    basic.pause(5000)
})
input.onGesture(Gesture.Shake, function () {
    // A pitchfork and diamond are shown when Shake is pressed
    basic.showIcon(IconNames.Pitchfork)
    basic.showIcon(IconNames.Target)
})
// A countdown is shown before other actions
basic.showNumber(5)
basic.clearScreen()
basic.showNumber(4)
basic.clearScreen()
basic.showNumber(3)
basic.clearScreen()
basic.showNumber(2)
basic.clearScreen()
basic.showNumber(1)
basic.forever(function () {
    // The turtle jumps up and down 4 times
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Tortoise)
        basic.showLeds(`
            . # # # .
            # # # # #
            . # . # .
            . . . . .
            . . . . .
            `)
    }
})
