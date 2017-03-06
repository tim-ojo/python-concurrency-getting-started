# thumbnail_maker.py
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve
import PIL
from PIL import Image, ImageOps

logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir

    def download_images(self, img_url_list):
        dest_dir = self.home_dir + os.path.sep + 'incoming'
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)
        
        start = time.perf_counter()
        for url in img_url_list:
            parsed_url = urlparse(url)
            filename = parsed_url.path.split('/')[-1]
            urlretrieve(url, dest_dir + os.path.sep + filename)
        end = time.perf_counter()

        logging.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))

    def perform_resizing(self, posterize=False):
        source_dir = self.home_dir + os.path.sep + 'incoming'
        dest_dir = self.home_dir + os.path.sep + 'outgoing'
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)
        target_sizes = [48, 96, 120, 300]

        start = time.perf_counter()
        for filename in os.listdir(source_dir):
            for basewidth in target_sizes:
                img = Image.open(source_dir + os.path.sep + filename)
                
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
                
                new_filename = os.path.splitext(filename)[0] + \
                    '_' + str(basewidth) + os.path.splitext(filename)[1]
                img.save(dest_dir + os.path.sep + new_filename)

                if posterize:
                    edited_image = ImageOps.autocontrast(img, 15)
                    edited_image = ImageOps.posterize(edited_image, 2)
                    edited_image = edited_image.point(lambda p: p * 1.2)
                    edited_image = ImageOps.expand(edited_image, 20, 'white')
                    edited_filename = os.path.splitext(filename)[0] + \
                    '_' + str(basewidth) + '_p' + os.path.splitext(filename)[1]
                    edited_image.save(dest_dir + os.path.sep + edited_filename)
        end = time.perf_counter()
        logging.info("created thumbnails in {} seconds".format(end - start))

    def make_thumbnails(self, img_url_list):
        self.download_images(img_url_list)
        self.perform_resizing()
    
    def download_images_producer(self, img_url_list, lock):
        # in a loop, do each download (but to the staging dir)
        # try to acquire the lock in a non-blocking way 
        # if yes, then move all images in the staging dir to the incoming dir
        # when done, release the lock 
        pass

    def perform_resizing_consumer(self, lock):
        # in a loop, try to acquire the lock in a blocking fashion
        # when the lock is acquired, process the files in the folder
        # when done, release the lock. time.sleep for 0.1 seconds to 
        # allow producer acquire lock  
        pass

    def make_thumbnails_threadsync(self, img_url_list):
        # create a lock object 
        # create a new thread, the target is download_images_producer, start it.
        # create a 2nd thread, the target is perform_resizing_consumer, start it.
        # wait for both threads to complete
        pass
