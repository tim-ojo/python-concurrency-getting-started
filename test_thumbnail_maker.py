from thumbnail_maker import ThumbnailMakerService

def test_thumbnail_maker():
    tn_maker = ThumbnailMakerService()
    img_urls = \
    ['https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/10062929553_dcf4406299_k.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/10119289865_a488098f09_z.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/10119493095_5c610b4f96_k.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/10233612245_117aea1c26_z.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/11409439386_58232f1680_k.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/12665166284_c7e6d9c6b3_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/13896217830_90c1a48fb2_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/14128995140_c4882c9a45_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/14537579172_07a90b01e6_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/14567056019_b8793a34e3_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/14575556067_3645683f90_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/14592808598_80a7ca2b07_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/15304823795_5fffb5ed9b_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/15624035681_6864cbed1e_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/19024000380_fb77b7cf66_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/19338595355_aa13caf91e_b.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/19352834342_8f43699229_b.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/20292931565_6ceecddf21_b.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/21786078395_8864e1d6b7_b.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/21890494139_0d4cf26353_b.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/22562959415_87302fbfcd_b.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/9590919201_23d6577955_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/9633815280_c87a2f90bf_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/9650593016_b2533863be_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/9923140974_25c02decda_o.jpg',
     'https://cdn.rawgit.com/tim-ojo/python-concurrency-getting-started/53382895/SampleImages/9923272796_4f35d92941_k.jpg']
    
    tn_maker.make_thumbnails(img_urls)
