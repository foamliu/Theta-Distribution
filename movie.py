import cv2 as cv

if __name__ == "__main__":
    fourcc = cv.VideoWriter_fourcc(*'MPEG')
    out = cv.VideoWriter('output.avi', fourcc, 24.0, (640, 480))

    filename = 'images/theta_dist_0.png'
    img = cv.imread(filename)
    for _ in range(11):
        out.write(img)
        out.write(img)
        out.write(img)
        out.write(img)

    num_epochs = 40

    for i in range(1, num_epochs - 1):
        filename = 'images/theta_dist_{}.png'.format(i)
        img = cv.imread(filename)
        out.write(img)
        out.write(img)
        out.write(img)
        out.write(img)

    filename = 'images/theta_dist_{}.png'.format(num_epochs - 1)
    img = cv.imread(filename)
    for _ in range(11):
        out.write(img)
        out.write(img)
        out.write(img)
        out.write(img)

    out.release()
