from PIL import Image #its for manipulating or save different image file format

def asciiconvert(image_path, type, save_path, scale):
    scale = int(scale)

    #open the image and get the size
    img = Image.open(image_path)
    w,h = img.size

    #we resize the image
    img.resize((w//scale, h//scale)).save("resized.%s" % type)

    #open a new imagge
    img = Image.open("resized.%s" % type)
    w, h = img.size #get the new wide and height from the resized

    grid = [] #list correct length and height ( same like resized image )
    for i in range(h):
        grid.append(["X"] * w)

    pix = img.load()

    for y in range(h):
        for x in range(w):
            if sum(pix[x,y]) == 0:
                grid[y][x] = '#'
            elif sum(pix[x, y]) in range (1, 100):
                grid[y][x] = 'X'
            elif sum(pix[x,y]) in range (100, 200):
                grid[y][x] = '%'
            elif sum(pix[x, y]) in range (200, 300):
                grid[y][x] = '&'
            elif sum(pix[x, y]) in range (300, 400):
                 grid[y][x] = '*'
            elif sum(pix[x, y]) in range (400, 500):
                 grid[y][x] = '+'
            elif sum(pix[x, y]) in range (500, 600):
                 grid[y][x] = '/'
            elif sum(pix[x, y]) in range (600, 700):
                 grid[y][x] = '('
            elif sum(pix[x, y]) in range (700, 800):
                 grid[y][x] = '`'
            elif sum(pix[x, y]) in range (800, 900):
                 grid[y][x] = '-'
            elif sum(pix[x, y]) in range (900, 1000):
                 grid[y][x] = '='
            else:
                grid[y][x] = '                '

    art = open(save_path, "w")

    for row in grid:
        art.write("". join(row) + "\n")

    art.close()

if __name__ == '__main__':
    asciiconvert("test.jpg", "jpg", "test.txt", "3")

    
            