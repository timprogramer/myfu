"""
Сделать набор команд, с помощью которых можно запрограммировать сценарий, состоящий из следующих действий:
Появление танка номер 1 или 2 с анимацией.
Перемещение танков вверх, вниз, вправо, влево.
Танк не должен перемещаться по диагонали, только под углами в 90гр. Как в оригинальной игре.
"""
import wrap,time

wrap.world.create_world(400,500,200,200)

t1=wrap.sprite.add("battle_city_tanks",100,100,"tank_player_size1_purple2",False)
t2=wrap.sprite.add("battle_city_tanks",350,200,"tank_enemy_size4_yellow2",False)
def create_tanksandspawn(x,y,tank_id):
    star=wrap.sprite.add("battle_city_items",x,y,"effect_appearance1")

    wrap.sprite.set_size_percent(star,150,150)
    time.sleep(0.6)
    wrap.sprite.set_size_percent(star,100,100)
    time.sleep(0.6)
    wrap.sprite.set_size_percent(star,150,150)
    time.sleep(0.6)
    wrap.sprite.set_size_percent(star,100,100)
    time.sleep(0.6)
    wrap.sprite.set_size_percent(star,150,150)
    time.sleep(0.6)
    wrap.sprite.set_size_percent(star,100,100)
    time.sleep(0.6)
    wrap.sprite.set_size_percent(star,150,150)
    time.sleep(0.6)
    wrap.sprite.set_size_percent(star,100,100)

    wrap.sprite.remove(star)

    wrap.sprite.show(tank_id)


def tank_up(tank_id,pixel):
    wrap.sprite.set_angle(tank_id,360)
    wrap.sprite.move_at_angle_dir(tank_id,pixel)

def tank_down(tank_id,pixel):
    wrap.sprite.set_angle(tank_id,180)
    wrap.sprite.move_at_angle_dir(tank_id,pixel)

def tank_right(tank_id,pixel):
    wrap.sprite.set_angle(tank_id,90)
    wrap.sprite.move_at_angle_dir(tank_id,pixel)

def tank_left(tank_id,pixel):
    wrap.sprite.set_angle(tank_id,-90)
    wrap.sprite.move_at_angle_dir(tank_id,pixel)



create_tanksandspawn(100,100,t1)
create_tanksandspawn(350,200,t2)
time.sleep(0.7)
tank_up(t2,49)
time.sleep(0.7)
tank_down(t1,200)
time.sleep(0.7)
tank_right(t2,10)
time.sleep(0.7)
tank_left(t1,30)
time.sleep(0.7)
tank_down(t2,50)
time.sleep(0.7)
tank_up(t1,86)
time.sleep(0.7)
tank_left(t2,1)
time.sleep(0.7)
tank_right(t1,0)

































