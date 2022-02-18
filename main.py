import wrap,time

mariox=200
marioy=200
enemyx=120
enemyy=140

wrap.world.create_world(500,600,200,200)
wrap.world.set_back_color(255, 255, 255)

mario=wrap.sprite.add("mario-1-big",mariox,marioy,"jump")
enemy=wrap.sprite.add("mario-enemies",enemyx,enemyy,"cloud")
def run_vasya(x,y,angle):
    mariomex=wrap.sprite.get_x(mario)
    mariomey=wrap.sprite.get_y(mario)

    #text=wrap.sprite.add_text("run vasya run",mariomex,mariomey-50,"Arial")
    #time.sleep(2)
    #wrap.sprite.remove(text)

    wrap.sprite.set_size(mario,40,40)

    wrap.sprite.set_angle(mario,angle)

    wrap.actions.move_to(mario,x,y)

    wrap.sprite.set_size(mario,50,50)


def monstr():
    enemymex=wrap.sprite.get_x(enemy)
    enemymey=wrap.sprite.get_y(enemy)

   # text=wrap.sprite.add_text("иди сюда!!!",enemymex,enemymey-50,"Arial")
   #  time.sleep(2)
   #  wrap.sprite.remove(text)

    mariohuntx=wrap.sprite.get_x(mario)
    mariohunty=wrap.sprite.get_y(mario)

    wrap.actions.move_to(enemy,mariohuntx-40,mariohunty-40)

def saymonstr(player_id):
    enemymex=wrap.sprite.get_x(enemy)
    enemymey=wrap.sprite.get_y(enemy)
    textenemy = wrap.sprite.add_text("иди сюда!!!", enemymex, enemymey - 50, "Arial",font_size=20,underline=True,text_color=(254, 110, 159))
    time.sleep(2)
    wrap.sprite.set_size_percent(textenemy, 200, 200)
    time.sleep(1)
    wrap.sprite.set_size_percent(textenemy, 100, 100)
    time.sleep(2)
    wrap.sprite.remove(textenemy)


def saymario():


saymario()
run_vasya(340,240,180)
saymonstr()
monstr()
saymario()
run_vasya(150,340,270)
saymonstr()
monstr()
saymario()
run_vasya(440,540,90)
saymonstr()
monstr()








