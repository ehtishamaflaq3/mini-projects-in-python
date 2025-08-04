import qrcode
myqr=qrcode.make("https://github.com/ehtishamaflaq3/mini-projects-in-python")
myqr.save("myqr.jpg", scale=12)