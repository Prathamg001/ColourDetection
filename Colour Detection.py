import cv2
import pandas as pd

ipath = r'C:\Users\Pratham\OneDrive\Desktop\PROJECTS\Colour Detection\colour_dec.jpg'
i = cv2.imread(ipath)

# declaring global variables (are used later on)
click = False
r = g = b = xpos = ypos = 0

# Reading csv file with pandas and giving names to each column
ind = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv(r'C:\Users\Pratham\OneDrive\Desktop\PROJECTS\Colour Detection\colors.csv', names=ind, header=None)


# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, click
        click = True
        xpos = x
        ypos = y
        b, g, r = i[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:

    cv2.imshow("image", i)
    if click:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(i, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(i,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(i, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(i, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        click = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
