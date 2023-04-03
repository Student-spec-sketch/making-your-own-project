# A butterfly is shown when A is pressed

def on_button_pressed_a():
    basic.show_icon(IconNames.BUTTERFLY)
    basic.pause(5000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    # Welcome! is threaded, a smile is shown
    basic.show_string("Welcome!")
    basic.clear_screen()
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    basic.pause(5000)
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_gesture_shake():
    basic.show_icon(IconNames.PITCHFORK)
    basic.show_icon(IconNames.TARGET)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    for index in range(4):
        basic.show_icon(IconNames.TORTOISE)
        basic.show_leds("""
            . # # # .
                        # # # # #
                        . # . # .
                        . . . . .
                        . . . . .
        """)
basic.forever(on_forever)
