# -*- coding: utf


  # משימה שנייה- מציאת מטריצה מינימלית
import numpy as np

def find_the_minimu,_2d_arry():
    
    a1 = np.arange(8).reshape(2,4) #הגדרת מערך ראשון
    a2 = np.arange(15).reshape(5,3) #הגדרת מערך שני
    shape_ofa1 = a1.shape #ייצוג גודל המערך הראשון
    shape_ofa2 = a2.shape #ייצוג גודל המערך השני
    size = lambda x1, x2 : x1 if (x1 < x2) else x2 #הגדרת משתנה "גודל" המייצג את הגודל המינמלי של חיבור המטריצות 
    smallest_y = size(shape_ofa1[1], shape_ofa2[1]) #גודל הטור
    smallest_x = size(shape_ofa1[0], shape_ofa2[0]) #גודל השורה
    min_arry = np.zeros((smallest_x ,  smallest_y), dtype=int) # הגדרת מערך בגודל מינימלי המורכב מ2 המערכים שהוגדרו
    min_arry_size = min_arry.shape #מייצג את הגודל המינימלי הסופי
    for row in range(min_arry_size[0]): #חוזר כמספר השורות
        for tor in range(min_arry_size[1]): #חוזר כמספר הטורים                                     
           min_arry[row][tor] = a1[row][tor] + a2[row][tor] #הוספת ערך למערך החדש המורכב מחיבור 2 איברים של מערך 1 ו2
    print(min_arry)

if __name__ == "__main__":

d