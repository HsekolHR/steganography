from stegano import lsb

# Declare path of an image
path = "image.png"
# data to be hidden
texts = 'This is a test team....'
#Hiding data
secret = lsb.hide(path, texts)
secret.save("output_img.png")
#Retriveing data
clear_message = lsb.reveal("output_img.png")
print(clear_message)