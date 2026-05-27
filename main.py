#코드
ball = sphere(pos=vector(0, 0, 0), texture = "https://www.shutterstock.com/image-illustration/hydrogen-atom-model-showing-electron-600nw-2596229819.jpg")
ball = sphere(pos=vector(0, 0, -2.5), texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Electron_shell_002_Helium_-_no_label.svg/250px-Electron_shell_002_Helium_-_no_label.svg.png")
ball = sphere(pos=vector(0, 0, -5), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGPKIrzPenlG1RWuwI0Ql_4pk3kAxSRQoQHg&s")
ball = sphere(pos=vector(0, 0, -7.5), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyMihQTNJZjsp2hxUk4kIvP7it4VwstlpmXQ&s")
ball = sphere(pos=vector(0, 0, -10), texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Electron_shell_008_Oxygen_-_no_label.svg/250px-Electron_shell_008_Oxygen_-_no_label.svg.png")
a = arrow(pos = vector(0, 3, 0), color = color.green)
a.axis = vector(0, 0, 0) - a.pos

while True:
    rate(60)
    
    ev = scene.waitfor('keydown')
    
    if ev.key == ' ':
        current_index = current_index + 1
        
        if current_index >= 5:
            current_index = 0
            
        target_pos = balls[current_index].pos
        a.pos = target_pos + vector(0, 3, 0)





 새로운 코드
Web VPython 3.2

balls = []

balls.append(sphere(pos=vector(-5, 0, 0), texture= "https://www.shutterstock.com/image-illustration/hydrogen-atom-model-showing-electron-600nw-2596229819.jpg"))
balls.append(sphere(pos=vector(-2.5, 0, 0), texture= "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Electron_shell_002_Helium_-_no_label.svg/250px-Electron_shell_002_Helium_-_no_label.svg.png"))
balls.append(sphere(pos=vector(0, 0, 0), texture= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGPKIrzPenlG1RWuwI0Ql_4pk3kAxSRQoQHg&s"))
balls.append(sphere(pos=vector(2.5, 0, 0), texture= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyMihQTNJZjsp2hxUk4kIvP7it4VwstlpmXQ&s"))
balls.append(sphere(pos=vector(5, 0, 0), texture= "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Electron_shell_008_Oxygen_-_no_label.svg/250px-Electron_shell_008_Oxygen_-_no_label.svg.png"))
 
a = arrow(pos=vector(0, 3, 0), axis=vector(0, -1, 0), color=color.green)

current_index = 0

my_choice = [] 
names = ["H", "He", "Na", "Cl", "O"]

while True:
    rate(60)
    
    ev = scene.waitfor('keydown')
  
    if ev.key == ' ':
        current_index = current_index + 1
        if current_index >= 5:
            current_index = 0
            
        target_pos = balls[current_index].pos
        a.pos = target_pos + vector(0, 3, 0) 

    if ev.key == '+':
        chosen_name = names[current_index] 
        my_choice.append(chosen_name)
        print("바구니에 담긴 원소들:", my_choice)
        
    if ev.key == 'Enter':
        h_count = my_choice.count("H")
        o_count = my_choice.count("O")  # 1) 
        
        if h_count == 2 and o_count == 1:
            print("★ 결합 성공! H2O 완료 ★")
            sphere(pos=vector(0, -4, 0), radius=1.5, color=color.blue)
        else:
            print("결합 실패!")
            
        my_choice = []
