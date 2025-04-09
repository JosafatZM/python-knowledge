def auter():
    bubble_tea_flavor = "Black"
    color = "red"

    def inner():
        nonlocal bubble_tea_flavor # --> with this our output now is "Taro"
        nonlocal color
        bubble_tea_flavor = "Taro"
        color = "green"

    inner()

    return bubble_tea_flavor, color

print(auter())