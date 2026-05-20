#코드
ball = sphere(pos=vector(0, 0, 0), texture = "https://www.shutterstock.com/image-illustration/hydrogen-atom-model-showing-electron-600nw-2596229819.jpg")
ball = sphere(pos=vector(0, 0, -2.5), texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Electron_shell_002_Helium_-_no_label.svg/250px-Electron_shell_002_Helium_-_no_label.svg.png")
ball = sphere(pos=vector(0, 0, -5), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGPKIrzPenlG1RWuwI0Ql_4pk3kAxSRQoQHg&s")
ball = sphere(pos=vector(0, 0, -7.5), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyMihQTNJZjsp2hxUk4kIvP7it4VwstlpmXQ&s")
ball = sphere(pos=vector(0, 0, -10), texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Electron_shell_008_Oxygen_-_no_label.svg/250px-Electron_shell_008_Oxygen_-_no_label.svg.png")
a = arrow(pos = vector(0, 3, 0), color = color.green)
a.axis = vector(0, 0, 0) - a.pos
