import math
import ball_in_box.ballinbox as bb
import ball_in_box.validate as val

def area_sum(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area

if __name__ == '__main__':
    num_of_circle = 5
    blockers = [(0.5, 0.5)
               ,(0.5, -0.3)]
    
    circles = bb.ball_in_box(num_of_circle, blockers)
    
    if num_of_circle == len(circles) and val.validate(circles, blockers):
        area = area_sum(circles)
        i = 0.0
        max = 0.0
        temp=0.0
        while i <= 10:
              random.seed()
              circles = bb.ball_in_box(num_of_circle, blockers)
              temp = area_sum(circles)
              if  temp>max:
                  max=temp
              i+=1
        print("Total area: {}".format(max))
    else:
        print("Error: no good circles.")




