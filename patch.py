from PIL import Image, ImageDraw, ImageFont 

im_background = Image.open('background.png')
# im_background.show()
def textinbox(text,fnt,color):
	position_x = 195
	position_y = 375
	text_blank = Image.new('RGBA',im_background.size, (255,255,255,0))
	d = ImageDraw.Draw(text_blank)
	index = 0
	for x in text:
		d.text((position_x,position_y), x, font=fnt, fill=color)
		if index == 4:
			index = 0
			position_x = position_x + 67
		else:
			position_x = position_x + 39.5
			index = index + 1
	im_out = Image.composite( text_blank ,im_background,mask = text_blank.split()[3])
	# im_out.show()
	return im_out

fnt = ImageFont.truetype('Courier.ttf',size=50)

f = open('rcode.txt')
line = f.readline()
line=line.strip('\n')
filename = 0
while line:
	line = line.upper()
	im_final = textinbox(line,fnt,(0,0,0,255))
	im_final.save(str(filename) +'.png',dpi=(300.0,300.0))
	print(line+'	done')
	filename = filename + 1
	line = f.readline()
	line=line.strip('\n')
f.close()
print('total:	'+str(filename))