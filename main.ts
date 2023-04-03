//  A butterfly is shown when A is pressed
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Butterfly)
    basic.pause(5000)
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    //  Welcome! is threaded, a smile is shown
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
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showIcon(IconNames.Pitchfork)
    basic.showIcon(IconNames.Target)
})
basic.forever(function on_forever() {
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
