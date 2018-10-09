#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: Anatoli Kalysch
# DATE CREATED: 07.10.18
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images_solution.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules

from time import sleep
from timeit import default_timer as timer

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    start_time = timer()

    in_arg = get_input_args()

    # Function that checks command line arguments using in_arg
    if in_arg.verbose:
        check_command_line_arguments(in_arg)

    results = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the results Dictionary using results    
    if in_arg.verbose:
        check_creating_pet_image_labels(results)

    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results    
    if in_arg.verbose:
        check_classifying_images(results)

    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    if in_arg.verbose:
        check_classifying_labels_as_dogs(results)

    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    if in_arg.verbose:
        check_calculating_results(results, results_stats)

    print_results(results, results_stats, in_arg.arch, True, True)

    end_time = timer()

    tot_time = end_time - start_time
    print("\n[*] Total Elapsed Runtime: {:02d}:{:02d}:{}".format(int(tot_time/3600),  # hours
                                                         int(tot_time%3600/60),  # minutes
                                                         round(tot_time%3600%60, 5)))  # seconds
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
