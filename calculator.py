import tkinter as tk
from PIL import ImageGrab
from src import model

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 200
LINE_WIDTH = 20

class HandwritingCalculator(object):
	def __init__(self):
		self.translator = model.HandwritingTranslator()
		self.root = tk.Tk()
		self.root.title('Handwritten Calculator')
		self.c = tk.Canvas(self.root, bg='white', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
		self.c.pack()
		self.c.grid()
		self.setup()
		self.root.mainloop()

	def setup(self):
		self.x_pos = None
		self.y_pos = None
		self.c.bind('<B1-Motion>', self.paint)
		self.c.bind('<ButtonRelease-1>', self.finish_draw)
		self.c.bind('<ButtonRelease-3>', self.reset)
		self.reset(None)

	def paint(self, event):
		if self.x_pos and self.y_pos:
			self.c.create_line(self.x_pos, self.y_pos, event.x, event.y, width=LINE_WIDTH, smooth=tk.TRUE, capstyle=tk.ROUND)
		self.x_pos = event.x
		self.y_pos = event.y

	def reset(self, event):
		self.c.delete('all')

	def finish_draw(self, event):
		self.x_pos, self.y_pos = None, None
		x1 = self.c.winfo_rootx() + self.c.winfo_x()
		y1 = self.c.winfo_rooty() + self.c.winfo_y()
		x2 = x1 + CANVAS_WIDTH
		y2 = y1 + CANVAS_HEIGHT
		image = ImageGrab.grab((x1,y1,x2,y2)).convert('L')
		# image.save('tes.jpg')
		self.translator.translate(image)


if __name__ == '__main__':
	HandwritingCalculator()