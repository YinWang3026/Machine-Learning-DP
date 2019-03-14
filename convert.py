import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from PIL import Image, ImageDraw

out = Image.new("L",(28,28))
dout = ImageDraw.Draw(out)
with open('sign_mnist_test.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    count = 1
    for row in reader:
        label = row[0]
        row = np.array(row[1:], dtype='float')
        row = row.reshape(28,28)
        plt.imshow(row)
        for y in range(0,28):
            for x in range(0,28):
                dout.point((x,y),fill=int(int(row[y][x]) * 1))
        out = out.resize((224,224))
        fileName = './testImg/'+str(label)+'/'+str(count)+'.jpeg'
        with open(fileName, 'w+') as output:
            out.save(output)
        count = count + 1