#코드
Web VPython 3.2

balls = []

balls.append(sphere(pos=vector(-7.5, 0, 0), texture= "https://www.shutterstock.com/image-illustration/hydrogen-atom-model-showing-electron-600nw-2596229819.jpg"))
balls.append(sphere(pos=vector(-5, 0, 0), texture= "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Electron_shell_002_Helium_-_no_label.svg/250px-Electron_shell_002_Helium_-_no_label.svg.png"))
balls.append(sphere(pos=vector(-2.5, 0, 0), texture= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGPKIrzPenlG1RWuwI0Ql_4pk3kAxSRQoQHg&s"))
balls.append(sphere(pos=vector(0, 0, 0), texture= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyMihQTNJZjsp2hxUk4kIvP7it4VwstlpmXQ&s"))
balls.append(sphere(pos=vector(2.5, 0, 0), texture= "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Electron_shell_008_Oxygen_-_no_label.svg/250px-Electron_shell_008_Oxygen_-_no_label.svg.png"))
balls.append(sphere(pos=vector(5, 0, 0), texture= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAf-bd-0WCVJRGqoxWiZL78U18IHj3XuVxYg&s"))
balls.append(sphere(pos=vector(7.5, 0, 0), texture= "https://www.shutterstock.com/image-vector/nitrogen-chemical-element-icon-round-260nw-2138931285.jpg"))
 
a = arrow(pos=vector(0, 3, 0), axis=vector(0, -1, 0), color=color.green)

current_index = 0

my_choice = [] 
names = ["H", "He", "Na", "Cl", "O", "C", "N"]

while True:
    rate(60)
    
    ev = scene.waitfor('keydown')
  
    if ev.key == ' ':
        current_index = current_index + 1
        if current_index >= 7:
            current_index = 0
            
        target_pos = balls[current_index].pos
        a.pos = target_pos + vector(0, 3, 0) 

    if ev.key == '+':
        chosen_name = names[current_index] 
        my_choice.append(chosen_name)
        print("바구니에 담긴 원소들:", my_choice)
        
    if ev.key == 'e':
        h_count = my_choice.count("H")
        o_count = my_choice.count("O") 
        cl_count = my_choice.count("Cl") 
        na_count = my_choice.count("Na")
        c_count = my_choice.count("C")
        n_count = my_choice.count("N")# 1) 
        
        if h_count == 2 and o_count == 1:
            print("★ 결합 성공! 물 생성 완료 ★ ")
            sphere(pos=vector(0, -4, 0), texture = "https://cdn.ecocody.co.kr/news/photo/202304/4432_10130_335.jpg")
            
        elif cl_count == 1 and na_count ==1:
            print("★ 결합 성공! 소금 생성 완료 ★ "  )
            sphere(pos=vector(0, -4, 0), texture = "https://png.pngtree.com/png-clipart/20241121/original/pngtree-salt-png-image_17278352.png")
        
        elif o_count == 2 and c_count ==1:
            print("★ 결합 성공! 이산화탄소 생성 완료 ★ " )
            sphere(pos=vector(0, -4, 0), texture = "https://image.dongascience.com/Photo/2019/01/919f8ff9d2e91a764981fdfd9c22b717.jpg")
        
        elif o_count == 2 and h_count ==2:
            print("★ 결합 성공! 빨간약 생성 완료 ★ ")
            box(pos=vector(0, -4, 0), texture = "https://wimg.sedaily.com/news/legacy/2020/10/08/1Z91U7FT4M_1.jpg")
        
        else:
            print("결합 실패!")
            
        my_choice = []



CH_4 (메테인)(가스) CO_2 (이산화탄소) NaHCO_3 (탄산수소나트륨)(소화액) H_2O_2 (과산화수소)(소독약;빨간약)  NaCl (차아염소산나트륨)(락스) N_2O (아산화질소)(웃음이나는 마취제가스)
HCl (염화수소 / 염산) NaOH(수산화나트륨 / 가성소다)(비누) NH_3 (암모니아)(비료)$HCN$ (사이안화수소)(독성가스) NaNO_3 (질산나트륨)(소세지에 들어가는 빨간색 발색제)
