## https://learn.arcade.academy/en/latest/chapters/05_drawing/drawing.html#

import arcade

NATIVE = [1920, 1080]
WIN_RES = [600, 600]

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
WIN = arcade.open_window(WIN_RES[0], WIN_RES[1], "My Arcade Drawing")
arcade.Window.set_location(WIN, 1200 - NATIVE[0], NATIVE[1] - 800)
# -


# Set the background color
arcade.set_background_color(arcade.color.SKY_BLUE)
# -


# Get ready to draw
arcade.start_render()
# -


# Drawing a rectangle
# Left of 0, right of 600
# Top of 300, bottom of 0
arcade.draw_lrbt_rectangle_filled(0, WIN_RES[0], 0, WIN_RES[1]/2, arcade.csscolor.DARK_OLIVE_GREEN)
# -


# Tree trunk (rect)
# Center of 80, 320
# Width of 20
# Height of 50
arcade.draw_rect_filled(arcade.XYWH(40, 320, 20, 50), arcade.csscolor.SIENNA)

# Tree Top (cirle)
arcade.draw_circle_filled(40, 350, 28, arcade.csscolor.DARK_GREEN)
# -


# Drawing a rect and an ellipse centered in the rect that is
# alligned with edge of window resolution
# width of 18*5
# height of 13*5
ew = 18; eh = 13; eb = 3; em = 5; # multiplyer
e_xy_b = [ew, eh, eb]

arcade.draw_rect_outline(
    rect= arcade.XYWH(
        x= WIN_RES[0] - e_xy_b[2]-1 - e_xy_b[0]/2 * em, #center x: window res - borderwidth - extra pixels - w shape size * shape multiplyer
        y= WIN_RES[1] - e_xy_b[2]-1 - e_xy_b[1]/2 * em, #center y: window res - borderwidth - extra pixels - h shape size * shape multiplyer
        width= e_xy_b[0] * em,                          #w: w shape size * shape multiplyer
        height= e_xy_b[1] * em,                         #h: h shape size * shape multiplyer
    ),
    color= arcade.csscolor.BLACK,
    border_width= e_xy_b[2]
)
arcade.draw.draw_ellipse_outline(
    center_x= WIN_RES[0] - e_xy_b[2]-1 - e_xy_b[0]/2 * em, #center x: window res - borderwidth - extra pixels - w shape size * shape multiplyer
    center_y= WIN_RES[1] - e_xy_b[2]-1 - e_xy_b[1]/2 * em, #center y: window res - borderwidth - extra pixels - h shape size * shape multiplyer
    width= e_xy_b[0] * em,                                 #w: w shape size * shape multiplyer
    height= e_xy_b[1] * em,                                #h: h shape size * shape multiplyer
    color= arcade.csscolor.RED,
    border_width= e_xy_b[2]
)

# Another tree, with a rect for a trunk and an ellipse for the top
arcade.draw_rect_filled(arcade.XYWH(100, 320, 20, 50), arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(100, 350, 45, 70, arcade.csscolor.DARK_GREEN)
# -


# Drawing a rect and two arcs (one flipped and filled) centered in the rect that is
# alligned and adjusted with edge of window resolution
# width of 18*5
# height of 13*5
aw = 18; ah = 13; ab = 3; am = 5 # multiplyer
a_xy_b = [aw, ah, ab]

arcade.draw_rect_outline(
    rect= arcade.XYWH(
        x= WIN_RES[0] - a_xy_b[2]-1 - a_xy_b[0]/2 * am - 100, #center x: window res - borderwidth - extra pixels - w shape size * shape multiplyer + position adjustment
        y= WIN_RES[1] - a_xy_b[2]-1 - a_xy_b[1]/2 * am,       #center y: window res - borderwidth - extra pixels - h shape size * shape multiplyer
        width= a_xy_b[0] * am,                                #w: w shape size * shape multiplyer
        height= a_xy_b[1] * am,                               #h: h shape size * shape multiplyer
    ),
    color= arcade.csscolor.BLACK,
    border_width= a_xy_b[2],
)
arcade.draw_arc_outline(
    center_x= WIN_RES[0] - a_xy_b[2]-1 - a_xy_b[0]/2 * am - 100,
    center_y= WIN_RES[1] - a_xy_b[2]-1 - a_xy_b[1]/2 * am,
    width= a_xy_b[0] * am,
    height= a_xy_b[1] * am,
    color= arcade.csscolor.DARK_BLUE,
    start_angle= 0,
    end_angle= 180,
    border_width= a_xy_b[2],
)
arcade.draw_arc_filled(
    center_x= WIN_RES[0] - a_xy_b[2]-1 - a_xy_b[0]/2 * am - 100,
    center_y= WIN_RES[1] - a_xy_b[2]-1 - a_xy_b[1]/2 * am,
    width= a_xy_b[0] * am,
    height= a_xy_b[1] * am,
    color= arcade.csscolor.DARK_BLUE,
    start_angle= 180,
    end_angle= 360,
    #border_width= a_xyb[2],
)

# Another tree, with a rect for a trunk and an arc for the top
arcade.draw_rect_filled(
    rect= arcade.XYWH(
        x= 160,
        y= 320,
        width= 20,
        height= 50
        ),
    color= arcade.csscolor.SIENNA
)
arcade.draw_arc_filled(
    center_x= 160,
    center_y= 330,
    width= 40,
    height= 95,
    color= arcade.csscolor.DARK_GREEN,
    start_angle= 0,
    end_angle= 180,
)
# -


# Drawing a rect and a triange centered in the rect that is
# alligned and adjusted with the edge of window resolution
# width of 18*5
# height of 13*5
t_m = 5 # multiplyer
t_w = 18*t_m
t_h = 13*t_m
t_b = 3
t_x = WIN_RES[0] - t_w - t_b - 200
t_y = WIN_RES[1] - t_h - t_b - 1

tx_1 = t_x
ty_1 = t_y
tx_2 = t_x+t_w
ty_2 = t_y
tx_3 = t_x+(t_w/2)
ty_3 = t_y+t_h

tr_x = t_x + t_w/2
tr_y = t_y + t_h/2
tr_w = t_w
tr_h = t_h

arcade.draw_rect_outline(
    rect= arcade.XYWH(
        x= tr_x,        #center x: window res - w shape size borderwidth - extra pixels * shape multiplyer + position adjustment
        y= tr_y,        #center y: window res - h shape size borderwidth - extra pixels * shape multiplyer
        width= tr_w,    #w: w shape size * shape multiplyer
        height= tr_h,   #h: h shape size * shape multiplyer
    ),
    color= arcade.csscolor.BLACK,
    border_width= t_b,
)
arcade.draw_triangle_outline(
    x1= tx_1,
    y1= ty_1,
    x2= tx_2,
    y2= ty_2,
    x3= tx_3,
    y3= ty_3,
    color= arcade.csscolor.WHITE,
    border_width= t_b,
)

# Another tree with a rect for a trunk and a filled triangle for the top
tt_w = 40
tt_h = 60
tt_x = 200
tt_y = 330

ttx_1 = tt_x
tty_1 = tt_y
ttx_2 = tt_x+tt_w
tty_2 = tt_y
ttx_3 = tt_x+(tt_w/2)
tty_3 = tt_y+tt_h

arcade.draw_rect_filled(
    arcade.XYWH(
        x= 220, #center x
        y= 320, #center y
        width= 20,
        height= 50,
    ),
    color= arcade.csscolor.SIENNA,
)
arcade.draw_triangle_filled(
    x1= ttx_1,
    y1= tty_1,
    x2= ttx_2,
    y2= tty_2,
    x3= ttx_3,
    y3= tty_3,
    color= arcade.csscolor.DARK_GREEN
)
# -


# Drawing a rect outline and a polygon centered in the rect with 5 coordinates that is 
# alligned and adjusted with the edge of window resolution, order of sets: BL -> ML -> T -> MR - BR
p_m = 5
p_b = 3
p_w = 18*p_m                                # This has been moved up after compeleting!
p_h = 13*p_m                                # This has been moved up after compeleting!
p_x = WIN_RES[0] - p_w - p_b - 280          # This has been moved up after compeleting!
p_y = WIN_RES[1] - p_h - p_b - 1            # This has been moved up after compeleting!
                                            # This has been moved up after compeleting!
pr_w = p_w                                  # This has been moved up after compeleting!
pr_h = p_h                                  # This has been moved up after compeleting!
pr_x = p_x + (p_w/2 - p_w/4)                # This has been moved up after compeleting!
pr_y = p_y + (p_h/2)                        # This has been moved up after compeleting!
                                            # This has been moved up after compeleting!
arcade.draw_rect_outline(                   # This has been moved up after compeleting!
    arcade.XYWH(                            # This has been moved up after compeleting!
        x= pr_x, #center x                  # This has been moved up after compeleting!
        y= pr_y, #center y                  # This has been moved up after compeleting!
        width= pr_w,                        # This has been moved up after compeleting!
        height= pr_h,                       # This has been moved up after compeleting!
    ),                                      # This has been moved up after compeleting!
    color= arcade.csscolor.BLACK,           # This has been moved up after compeleting!
    border_width= p_b,                      # This has been moved up after compeleting!
)                                           # This has been moved up after compeleting!

p_bl = (p_x, p_y)
p_br = (p_x + (p_w/2), p_y)
p_ml = (p_x - (p_w/4), p_y + (p_h/1.8))
p_mr = (p_x + (3*p_w/4), p_y + (p_h/1.8))
p_t = (p_x + (p_w/4), p_y + p_h)

arcade.draw_polygon_outline(
    (
    p_bl, # BL
    p_ml, # ML
    p_t,  # T
    p_mr, # MR
    p_br, # BR
    ),
    color= arcade.csscolor.GREENYELLOW,
    line_width= p_b,
)

# Another tree that has a rect as the trunk and a polygon for the top
pp_w = 60
pp_h = 60
pp_x = 265
pp_y = 330
pp_bl = (pp_x, pp_y)
pp_br = (pp_x + (pp_w/2), pp_y)
pp_ml = (pp_x - (pp_w/4), pp_y + (pp_h/1.8))
pp_mr = (pp_x + (3*pp_w/4), pp_y + (pp_h/1.8))
pp_t = (pp_x + (pp_w/4), pp_y + pp_h)

arcade.draw_rect_filled(
    arcade.XYWH(
        x= 280, #center x
        y= 320, #center y
        width= 20,
        height= 50,
    ),
    color= arcade.csscolor.SIENNA,
)
arcade.draw_polygon_filled(
    (
    pp_bl, # BL
    pp_ml, # ML
    pp_t,  # T
    pp_mr, # MR
    pp_br, # BR
    ),
    color= arcade.csscolor.DARK_GREEN,
)
# -


# Finish drawing
arcade.finish_render()
# -


# Keep the window up until someone closes it.
arcade.run()
# -