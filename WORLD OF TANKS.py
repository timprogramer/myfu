"""
Сделать набор команд, с помощью которых можно запрограммировать сценарий, состоящий из следующих действий:
Появление танка номер 1 или 2 с анимацией.
Перемещение танков вверх, вниз, вправо, влево.
Танк не должен перемещаться по диагонали, только под углами в 90гр. Как в оригинальной игре.
"""
import wrap,time

wrap.world.create_world(400,500,200,200)

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

    tanks=wrap.sprite.add("battle_city_tanks",x,y,tank_id)










create_tanksandspawn(100,100,"tank_player_size1_purple2")
create_tanksandspawn(350,200,"tank_enemy_size4_yellow2")








































