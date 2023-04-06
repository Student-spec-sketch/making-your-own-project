def on_pin_pressed_p0():
    # Welcome! is threaded, a smile is shown when pin 0 is pressed
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
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

# A butterfly is shown when A is pressed

def on_button_pressed_a():
    basic.show_icon(IconNames.BUTTERFLY)
    basic.pause(5000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    # A pitchfork and diamond are shown when Shake is pressed
    basic.show_icon(IconNames.PITCHFORK)
    basic.show_icon(IconNames.TARGET)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# A countdown is shown before other actions
basic.show_number(5)
basic.clear_screen()
basic.show_number(4)
basic.clear_screen()
basic.show_number(3)
basic.clear_screen()
basic.show_number(2)
basic.clear_screen()
basic.show_number(1)

def on_forever():
    # The turtle jumps up and down 4 times
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
