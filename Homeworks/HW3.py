#Students&Average HW3

midterm = int(input('midterm grade: '))
project = int(input('project grade: '))
final =  int(input('final grade: '))


average = midterm*(0.3) + project*(0.3) + final *(0.4)

#Grading scale
def determine_score(average):
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average <= 89:
        return 'B'
    elif 70 <= average <= 79:
        return 'C'
    else:
        return 'F'

grade = average
avg = determine_score(average)

print("That's a(n): " + str(grade))
print('Average grade is: ' + str(avg))


studentavg = ['40','50','69','78','56']
studentavg.sort(reverse=True)
print(studentavg)

#ps: I couldn't do the homework correctly I know that, but I did my own best.
