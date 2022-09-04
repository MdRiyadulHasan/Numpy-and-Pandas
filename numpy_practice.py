import numpy as np
grades=np.array([72,35,64,88,51,90,74,12])
curve_center=80
def curve(grades):
    avg=grades.mean()
    print(avg)
    change=curve_center - avg
    new_grades=grades+change
    print(new_grades)
    return np.clip(new_grades,grades,100)
result = curve(grades)
print(result)





























