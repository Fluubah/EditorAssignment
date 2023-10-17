from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from PIL import Image, ImageDraw
import random



class PhotoEditorApp(App):
    pass


class Display(Screen):

    def load_image(self):
        self.ids.image.source = self.ids.img_name.text

    def display_image(self):
        return

    def invert(self, image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 255 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        img.save(self.ids.image.source + "_inverted.png")
        self.ids.image.source = self.ids.image.source+"_inverted.png"

    def sepia(self, image):
        img=Image.open(image)
        pixels=img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red=pixels[x,y][0]
                green=pixels[x,y][1]
                blue=pixels[x,y][2]
                red = int(red*.393 + green*0.769 +blue*0.189)
                green = int(red*.349 + green*0.686 +blue*0.168)
                blue = int(red*.272 + green*0.534 +blue*0.131)
                pixels[x,y]=(red,green,blue)
        img.save(image+"_sepia.png")
        self.ids.image.source = self.ids.image.source+"_sepia.png"

    def black_and_white(self, image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = pixels[x, y][0]
                green = pixels[x, y][1]
                blue = pixels[x, y][2]
                pixels[x, y] = (red, red, red)
        img.save(image + "_bw.png")
        self.ids.image.source = image+"_bw.png"

    def pointillism(self, image):
        img = Image.open(image)
        pixels = img.load()
        canvas = Image.new("RGB", (img.size[0], img.size[1]), "white")
        for i in range(10000):
            x = random.randint(0, img.size[0] - 1)
            y = random.randint(0, img.size[1] - 1)

            size = random.randint(10, 20)
            circle = [(x, y), (x + size, y + size)]
            draw = ImageDraw.Draw(canvas)

            draw.ellipse(circle, fill=(pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]))

            del draw
        canvas.save(f"{image}_pointillism.png")
        self.ids.image.source = image+"_pointillism.png"

PhotoEditorApp().run()
