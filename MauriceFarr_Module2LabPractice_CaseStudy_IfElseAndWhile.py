#header information
"""
author: Maurice Farr
date: 1/23/2024
assignment: Module 2 Lab Practice - Case Study: If...Else and While
purpose: We need to create a Python application that takes student names and GPAs to determine if they qualify for the Dean's List or Honor Roll. The application will prompt for a student's last name 
and stop processing if 'ZZZ' is entered. It will then ask for the student's first name and GPA as a float. If the GPA is 3.5 or higher, it will display a message indicating the student is 
on the Dean's List. If the GPA is 3.25 or higher, it will show a message for the Honor Roll. The app should be tested with at least five students.
"""
#MauriceFarr_Module2LabPractice_CaseStudy_IfElseAndWhile.py

#Source Code of All Files:
import random

#Define the function to get student's information 
def student_info():
    while True:
        #Ask for and accept a student's last name
        student_last_name = input("Please enter the student's last name (or 'ZZZ' to quit processing student records): ")

        #Quit processing student records if the last name entered is 'ZZZ'
        if student_last_name == 'ZZZ':
            print("Exit the student info process. ")
            break #Indication that we will exit the inner loop after quiting to process student records

        #Ask for and accept a student's first name
        student_first_name = input ("Please enter the student's first name: ")

        #Ask for and accept the student's GPA as a float
        student_GPA = float(input("Please enter the student's GPA : "))

        #Determine if the student's GPA is 3.5 or greater
        if student_GPA >= 3.5:
            print(str(student_first_name + " " + student_last_name + " has made the Dean's List. ")) #Confirmation that the student made the Dean's List

        #Determine if the student's GPA is 3.25 or greater
        elif student_GPA >= 3.25:
            print(str(student_first_name + " " + student_last_name + " has made the Honor Roll.")) #Confirmation that the student made the Honor Roll
        else:
            #Determine if the student's GPA is below 3.25
            print(str(student_first_name + " " + student_last_name + " did not make the Dean's List or Honor Roll.")) #Confirmation that the student did not make the Dean's List or Honor Roll

#Call the function to run the application 
student_info()