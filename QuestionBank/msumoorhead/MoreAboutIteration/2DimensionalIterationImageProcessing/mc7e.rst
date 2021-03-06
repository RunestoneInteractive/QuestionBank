.. mchoice:: mc7e
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: MoreAboutIteration
   :subchapter: 2DimensionalIterationImageProcessing
   :topics: MoreAboutIteration/2DimensionalIterationImageProcessing
   :from_source: None
   :answer_a: It would look like a red-filtered version of the original image
   :answer_b: It would be a solid red rectangle the same size as the original image
   :answer_c: It would look the same as the original image
   :answer_d: It would look the same as the negative image in the example code
   :correct: a
   :feedback_a: Because we are removing the green and the blue values, but keeping the variation of the red the same, you will get the same image, but it will look like it has been bathed in red.
   :feedback_b: Because the red value varies from pixel to pixel, this will not look like a solid red rectangle.  For it to look like a solid red rectangle each pixel would have to have exactly the same red value.
   :feedback_c: If you remove the blue and green values from the pixels, the image will look different, even though there does not appear to be any blue or green in the original image (remember that other colors are made of combinations of red, green and blue).
   :feedback_d: Because we have changed the value of the pixels from what they were in the original ActiveCode box code, the image will not be the same.

   What would the image produced from the above activecode (itf) look like if you replaced the lines:

   .. code-block:: python

      newred = 255 - p.getRed()
      newgreen = 255 - p.getGreen()
      newblue = 255 - p.getBlue()

   with the lines:

   .. code-block:: python

      newred = p.getRed()
      newgreen = 0
      newblue = 0