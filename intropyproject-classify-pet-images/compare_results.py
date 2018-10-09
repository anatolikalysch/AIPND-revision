#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/compare_results.py
#
# PROGRAMMER: Anatoli Kalysch
# DATE CREATED: 09.10.2018
# REVISED DATE:
# PURPOSE: Create a function that compares the three CNN arch models. The output is
# provided as a table on the command line.
#
##
# Imports python modules

from tabulate import tabulate
from re import findall


def table_comparison(results_stats):
    print()
    print('Total stats following: ')
    print(tabulate([['Number of Total Images', results_stats['n_images']],
                    ['Number of Dog Images', results_stats['n_dogs_img']],
                    ['Number of Not a Dog Images', results_stats['n_notdogs_img']]
                    ], tablefmt='orgtbl'))
    print()
    comparison_results = []
    for arch in ['resnet', 'alexnet', 'vgg']:
        try:
            with open('{}_pet-images.txt'.format(arch), 'r') as f:
                contents = f.read()

        except Exception:
            print('{} results could not be read. Check existance of {}_pet-images.txt'.format(arch, arch))

        try:
            not_a_dog_correct = findall(r".*correctly classified not dogs:.*?\((.*?\%)\).*", contents)[0]
            dog_correct = findall(r".*correctly classified dogs:.*?\((.*?\%)\).*", contents)[0]
            breed_correct = findall(r".*correctly classified breeds:.*?\((.*?\%)\).*", contents)[0]
            match = findall(r".*matches \(dogs and not dogs\):.*?\((.*?\%)\).*", contents)[0]
            comparison_results.append([arch, not_a_dog_correct, dog_correct, breed_correct, match])
        except Exception:
            print('{} results could not be read. During the file parsing steps something went wrong.'.format(arch))


    print(tabulate([line for line in comparison_results],
                   headers=['CNN Model Arch', '% Not a Dog correct',
                            '% Dog correct', '% Breed correct', '% Label Matches'],
                   tablefmt='orgtbl'))