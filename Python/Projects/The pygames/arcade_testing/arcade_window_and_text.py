import arcade

WIDTH = 800
HEIGHT = 600

def text_on_screen():
    arcade.draw_text("Hello Arcade! - ax = centre       123", WIDTH//2, HEIGHT//2 + 100, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "baseline")
    arcade.draw_text("Hello Arcade! - ax = right        123", WIDTH//2, HEIGHT//2 + 80, arcade.color.GREEN, 20, anchor_x= "right", anchor_y= "baseline")
    arcade.draw_text("Hello Arcade! - ax = left     123", WIDTH//2, HEIGHT//2 + 60, arcade.color.RED, 20, anchor_x= "left", anchor_y= "baseline")

    arcade.draw_text("Hello Arcade! - ay = baseline", WIDTH//2, HEIGHT//2, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "baseline")
    arcade.draw_text("Hello Arcade! - ay = centre", WIDTH//2, HEIGHT//2, arcade.color.YELLOW, 20, anchor_x= "center", anchor_y= "center")
    arcade.draw_text("Hello Arcade! - ay = top", WIDTH//2, HEIGHT//2, arcade.color.GREEN, 20, anchor_x= "center", anchor_y= "top")
    arcade.draw_text("Hello Arcade! - ay = bottom", WIDTH//2, HEIGHT//2, arcade.color.RED, 20, anchor_x= "center", anchor_y= "bottom")

# Create a window
arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.AZURE)


# Static text
arcade.start_render()
#arcade.draw_text("x= (/2 - 000) - Hello Arcade! - centre", WIDTH/2, HEIGHT/2, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "center")
#arcade.draw_text("x= (/2 - 050) - Hello Arcade! - bottom", WIDTH/2, HEIGHT/2 - 50, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "bottom")
#arcade.draw_text("x= (/2 - 100) - Hello Arcade! - top", WIDTH/2, HEIGHT/2 - 100, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "top")
#arcade.draw_text("x= (/2 - 150) - Hello Arcade! - baseline", WIDTH/2, HEIGHT/2 - 150, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "baseline")
arcade.draw_text("Hello Arcade! - ax = centre       123", WIDTH//2, HEIGHT//2 + 100, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "baseline")
arcade.draw_text("Hello Arcade! - ax = right        123", WIDTH//2, HEIGHT//2 + 80, arcade.color.GREEN, 20, anchor_x= "right", anchor_y= "baseline")
arcade.draw_text("Hello Arcade! - ax = left     123", WIDTH//2, HEIGHT//2 + 60, arcade.color.RED, 20, anchor_x= "left", anchor_y= "baseline")

arcade.draw_text("Hello Arcade! - ay = baseline", WIDTH//2, HEIGHT//2, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "baseline")
arcade.draw_text("Hello Arcade! - ay = centre", WIDTH//2, HEIGHT//2, arcade.color.YELLOW, 20, anchor_x= "center", anchor_y= "center")
arcade.draw_text("Hello Arcade! - ay = top", WIDTH//2, HEIGHT//2, arcade.color.GREEN, 20, anchor_x= "center", anchor_y= "top")
arcade.draw_text("Hello Arcade! - ay = bottom", WIDTH//2, HEIGHT//2, arcade.color.RED, 20, anchor_x= "center", anchor_y= "bottom")

arcade.draw_text("moving text!", WIDTH/2, HEIGHT/2 - 100, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "baseline")

arcade.finish_render()
arcade.run()


# can't loop without class?

#text_zpos = 0
#while True:
#    if text_zpos < 361:
#        text_zpos += 1
#        arcade.start_render()
#        text_on_screen()
#        arcade.draw_text("moving text!", WIDTH/2, HEIGHT/2 - 100, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "baseline", rotation= text_zpos)
#        arcade.finish_render()
#    else:
#        text_zpos = 0
#        arcade.start_render()
#        text_on_screen()
#        arcade.draw_text("moving text!", WIDTH/2, HEIGHT/2 - 100, arcade.color.BLACK, 20, anchor_x= "center", anchor_y= "baseline", rotation= text_zpos)
#        arcade.finish_render()
#
#    arcade.run()
#    break